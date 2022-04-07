#-*- coding: utf-8 -*-

import json
from Nucleo.Clases.LinkedList import*
from Nucleo.Clases.Movie import *

"""
    Nombre de la Clase: FileManager
    Descripción: La clase FileManager contiene los métodos importantes para escribir y
    leer en el disco un archivo de formato json que contiene las películas 
    en el invetario de películas.
    Atributos: ---
"""
class FileManager:
    def __init__(self):
        pass

    """
        Nombre de la Clase: readFileJSON
        Descripción: Metodo que recibe el nombre del archivo JSON y devuelve un
        objeto LinkedList.
        Parametros: Archivo JSON.
        Retorno: Una lista enlazada.
    """
    def readFileJSON(self, fileName=""):
        content=""

        with open(fileName) as file:
            content = json.load(file)
        ll=self.convertJSONToLinkedList(content)

        return ll

    """
        Método: writeInFile
        Descripción: Método que recibe como parámetro el archivo donde se va a ingresar la
        información y la lista enlazada de donde se obtiene dicha información.
        Parámetros: Un archivo y una lista enlazada.
        Retorno: ---
    """
    def writeInFile(self, fileName="", ll=None):
        content={}
        content=self.convertLinkedListToJSON(ll)
        
        with open(fileName, 'w') as file:
            json.dump(content, file, indent=4)
            


    """
        Método: convertJSONToLinkedList
        Descripción: Convierte el diccionario en una lista enlazada.
        Parametros: Un diccionario JSON.
        Retorno: Una lista enlazada.
    """
    def convertJSONToLinkedList(self, dictionary):
        ll=LinkedList()

        for k,i in dictionary.items():
            atribute=[]
            for j,z in i.items():
                atribute.append(z)

            name, id,time, autor, description, gender=atribute
            ll.push(Movie(name, id, time, autor, description, gender))
            
        return ll

    """
        Método: convertLinkedListToJSON
        Descripción: Convierte una lista enlazada en un diccionario.
        Parametros: Una lista enlazada.
        Retorno: Un diccionario JSON.
    """
    def convertLinkedListToJSON(self, ll):
        current=ll.first
        
        d={}
        count=0
        while(current):
            d[count]={}
            current=current.next
            count+=1
        
        arreglo=["name", "id", "time", "autor", "description", "gender"]

        current=ll.first
        for k, i in d.items():
            data=[current.value.name, current.value.id, current.value.time, current.value.autor, current.value.description, current.value.gender]
            for p in range (len(arreglo)):
                i[arreglo[p]]="%s"%(data[p])
            current=current.next

        return d

