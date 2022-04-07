# -*- coding:utf-8 -*-

from Nucleo.Clases.Movie import *
from Nucleo.Clases.MovieList import *
from Nucleo.Clases.ToSeconds import *


"""
    Nombre de la Clase: Table
    Descripción: Esta clase construye una tabla ASCII apartir de la lista de películas. Muestra: Id de la Película, Nombre de la Película, su Duración y la Descripción.
    Atributos: ---
"""
class Table:
    def __init__(self,MovieList):
        self.movieList = MovieList 


    """
        Método: generateTable
        Parametros: ---
        Descripción: Un apuntador recorre las peliculas y muestra los atributos antes mencionados en la descripción de la clase Table. La duración se muestra en segundos.
        Retorno: Retorna una varible que contiene en una cadena con formato la tabla.
    """
    def generateTable(self):
        tableHeading = ""
        tableHeading += "%s\n%s\n%s\n" % ("*"*100,"\t\tInventario de Peliculas".center(80," "),"*"*100)
        
        tableHeading += "Id.%s| Nombre \t| Duración\t\t | Descripción%s\n%s" % (" "*2,"","="*95)
        tableHeading += "\n"
        current = self.movieList.movieCatalogue.first
        count=0

        while(current):
    
            if ((len(current.value.name)>14)):
                name = current.value.name[0:14]
                setName = "%s..."%(name)
            else:
                name = current.value.name
                lName = len(name)
                setName = "%s%s"%(name, " "*(22-lName))

            if ((len(current.value.description)>60)):
                setDescription = current.value.description[0:55]
                setDescription = "%s..."%(setDescription)
            else:
                setDescription = current.value.description
                


            toSec = ToSeconds()
            time = str(toSec.toSeconds(current.value.time))
            lTime = len(time)
            setTime = "%s seg.%s"%(time, " "*(7-lTime))
            tableHeading+=("%s    | %s\t| %s\t\t| %s\n"%(count, setName, setTime, setDescription))
            tableHeading+=("-"*170)
            tableHeading+=("\n")
            if(current.next != None):
                current = current.next
                count+=1
            else:
                break

        return tableHeading

            
            
