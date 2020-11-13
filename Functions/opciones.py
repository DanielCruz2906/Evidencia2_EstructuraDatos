import pandas as pd
import sys
import datetime
import csv
import os

class Venta:

    def __init__(self,descripcion="",cantidad="",precio=""):
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def venta_producto(self):

        lista_descripcion=[]
        lista_cantidad=[]
        lista_precio=[]
        lista_tiempo=[]
        diccionario= {}

        lista_descripcion.append(self.descripcion)
        lista_cantidad.append(self.cantidad)
        lista_precio.append(self.precio)
        lista_mult = self.precio * self.cantidad

        ahora = datetime.datetime.now()
        ahora1=ahora.strftime('%d/%m/%Y')
        lista_tiempo.append(str(ahora1))
    
        diccionario["Fecha"]= lista_tiempo
        diccionario["Descripcion"]= lista_descripcion
        diccionario["Cantidad vendida"]= lista_cantidad
        diccionario["Precio"]= lista_precio
        diccionario1= pd.DataFrame(diccionario)

        return diccionario1

def to_csv(nombre,dataframe):
    direct = nombre
    dataframe.to_csv(direct, index=None, mode="a", header=not os.path.isfile(direct))
        