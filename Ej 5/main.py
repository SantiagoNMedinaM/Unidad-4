from classPelicula import Pelicula
from claseVista import AplicacionPelicula
import tkinter as tk
import json
from classObjectEncoder import ObjectEncoder
from ModeloPelicula import ModeloPelicula
from classPelicula import Pelicula
from controladorPelicula import Controlador



def main():
    apiKey = "689d020aea348a7e0e9174f6bd16149c"
    api_Manager = ModeloPelicula(apiKey)
    vista = AplicacionPelicula()
    encoder = ObjectEncoder("generos.json")
    controlador = Controlador(api_Manager, vista, encoder)
    vista.mainloop()

if __name__ == '__main__':
    main()