from Domain.restaurantValidator import RestaurantValidator
from Domain.reviewValidator import ReviewValidator
from Repository.json_repository import JsonRepository
from Service.restaurantService import RestaurantService
from Service.reviewService import ReviewService
from UserInterface.consola import Consola


def main():
    restaurantRepository = JsonRepository("restaurant.json")
    reviewRepository = JsonRepository("review.json")
    restaurantValidator = RestaurantValidator()
    reviewValidator = ReviewValidator()

    reviewService = ReviewService(reviewRepository, reviewValidator, restaurantRepository)
    restaurantService = RestaurantService(restaurantRepository,restaurantValidator)

    consola = Consola(restaurantService,reviewService)
    consola.runMenu()
if __name__ == '__main__':
    main()