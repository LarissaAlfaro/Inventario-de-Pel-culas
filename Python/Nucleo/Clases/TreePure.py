#-*- coding:utf-8

"""
    Nombre de la Clase: NodeTree
    Descripción: Esta clase nos permite crear los elementos(nodos) que constituyen el TDA árbol jerárquico.
    Atributos: value(valor del nodo), next(apunta al siguiente nodo), children(Tipo lista enlazada).
"""
class NodeTree:
    def __init__(self, value):
        self.value=value
        self.next=None
        self.children=LinkedListT()


"""
    Nombre de la Clase: TreePure
    Descripción: Mediante esta clase podemos crear un arbol jerárquica a partir de la lista de peliculas,
    y así mismo otras operaciones sobre este.
    Atributos: La raíz del árbol y sus hijos los cuales constituyen las categorias.
"""
class TreePure:
    def __init__(self):
        self.root=NodeTree("Categorias")
        self.root.children.push("Hechos Reales")
        self.root.children.push("Bélicas")
        self.root.children.push("Comedias Musicales")
        self.root.children.push("Acción")
        self.root.children.push("Artes Marciales")
        self.root.children.push("Aventuras")
        self.root.children.push("Ciencia Ficción")
        self.root.children.push("Comedia")
        self.root.children.push("Dibujos Animados")
        self.root.children.push("Documental")
        self.root.children.push("Espada y Hechicería")
        self.root.children.push("Espionaje")
        self.root.children.push("Horror")
        self.root.children.push("Misterio")
        self.root.children.push("Muertos Vivientes")
        self.root.children.push("Propaganda")
        self.root.children.push("Suspenso")
        self.root.children.push("Terror")
        self.root.children.push("Deportivas")
        self.root.children.push("Dramáticas")
        self.root.children.push("Fantásticas")
        self.root.children.push("Infantiles")
        self.root.children.push("Musicales")
        self.root.children.push("Policíacas")
        self.root.children.push("Psicológicas")
        self.root.children.push("Romanticas")
        self.root.children.push("Animales")
        self.root.children.push("Aviación")
        self.root.children.push("Delincuencia")
        self.root.children.push("Discapacitados")
        self.root.children.push("Religión")
        self.root.children.push("Política")

    """
        Método: push
        Descripción: Agrega elementos al árbol mediante el "push" de la lista enlazada.
        Parámetros: El valor que se desea agregar y una variable de tipo apuntador para recorrer las posiciones a donde se van a agregar los elementos.
        Retorno: ---
    """
    def push(self, value, current=None):
        if not current:
            current = self.root

        if not isinstance(current, NodeTree):
            return False

        current.children.push(value)

    """
        Método: search
        Descripción: Busca elementos en el árbol mediante el "search" de la lista enlazada.
        Parámetros: El valor que se desea buscar y una variable de tipo apuntador para recorrer las posiciones a lo largo de la búsqueda.
        Retorno: ---
    """
    def search(self, value, current=None):
        if not current:
            current=self.root.children

        if not isinstance(current, NodeTree):
            return False

        current.children.search(value)


    """
        Método: length
        Descripción: Recorre cada uno de los elementos de la lista enlazada que constituye el árbol para encontrar la longitud de este.
        Parámetros: Un apuntador y una variable contadora.
        Retorno: Una variable contadora con la longitud del árbol.
    """
    def length(self, current=None, count=0):
        if not current:
            current = self.root

        count+=current.children.length()

        curent2=current.children.first

        while(current2):
            if current2.children.first:
                self.length(current2, count)
            current2=curent2.next

        return count

""" 
    Nombre de la clase: LinkedListT
    Descripción: Esta clase nos permite crear una lista enlazada a partir de nodos. 
    Contiene diversos métodos que nos permiten hacer operaciones sobre esta.
    Atributos: first(primer nodo de la lista enlazada)
"""
class LinkedListT:
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
                self.first=NodeTree(value)
                self.first.next=current
                return True

            count+=1

            before=self.first
            current=before.next

            while(current):
                if(count==pos):
                    before.next= NodeTree(value)
                    before.next.next=current
                    return True

                before=before.next
                current=current.next

        else:
            if(not self.first):
                self.first=NodeTree(value)
                return True
            current=self.first
            while(current.next):
                current=current.next

            current.next=NodeTree(value)
            return True
    
    """
        *Método: pop
        *Parámetros: recibe el la posición del elemento que se desea eliminar. 
        *Descripcion: Si se ha ingresado una posición válida, se válida si es en la primera posición o en cualquier otra.
        Si es la primera posición se le asigna a "first" la referencia del siguiente elemento en la lista.          Si es en cualquier otra se hace referencia ,en el nodo anterior, al siguiente elemento después del elemento que borraremos.
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
    def search(self, value):
        if not self.first:
            return False
        """
        if position < 0 or position >= self.length():
            return False
        """
        current = self.first
        
        while(current):
            if (value==current.value):
                return current
            
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
    

