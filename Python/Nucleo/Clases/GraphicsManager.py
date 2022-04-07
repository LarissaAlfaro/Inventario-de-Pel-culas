#-*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from Nucleo.Clases.BSTNode import *
from Nucleo.Clases.Movie import *


class GraphicsManager:
    def __init__(self):
        pass

    def generateTree(self, tree, l):
        G=nx.DiGraph()
        pos={}
        root=tree.root.value
        G.add_node(root)
        pos[root]=[l/2, 3]
    
        current=tree.root.children.first

        count = 0 
        while(current):
            if current.children.first:
                count+=1
            current=current.next

        sum=(l/count)
        x=int((l/count)/2)+1

        current=tree.root.children.first
        count=0
        while current:
            if (current.children.first):
                name1=current.value
                if len(name1)>13:
                    name1=name1[0:11]+"..."
                G.add_node(name1)
                G.add_edge(root, name1)
                pos[name1]=[x, 2]
                x+=sum
                current2=current.children.first
                while current2:
                    name2=current2.value
                    if len(name2)>10:
                        name2=name2[0:11]+"..."
                    G.add_node(name2)
                    G.add_edge(name1, name2)
                    pos[name2]=[count, 1]
                    current2=current2.next
                    count+=sum
            current=current.next
            
        plt.title("Categorias")
        nx.draw(G,pos=pos ,with_labels=True, arrows=False ,node_size=2000, node_color="#00CED1", font_size=8, node_shape='s')
        
        plt.axis([0, l, 0,4])
        plt.show()
        

    def generateBST(self, tree, h):
        self.h=h
        w=(2**h)
        G = nx.DiGraph()
        
        pos={}
        #Caso 1:colocar la raiz:
        name=tree.root.value.name
        time=tree.root.value.time
        if (len(name)>13):
            name=name[0:12]+"..."
        
        name="%s\n%s"%(name, time)
        G.add_node(name)
        pos[name]=[w/2, h]

        #Caso 2:llanear centro del arbol:
        
        self.addNodes(tree.root, pos,G , name, h-1, w/2, 2, w/2)

        plt.title("Binary Tree")
        nx.draw(G,pos=pos ,with_labels=True, arrows=False ,node_size=2000, node_color="#ADFF2F", font_size=7, node_shape='s')
        
        plt.axis([0, w-1, 0, h+1])
        plt.savefig("Nucleo/Memoria/BinaryTree.png", dpi=125, quality=99)

        plt.close()
        
        
        
        
    
    def addNodes(self, current, pos, G, parentName, y, w, div, wOriginal):
        if (current!= None):
            if current.left :
                name=current.left.value.name
                time=current.left.value.time
                if (len(name)>13):
                    name=name[0:12]+"..."
                nameI="%s\n%s"%(name, time)

                G.add_node(nameI)
                G.add_edge(parentName, nameI)
                pos[nameI]=[w-wOriginal/div, y]
                self.addNodes(current.left, pos, G, nameI, y-1, w-wOriginal/div, 2,wOriginal/div)

            if current.right:
                name=current.right.value.name
                time=current.right.value.time
                if (len(name)>13):
                    name=name[0:12]+"..."
                nameD="%s\n%s"%(name, time)

                G.add_node(nameD)
                G.add_edge(parentName, nameD)
                pos[nameD]=[w+wOriginal/div, y]
                self.addNodes(current.right, pos, G, nameD, y-1, w+wOriginal/div, 2,wOriginal/div)

            else:
                return True
    
    def addNodeInLeft(self, root, pos, G, parentName, y ,w, div=2):
        
        if (root!=None):
            if isinstance(root.value, Movie):
            
                name=root.value.name
                time=root.value.time
                if (len(name)>13):
                    name=name[0:12]+"..."
                nameI="%s\n%s"%(name, time)

                G.add_node(nameI)
                G.add_edge(parentName, nameI)
                pos[nameI]=[w, y]

                if div==0:
                    div=1
                if div == -1:
                    div=-2
                if isinstance(root.left, BSTNode):
                    self.addNodeInLeft(root.left, pos,G , nameI, y-1, w-w/div)
                if isinstance(root.right, BSTNode):
                    self.addNodeInRight(root.right, pos,G , nameI, y-1, w+w/div)
                    
                return True
            return True
        return True
    
    def addNodeInRight(self,root, pos, G, parentName, y ,w, div=2):
        if isinstance(root.value, Movie):
            name=root.value.name
            time=root.value.time
            if (len(name)>13):
                name=name[0:12]+"..."
            nameD="%s\n%s"%(name, time)

            G.add_node(nameD)
            G.add_edge(parentName, nameD)
            pos[nameD]=[w, y]

            if isinstance(root.left, BSTNode):
                self.addNodeInLeft(root.left, pos,G , nameD, y-1, w-w/div)
            if isinstance(root.right, BSTNode):
                self.addNodeInRight(root.right, pos,G , nameD, y-1, w+w/div)
                
            return True
        return True
