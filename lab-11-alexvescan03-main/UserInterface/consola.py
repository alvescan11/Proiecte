from Service.restaurantService import RestaurantService
from Service.reviewService import ReviewService


class Consola:
    def __init__(self,restaurantService:RestaurantService ,reviewService:ReviewService ):
        self.restaurantService = restaurantService
        self.reviewService = reviewService


    def runMenu(self):
        while True:
            print("1.Adauga restaurant")
            print("2.Adauga review")
            print("a1.Afiseaza restaurant")
            print("a2.Afiseaza review")
            print("3.Ordonare alfabetica")
            print("4.Nota medie")
            print("x.Iesire")
            print("5.ExportJson")
            optiune = input("Dati optiundea dumneavoastra: ")
            if optiune == "1":
                self.adaugaRestaurant()
            elif optiune == "a1":
                self.afisare(self.restaurantService.getAll())
            elif optiune == "2":
                self.adaugaReview()
            elif optiune == "a2":
                self.afisare(self.reviewService.getAll())
            elif optiune == "3":
                self.afisare(self.restaurantService.OrdonareAlfabetica())
            elif optiune == "4":
               print(self.reviewService.NotaMedie())
            elif optiune == "5":
                self.ExportJson()
            elif optiune == "x":
                break
            else:
                print("nu exista aceasta optiune")

    def adaugaRestaurant(self):
        try:
            idRestaurant = input("Dati id-ul restaurantului: ")
            if idRestaurant == "0":
                raise ValueError("id-ul nu poate fi nul")
            nume = input("Dati numele restaurantului: ")
            adresa = input("Dati adresa restaurantului: ")
            vegetarian = input("Specificati daca este vegetarian(da/nu)")
            if vegetarian == "da":
                vegetarian = True
            if vegetarian == "nu":
                vegetarian =False
            self.restaurantService.adauga(idRestaurant,nume,adresa,vegetarian)
            self.afisare(self.restaurantService.getAll())
        except Exception as e:
            print(e)

    def afisare(self,listaEntitati):
        for entitate in listaEntitati:
            print(entitate)

    def AfisareDictionar(self,lista):
        for entitate in lista:
            print(str(entitate) + ":" + str(entitate[lista]))

    def adaugaReview(self):
        try:
            idReview = input("Dati id ul reviewului: ")
            if idReview == "0":
                raise ValueError("id-ul nu poate fi nul")
            idRestaurant = input("Dati id ul restaurantului: ")
            numeClient = input("Dati numele clientului: ")
            comentariu = input("Dati comentariu: ")
            nota = int(input("Dati nota: "))

            self.reviewService.adauga(idReview,numeClient,idRestaurant,comentariu,nota)
            self.afisare(self.reviewService.getAll())
        except Exception as e:
            print(e)

    def ExportJson(self):
        try:
            filename = input("Dati numele fisierului unde sa va face exportul: ")
            self.reviewService.Export_json(filename)
        except Exception as e:
            print(e)







