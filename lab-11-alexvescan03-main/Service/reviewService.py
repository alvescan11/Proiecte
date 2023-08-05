import jsonpickle

from Domain.review import Review
from Domain.reviewValidator import ReviewValidator
from Repository.json_repository import JsonRepository


class ReviewService:
    def __init__(self,reviewRepository:JsonRepository,reviewValidator:ReviewValidator,
                 restaurantRepository:JsonRepository):
        self.reviewRepository = reviewRepository
        self.reviewValidator = reviewValidator
        self.restaurantRepository = restaurantRepository

    def getAll(self):
        return self.reviewRepository.read()

    def adauga(self, idReview: str, numeClient: str, idRestaurant: str, comentariu: str, nota: int):
        if self.restaurantRepository.read(idRestaurant) is None:
            raise KeyError("nu exista acest restaurant")
        review = Review(idReview,numeClient,idRestaurant,comentariu,nota)
        self.reviewValidator.valideazaReview(review)
        self.reviewRepository.create(review)

    def NotaMedie(self):
        rezultat = {}
        for restaurant in self.restaurantRepository.read():
            for review in self.reviewRepository.read():
                i = 1
                if review.id_restaurant == restaurant.id_entity:
                    if restaurant.nume in rezultat:
                        i += 1
                        rezultat[restaurant.nume]["nota medie"] += review.nota
                    if restaurant.nume not in rezultat:
                        rezultat[restaurant.nume] = {
                                "nota medie": review.nota
                        }
                    rezultat[restaurant.nume]["nota medie"] = rezultat[restaurant.nume]["nota medie"] / i
        return rezultat



    def Export_json(self,filename: str):
        rezultat = {}
        for restaurant in self.restaurantRepository.read():
            rezultat[restaurant.nume] = []
        for review in self.reviewRepository.read():
            restaurant = self.restaurantRepository.read(review.id_restaurant)
            rezultat[restaurant.nume].append(review.comentariu)

        with open(filename, "w") as f:
            f.write(jsonpickle.dumps(rezultat))



