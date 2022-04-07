# -*- coding:utf-8 -*-

"""
    Nombre de la clase: Movie
    Descripción: Los objetos de esta clase constituiran nuestra lista de películas a partir de la cual se basa el programa. 
    Atributos: Nombre de la película, Id, Duración, Autor, Descripción y Género.
"""
class Movie:
    def __init__(self, name, id, time, autor, description, gender):
        self.name=name
        self.id=id
        self.time=time
        self.autor=autor
        self.description=description
        self.gender=gender

    """
        Método: str
        Descripción: Convierte a cadena una lista apartir de los atributos de la pelicula.
    """
    def __str__(self):
        return "[%s, %s, %s, %s]"%(self.name, self.time, self.autor, self.description)