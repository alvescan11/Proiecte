from Domain.restaurant import Restaurant


class RestaurantValidator:
    def valideazaRestaurant(self,restaurant:Restaurant):
        erori = []
        if restaurant.nume == '':
            erori.append("numele trebe sa fie nenul")
        if restaurant.vegetarian !=True and restaurant.vegetarian !=False:
            erori.append("Trebe sa fie True sau False")
        if erori:
            raise ValueError(erori)

