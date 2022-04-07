# -*- coding:utf-8 -*-

from Nucleo.Clases.LinkedList import *

"""
    Nombre de la Clase: MovieList
    Descripción: Crea una lista de películas en base a una lista enlazada.
    Atributos: Una lista enlazada.
"""
class MovieList:

    def __init__(self):
        self.movieCatalogue = LinkedList()

    """
        Método: moviePush
        Parámetros: Objeto de tipo película.
        Descripción: Agrega elementos a la lista de películas por medio del "agregar" del TDA lista enlazada.
        Retorno: ---
    """
    def moviePush(self,obj): 
        self.movieCatalogue.push(obj)

    """
        Método: moviePop
        Parámetros: La posición del elemento que se desea eliminar.
        Descripción: Elimina elementos de la lista de películas por medio del "borrar" del TDA lista enlazada.
        Retorno: ---
    """
    def moviePop(self,pos):
        self.movieCatalogue.pop(pos)


    """
        Método: movieSearch
        Parámetros: La posición del elemento que se desea buscar.
        Descripción: Busca elementos en la lista de películas por medio del "buscar" del TDA lista enlazada.
        Retorno: ---
    """
    def movieSearch(self,pos):
        self.movieCatalogue.search(pos) 
