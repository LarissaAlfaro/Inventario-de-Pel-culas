# -*-coding:utf-8 -*-
from Nucleo.Clases.BSTNode import *
from Nucleo.Clases.LinkedList import *
from Nucleo.Clases.ToSeconds import*
from Nucleo.Clases.Movie import*
#from Nucleo.Clases.MovieList import*

"""
    *Nombre de clase: BST
    *Atributos: root(raiz del arbol binario)
    *Descripción: Mediante esta clase podemos crear un arbol binario a partir de la lista de peliculas,
    y así mismo otras operaciones sobre este:
    remover, buscar, y encontrar subárbol.
"""
class BST:
    def __init__(self):
        self.root=None 

    def add(self,Movie): 
        return self.innerAdd(Movie,self.root) 

    """
        *Método: innerAdd
        *Parámetros: recibe un objeto de tipo pelicula y un puntero.
        *Descripcion: Recibe el objeto de tipo pelicula y obtiene su duración. Luego si el árbol esta vacío,el elemento se
        agrega en la raíz del árbol y si no, compara la duración de la película a ingresar con la del nodo "actual" al que 
        se esta apuntando. Si es menor se agrega a la izquierda, y si es mayor a la derecha, esto, de no haber un elemento 
        en estas posiciones. Si ya existe, se retona un llamado recursivo a la misma función, tomando la posición "izquierda" 
        o "derecha" del nodo actual como refrencia.
        *Retorno: True-se agregó la pelicula exitosamente.
                False-no se logró añadir película.
    """
    

    def innerAdd(self,film,current):
        
        if isinstance(film,Movie):
            toSec=ToSeconds()
            valueFilm=toSec.toSeconds(film.time)

            if (not self.root):
                self.root=BSTNode(film)
                return True

            if isinstance(current, BSTNode):
                if toSec.toSeconds(current.value.time)<valueFilm:
                    if not current.right:
                        current.right=BSTNode(film)
                        return True
                    return self.innerAdd(film,current.right)

                elif toSec.toSeconds(current.value.time)>valueFilm:
                    if not current.left:
                        current.left=BSTNode(film)
                        return True
                    return self.innerAdd(film,current.left)
        
            return False
        
        return False


    def search(self,value):
        return self.innerSearch(value,self.root)
    
    """
        *Método: innerSearch
        *Parámetros: recibe el valor a buscar y un apuntador.
        *Descripcion: Busca el elemento comparando el valor ingresado con el valor al cual se apunta.
        Si es menor o mayor se retorna un llamado recursivo de la función tomando como referencia el
        nodo a la izquierda o a la derecha respectivamente. El proceso se repite hasta que se encuentra 
        el valor.
        *Retorno: True-se encontró el valor.
                  False-el árbol esta vacío, el apuntador no hace referencia a un objeto de tipo BSTNode, 
                    o si no se encontró el valor.
    """

    def innerSearch(self,value,current):

        if not self.root:
            return False

        if isinstance(current,BSTNode):
            if(current.value==value):
                return True
            
            elif(current.value>value):
                if not current.left:
                    return False
                return self.innerSearch(value,current.left)

            else:
                if not current.right:
                    return False
                return self.innerSearch(value,current.right)
        else:
            return False         


    def subTree(self,value):
        return self.innersubTree(value,self.root)


    """
        Método: innerSubTree
        Parametros: Valor del cual deseamos obtener el sub árbol y una varible tipo apuntador.
        Descripción: Busca el nodo que contenga el valor ingresado mediante comparación. Cuando finalmente
        se encuentra el valor se instancia un objeto de tipo árbol y se se le asigna a su raiz la dirección 
        del valor ingresado.
        Retorno: -Retorna el subárbol encontrado.
                 -Retorna None si no se apunta a una variable de tipo BSTNode o si no se encontró el valor ingresado.

    """
    def innersubTree(self,value,current):
        if not self.root:
            return None 
        
        if isinstance(current,BSTNode):
            if current.value==value:
                tree=BST()
                tree.root=current
                return tree 
            
            elif current.value>value:
                if not current.left:
                    return None 
                return self.innersubTree(value,current.left)
            
            else:
                if not current.right:
                    return None 
                return self.innersubTree(value,current.right)
        else:
            return None 

    """
        *Método: convert
        *Parámetros: recibe una lista de películas.
        *Descripcion: Se ingresa un elemento, y si es del tipo de lista de película entonces se hace referencia al
        primer elemento. Si este tiene un valor, entonces se agrega el valor a un nodo de árbol, y se pasa al 
        siguiente elemento. Mientas los nodos no tengan una referencia a "None" y se haya terminado de convertir la 
        lista, el proceso de converión se repite. Como resultado cada nodo ahora sera del tipo nodo de árbol binario.
        *Retorno: True-se convirtió cada nodo de forma exitosa.
                False-no se lograron convertir los elementos.
    """
    
    def convert(self,record):
        if isinstance(record,LinkedList):
            current=record.first
            while(current):
                value=current.value
                self.add(value)
                current=current.next
            return True
        else:
            return False

    
    """
        *Método: height
        *Parámetros: recibe una variable de tipo puntero y una variable contador.
        *Descripcion: Este método calcula la altura del árbol. Inicialemente, 
        al no recibir el parámetro de tipo  puntero, cuenta a la raíz como primer elemento. 
        Luego, se navega hacia abajo evaluando cada siguiente nivel del nodo actual. 
        Si este nodo tiene un hijo, se hace un llamado recursivo con referencia a este y 
        con el contador que incrementa a 1. Si tiene ambos hijos entonces se hace un llamado 
        recursivo a cada uno y se evalua luego cual de estos tiene el subarbol más largo,
         para tomar este como el contador a retornar. 
        *Retorno: El contador total de todo el árbol.
    """
    def height(self, current=None, count=0):
        if not current:
            current=self.root
            count=1

        if current.left and current.right:
            count+=1
            countLeft= self.height(current.left, count)
            countRight= self.height(current.right, count)

            if(countLeft > countRight):
                return countLeft
            elif(countLeft < countRight):
                return countRight
            else:
                return countLeft
        
        elif current.left and not current.right:
            return self.height(current.left, (count+1))

        elif current.right and not current.left:
            return self.height(current.right, (count+1))

        else:
            return count
    """
        *Método: create
        *Parámetros: recibe una lista de películas.
        *Descripcion: Este método recibe una lista de películas e instancia un objeto de tipo árbol. 
        Luego de esto, hace uso del método "convert" del árbol recien creado para convertir la lista. 
        *Retorno: Retorna el árbol que se ha creado.
                Retorna "None" si el párametro que se ingresó no era del tipo lista de películas.
    """



    def create(self,record):
        if isinstance(record,LinkedList):
            treeC=BST()
            treeC.convert(record)
            return treeC 
            """NOTA=de donde se llame a esta funcion(main, etc.) se debe crear una variable
                    que almacene el arbol que se retorna, si no, este se perderá."""
        else:
            return None

    
    
  