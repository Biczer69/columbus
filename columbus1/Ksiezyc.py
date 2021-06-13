import pygame
from kolko_i_krzyzyk import tic_tac_toeing
import Zakonczenie


class Ksiezyc(object):
    def __init__(self):
        print("Wiesz już, że kwiat paproci znajduje się na Księżycu. Udaj się tam.")
        print("Witaj na Księżycu! To tutaj odnajdziesz mistyczny kwiat paproci, który ma Ci zapewnić wieczne szczęście. ")
        tic_tac_toeing()
        print("""\
            Widzisz przed sobą kwiat paproci. Może on zagwarantować Ci wieczne szczęście, 
            spełnić Twoje wszelkie marzenia i dać Ci wszystko czego potrzebujesz. Pamiętaj 
            jednak, że żadną z tych rzeczy nie możesz się podzielić. Czy zerwiesz paproć, 
            czy po tej męczącej i niebezpiecznej podróży, wolisz zostawić sprawy takimi jak 
            się mają?
            """)
        wybor_konca = int(input("Wybierz 1: Odejdź bez paprotki\nWybierz 2: Zerwij paproć"))
        if wybor_konca == 1:
            print("""\
                Zdecydowałeś/zdecydowałaś się odejść bez kwiatu paproci. Czy była to dobra decyzja?    
                Trudno powiedzieć. Pamiętaj, że zawsze możesz spróbować go zdobyć przy następnej 
                koniunkcji planet.""")
        else:
            z = Zakonczenie()




