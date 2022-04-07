#-*- coding:utf-8 -*-
"""
    *Nombre de clase: ToSeconds
    *Atributos: ----
    *Descripción: Esta clase contiene un único método encargado de convertir el valor de duración de una película
    del formato "HH:MM:SS" a segundos.
"""
class ToSeconds:

    def __init__(self):
        pass

    """
        *Método: toSeconds
        *Parámetros: recibe el valor en formato "HH:MM.SS"
        *Descripcion: Separa la cadena que se recibe por cada ":", mediante el método split,  y se almacena cada elemento 
        resultante en una variable. Las variables representan las horas, minutos y segundos respectivamente.Por último 
        se retorna la suma de estos valores convertidos a enteros multiplicados por su equivalente en segundos.
        *Retorne: el equivalente en segundos del parámetro ingresado.
    """

    def toSeconds(self,HMS):

        h,m,s = HMS.split(":")

        return int(h)*3600 + int(m)*60 + int(s)


