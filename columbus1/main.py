import numpy as np
import pygame,sys
from pygame.math import Vector2,Vector3
from planet_choosing import *
from klasy import *
from planeta_zero import *
from kolko_i_krzyzyk import *
from Labirynt import *
from Paprociara import *
from chodzenie import *
from Zakonczenie import *
from Ksiezyc import *
from myszka import pierwszy_wybor
from functions import *

pygame.init()
pygame.font.init()



def main():

    """
    planeta_zero()
    loop = True
    #Ksiezyc()
    #Zakonczenie()
    input()
    while loop:
        temp = planet_choosing()
        if temp == 1:
            chodzenie()
            Game()
        if temp == 2:
            chodzenie()
            tic_tac_toeing()
    """
    print(planet_choosing(False))
if __name__ == '__main__':
    main()