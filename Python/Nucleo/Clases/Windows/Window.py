#-*- coding: utf-8 -*-

#Clases de las componentes graficas
from Nucleo.InterfazGraficaProyecto.MainWindow_ui import *
from Nucleo.InterfazGraficaProyecto.AddMenu_ui import *
from Nucleo.InterfazGraficaProyecto.ViewAndEditMenu_ui import *
from Nucleo.InterfazGraficaProyecto.About_ui import *
from Nucleo.InterfazGraficaProyecto.ExitoAdd_ui import *
from Nucleo.InterfazGraficaProyecto.Advertencia_ui import *
from Nucleo.InterfazGraficaProyecto.EditMenu_ui import *

#Clases de las componentes graficas y de mensahjes de advetencia
from Nucleo.InterfazGraficaProyecto.VentanasEmegentes.EmergenteAgregar_ui import *
from Nucleo.InterfazGraficaProyecto.VentanasEmegentes.EmergenteEliminar_ui import *

#Importando la libreria Qt para Python
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog, QDesktopWidget
from PyQt5.QtCore import QTime, QTimer

#Clases Utilizadas de encasulamiento y abstraccion
from Nucleo.Clases.LinkedList import *
from Nucleo.Clases.FileManager import *
from Nucleo.Clases.Movie import *
from Nucleo.Clases.Table import *
from Nucleo.Clases.MovieList import *
from Nucleo.Clases.GraphicsManager import *
from Nucleo.Clases.BST import*
from Nucleo.Clases.TreePure import *

import time as t

#Librerias y frameworks para la visualizacion de los arboles
from PIL import Image
import matplotlib.pyplot as plt

#Se crea el objeto que servira para leer el Jsonb y escribir en el
fm=FileManager()

#se guarde la ruta del archivo en una variable str
fileName="Nucleo/Memoria/data.json"



