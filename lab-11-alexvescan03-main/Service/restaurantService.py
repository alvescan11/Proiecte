from Domain.restaurant import Restaurant
from Domain.restaurantValidator import RestaurantValidator
from Repository.json_repository import JsonRepository


class RestaurantService:
    def __init__(self,restaurantRepository:JsonRepository,restaurantValidator:RestaurantValidator):
        self.restaurantRepository = restaurantRepository
        self.restaurantValidator = restaurantValidator

    def getAll(self):
        return self.restaurantRepository.read()

    def adauga(self,idRestaurant: str, nume: str, adresa:str, vegetarian: bool):
        restaurant = Restaurant(idRestaurant,nume,adresa,vegetarian)
        self.restaurantValidator.valideazaRestaurant(restaurant)
        self.restaurantRepository.create(restaurant)

    def OrdonareAlfabetica(self):
        rezultat = []
        for restaurant in self.restaurantRepository.read():
            if restaurant.vegetarian is True:
                rezultat.append(restaurant)
        return sorted(rezultat, key = lambda x:x.nume)

