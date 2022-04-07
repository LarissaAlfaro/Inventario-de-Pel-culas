#-*-coding :utf-8 -*-

"""
    Nombre de la clase: BSTNode
    Descripción: Esta clase nos permite crear los elementos(nodos) que constituyen el TDA árbol binario.
    Atributos: value(valor del nodo), right(apunta al hijo derecho), left(apunta al hijo izquierdo.)
"""
class BSTNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