"""
    Esta clase contiene La ventana principal, que es la ejecutada en main.py:
        Son utilisados los conseptos de Herencia y Encapsulamiento
"""
class MainWindow(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.ll=LinkedList()
        """
            self.ll es una lista enlasada que al momento de ejecutar la 
            clase en el main es cargarda desde un archivo JSON usando la clase
            FileManager y el metodo readFileJSON() de la misma
        """
        self.ll=fm.readFileJSON(fileName)

        """
            esta instancia de la clase GraphicsManager se utilizara en los 
            metodos de la graficacion de arbol y su visualizacion
        """
        self.gM=GraphicsManager()
        
        """
            En el siguiente apartado estan los botones de la ventana principal
            y la funcion q se ejecutara al precionarlos
        """
        self.Add.clicked.connect(self.add)
        self.ViewAndEdit.clicked.connect(self.viewAndEdit)
        self.Display.clicked.connect(self.tree)
        self.Display.clicked.connect(self.tree2)
        self.About.clicked.connect(self.about)

        #Esta funcion se encargar de centrar la ventana en la pantalla
        self.center()

        #esta porcion de codigo es utilizado para el contador de peliculas
        timer=QTimer(self)
        timer.timeout.connect(self.showCant)
        timer.start(1000)
        self.showCant()
        
    #Metodo encargado de actualizar el numero de peliculas en el inventario
    def showCant(self):
        time=QTime.currentTime()
        text=0
        if isinstance(time.second(), int):
            self.ll=fm.readFileJSON(fileName)
            text=self.ll.length()

        self.lcdNumber.display(text)
    
    #Funcion ejecutada por el boton add de la ventana principal que ejecuta
    #El Componente grafico de la ventana add usando la clase addWindow teniendo como
    #padre la clase que ejecuta a la ventana principal
    def add(self):
        window=AddWindow(self)
        window.show()

    #Ejecuta le ventana de ver y editar de la clase LookEditWindow
    def viewAndEdit(self):
        window=LookEditWindow(self)
        window.show()

    #visualizacion del arbol binario
    def tree(self):
        binaryTree=BST()
        binaryTree.convert(self.ll)
        
        self.gM.generateBST(binaryTree, binaryTree.height())

        im= Image.open("Nucleo/Memoria/BinaryTree.png")
        im.show()
        
        
    #Visualizacion del Arbol de Categorias
    def tree2(self):
        gM=GraphicsManager()
        t = TreePure()

        current=self.ll.first

        while current:
            current2=t.root.children.first
            while(current2):
                if current2.value.strip() == current.value.gender.strip():
                    #print(current2.value)
                    t.push(current.value.name, current2)
                current2=current2.next
            current=current.next

        print("%s"%t.root.children.first.children)

        gM.generateTree(t, self.ll.length())
        """
        im= Image.open("Nucleo/Memoria/Categoria.png")
        im.show()
        """
        
    #Abre la ventana Que contiene la informacion del proyecto
    def about(self):
        window=AboutWindow(self)
        window.show()

    #esta funcion es utilizada en casi todas las ventanas y sirve 
    #para abrir estas en el centro de la pantalla
    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

#De la linea 150 a 282 Todo el codido para la ventana de AÑADIR PELICULA.
class AddWindow(QtWidgets.QMainWindow, Ui_Add):
    def __init__(self, parent=None,name="", time="", description="", autor="", gender=""):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        #Se carga la Lista desde el archivo JSON
        self.ll=fm.readFileJSON(fileName)

        self.TxtName.setText(name)
        self.TxtTime.setText(time)
        self.TxtDescription.setText(description)
        self.TxtDirector.setText(autor)
        
        self.pushButton_3.clicked.connect(self.abort)
        self.pushButton_2.clicked.connect(self.save)

        self.center()

    #Metodo que desplega una ventana de confirmar si quiere cancelar lo que esta agregando
    def abort(self):
        
        self.name=self.TxtName.text()
        self.time=self.TxtTime.text()
        self.description=self.TxtDescription.toPlainText()
        self.autor=self.TxtDirector.text()
        self.gender=self.comboBox.currentText()
        
        """
            a la clase ConfirmAbortWindow se le pasan todos los valores en el formulario 
            escritos hasta el momento porque si la respuesta del usuario es negativa volver 
            abrir la ventana de add y no pierda lo que habia escrito
        """
        window=ConfirmAbortWindow(self, self.name, self.time, self.description, self.autor, self.gender)
        window.show()
        self.close()
        return True

    #Este metodo se encarga de guardar todo en memoria permanente(archivo JSON) y desplegar una ventana de exito 
    def save(self):
        if(
            self.TxtName.text()=="" or
            self.TxtTime.text()=="" or
            len(self.TxtTime.text())<7 or len(self.TxtTime.text())>8 or
            self.TxtDescription.toPlainText()=="" or
            self.TxtDirector.text()=="" or
            self.comboBox.currentText()=="[Seleccione el Género de la Película]"
        ):
        
            window1=AdvertenciaAdd(self)
            window1.show()
            return 0

        self.name=self.TxtName.text()
        self.time=self.TxtTime.text()
        self.description=self.TxtDescription.toPlainText()
        self.autor=self.TxtDirector.text()
        self.gender=self.comboBox.currentText()

        self.ll.push(Movie(self.name,"%s"%self.ll.length(), self.time, self.autor ,self.description, self.gender))
        
        fm.writeInFile(fileName, self.ll)

        window = ConfirmAddWindow(self)
        window.show()
        self.TxtName.clear()
        self.TxtTime.clear()
        self.TxtDescription.clear()
        self.TxtDirector.clear()
        return True

    #Metodo que se encarga de que la ventana add se abra en el centro de la pantalla
    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

"""
    Esta ventana es utilizada en el evento del boton save de la ventana add y 
    advierte al usuario que no se han llenado los campos necesarios para guardarlo 
    o que el formato del tiempo es invalido
"""
class AdvertenciaAdd(QtWidgets.QMainWindow, Ui_Advertencia):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.center()

        self.pushButton.clicked.connect(self.regresar)
    
    def regresar(self):
        self.close()

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

"""
    La clase ejecutada al momento de precionar el voton de save en la ventana add 
    y desplega una ventana con un mensaje de exito, que confirma la agregacion de
    la pelicula al inventario
"""
class ConfirmAddWindow(QtWidgets.QMainWindow, Ui_Exito):
    def __init__(self, parent=None, op=0):
            
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        if op==1:
            self.label.setText("Pelicula Editada con exito")
        self.pushButton.clicked.connect(self.close)

        self.center()

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def aceptar(self):
        self.close()


"""
    Es la clase que se desplega al presionar el boton del cesto de basura en la ventana 
    add y esta clase desplega el mensaje de advertencia que va a cancelar una accion, 
    previamente iniciada
"""
class ConfirmAbortWindow(QtWidgets.QMainWindow, Ui_confirmAdd):

    def __init__(self, parent=None, name="", time="", description="", autor="", gender="", op=1 , ll=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        self.ll=ll
        self.op=op
        self.name=name
        self.time=time
        self.description=description
        self.autor=autor
        self.gender=gender

        self.center()
        self.pushButton_3.clicked.connect(self.action)
        self.pushButton.clicked.connect(self.close1)

    def close1(self):
        self.close()
        
    def action(self):
        if self.op==-1:
            window = AddWindow(self, self.name, self.time, self.description, self.autor, self.gender)
            window.show()
            self.close()
        else:
            window = EditWindow(self, self.op, self.ll)
            window.show()
            self.close()

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
#fIN del codigo relacionado con la ventana de añadir.       


"""
    Clase que contiene la interfaz grafica del boton acerca de y muetra toda la 
    info del proyecto
"""
class AboutWindow(QtWidgets.QMainWindow, Ui_About):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.center()

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

#linea 337 a linea 378 todo el codigo de la ventana ver y editar
"""
    Clase que contiene la interfaz grafica donde se muestran las peliculas en el inventario
    desplegadas en una tabla ASCCI, y contiene los botones editar y eliminar
"""
class LookEditWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.id=id
        self.ll=fm.readFileJSON(fileName)
        
        listMovie=MovieList()

        listMovie.movieCatalogue=self.ll

        table=Table(listMovie)

        self.textEdit.insertPlainText(table.generateTable())

        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton_2.clicked.connect(self.edit)

        
        self.center()

    """
        esta funcion es ejecutada a precionar el boton del sesto que es para eliminar una pelicula
        y desplega una ventana de confirmacion , se le pasa la lista enlazada y el id a la clase 
        que contiene esta interfaz grafica de esta ventanita par decidir el destino de la pelicula
    """
    def delete(self):
        self.id=self.lineEdit.text()
        window=ConfimRemoveWindow(self, self.ll, self.id)
        window.show()
        self.close()

    """
        Ejecuta la clase que tiene lcomponente grafica de la ventana edit i al constructor
        se le pasa el id y la lista enlazada para cargar los datos de cada componente en la
        ventana y sea mas facil editarlo
    """
    def edit(self):
        self.id=self.lineEdit.text()
        window=EditWindow(self ,self.id, self.ll)
        window.show()
        self.close()

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    
"""
    En esta clase se encuentra el incializador de la ventana edit y que contiene todos los eventos
    de los botones para editar o cancellar accion
"""
class EditWindow(QtWidgets.QMainWindow, Ui_editMovie):
    def __init__(self, parent=None, id="", ll=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        #Carga la lista y el id enviados por la ventana ver y editar en lineas 402 y 403
        self.id=int(id)
        self.ll=ll

        obj=self.ll.search(self.id)

        #carga todos los valores en el formulario para ser editados
        self.TxtName.setText(obj.name)
        self.TxtTime.setText(obj.time)
        self.TxtDescription.setText(obj.description)
        self.TxtDirector.setText(obj.autor)
        self.comboBox.setCurrentText(obj.gender)

        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton_2.clicked.connect(self.save)
        self.center()

    #esta funcion solo pregunta si esta seguro el usuario de no editar nada de la pelicula o continuar
    def delete(self):
        #Esta instancia contiene la componente grafica de la ventana de emergencia
        window = ConfirmAbortWindow(self, op=self.id, ll=self.ll)
        window.show()
        self.close()
    
    #Verifica que todo este en su lugar y con el formato deceado para guardarlo o advertirle al usuario que le falta llenar campos
    def save(self):
        if(
            self.TxtName.text()=="" or
            self.TxtTime.text()=="" or
            len(self.TxtTime.text())<7 or len(self.TxtTime.text())>8 or
            self.TxtDescription.toPlainText()=="" or
            self.TxtDirector.text()=="" or
            self.comboBox.currentText()=="[Seleccione el Género de la Película]"
        ):
        
            window1=AdvertenciaAdd(self)
            window1.show()
            return 0

        name=self.TxtName.text()
        time=self.TxtTime.text()
        description=self.TxtDescription.toPlainText()
        autor=self.TxtDirector.text()
        gender=self.comboBox.currentText()
        self.ll.search(self.id).name=name
        self.ll.search(self.id).time=time
        self.ll.search(self.id).description=description
        self.ll.search(self.id).autor=autor
        self.ll.search(self.id).gender=gender

        #escribe en el Json la lista enlazada
        fm.writeInFile(fileName, self.ll)
        
        self.close()

        #Ventana que confirma que se anadio con exito la pelicula
        window1=LookEditWindow(self)
        window1.show()
        window=ConfirmAddWindow(self, op=1)
        window.show()

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
        
"""
    Clase que contiene las componentes graficas para verificcar si el usuario esta 
    seguro de querer eliminar la pelicula.
"""
class ConfimRemoveWindow(QtWidgets.QMainWindow, Ui_confirmRemove):
    def __init__(self, parent=None, ll=None,id=""):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.ll=ll
        self.id=id

        self.pushButton.clicked.connect(self.aceptar)
        self.pushButton_3.clicked.connect(self.abort)

        self.center()
    def abort(self):
        window=LookEditWindow(self)
        window.show()
        self.close()

    def aceptar(self):
        a=self.id
        self.ll.pop(int(a))

        current=self.ll.first
        count=0
        while(current):
            current.value.id=count
            current=current.next
            count+=1

        fm.writeInFile(fileName, self.ll)

        window=LookEditWindow(self)
        window.show()
        self.close()

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
#FIN de la ventana ver y editar




