#-*- coding:utf-8 -*-

"""
    Nombre de la clase: Node
    Descripción: Esta clase nos permite crear los elementos(nodos) que constituyen el TDA lista enlazada.
    Atributos: value(valor del nodo), next(apunta al próximo elemento)
"""
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

"""
    Nombre de la clase: LinkedList
    Descripción: Esta clase nos permite crear una lista enlazada a partir de nodos. 
    Contiene diversos métodos que nos permiten hacer operaciones sobre esta.
    Atributos: first(primer nodo de la lista enlazada)
"""

class LinkedList:
    def __init__(self):
        self.first=None

    
    """
        *Método: push
        *Parámetros: recibe el valor a agregar y la posición donde se desea agregar. 
        *Descripcion: Si se ha ingresado una posición, se evalua si es en la primera posición 
        o en cualquier otra. Se recorren los elementos de la lista hasta encontrar la posición en
        la que deseamos agregar. Si no se ingresa una posición o es una posición mayor a la longitud,
        entonces, si esta vacía agrega en la primera posición y si no se agrega al final.
        *Retorno: True-se agregó el valor exitosamente.
    """
    def push(self, value, pos=-1):
        if(pos>=0 and pos<self.length()):
            count=0
            if(count==pos):
                current=self.first
                self.first=Node(value)
                self.first.next=current
                return True

            count+=1

            before=self.first
            current=before.next

            while(current):
                if(count==pos):
                    before.next= Node(value)
                    before.next.next=current
                    return True

                before=before.next
                current=current.next

        else:
            if(not self.first):
                self.first=Node(value)
                return True
            current=self.first
            while(current.next):
                current=current.next

            current.next=Node(value)
            return True


    """
        *Método: pop
        *Parámetros: recibe el la posición del elemento que se desea eliminar. 
        *Descripcion: Si se ha ingresado una posición válida, se válida si es en la primera posición o en cualquier otra.
        Si es la primera posición se le asigna a "first" la referencia del siguiente elemento en la lista. Si es en cualquier 
        otra se hace referencia ,en el nodo anterior, al siguiente elemento después del elemento que borraremos.
        *Retorno: True-se eliminó el elemento
                  False-no se eliminó el elemento(la lista esta vacía, no se ingresó la posición, o la posición es mayor 
                    al tamaño de la lista)
    """
    def pop(self, position=None):
        if(not self.first): #si la lista esta vacia
            return False

        if(position>self.length()-1): #se ingresa una posicion mayor a la lista
            return False

        if position == None: #no se ingresa posicion
            return False

        if position==0: #eliminar el primer elemento de la lista
            self.first=self.first.next
            return True

        else: #una posicion cualquiera existente diferente a 0            
            count=0
            before=self.first
            current=self.first.next
            while count!=(position-1):
                count+=1
                before=before.next
                current=current.next

            before.next=current.next
            return True

    """
        *Método: length
        *Parámetros: ---
        *Descripcion: Mediante una varible de tipo apuntador se recorren las posiciones de la lista enlazada
        y por cada elemento que se recorre, una varible de tipo contador incrementa en uno. Se termina de "contar"
         cuando se encuentra una referencia a "null".
        *Retorno: 0-la lista esta vacía
                  count-el número de elementos en la lista enlazada.
    """
    def length(self):
        if(not self.first):
            return 0

        count=0
        current=self.first

        while(current):
            count+=1
            current=current.next

        return count

    
    """
        *Método: search
        *Parámetros: recibe la posición que se busca.
        *Descripcion: Se recorren los elementos de la lista enlazada, y por cada elemento que se recorre 
        el contador aumenta en uno. Cuando la posición ingresada sea igual al contador, se regresa el valor del
        nodo en esta posición.
        *Retorno: False-la lista esta vacía, la posición ingresada no existe.
                  Retorna el valor en dicha posición.
    """
    def search(self, position):
        if not self.first:
            return False

        if position < 0 or position >= self.length():
            return False

        current = self.first
        count=0
        while(current):
            if (count==position):
                return current.value
            count+=1
            current=current.next

        return False


    """
        *Método: __str__
        *Parámetros: ---
        *Descripcion: Se recorre cada elemento del arreglo con una variable apuntador y se convierte 
        cada valor en una cadena.
        Cada elemento se concatena a una variable de tipo string para su posterior retorno.
        *Retorno: la cadena donde estan incluídos todos los elementos de la lista enlazada.
    """
    def __str__(self):
        if not self.first:
            return "null"

        current=self.first
        txt=""
        while(current):
            txt+=str(current.value)
            txt+="-->"
            current=current.next

        txt+="null"
        return txt