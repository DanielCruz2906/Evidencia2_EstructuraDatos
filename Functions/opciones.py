import pandas as pd
import sys
import datetime
import csv
import os

class Venta:

    def __init__(self,descripcion="",cantidad="",precio="",fecha="",documento="",df=""):
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
        self.fecha = fecha
        self.documento = documento
        self.df = df

    def venta_producto(self):

        lista_descripcion=[]
        lista_cantidad=[]
        lista_precio=[]
        lista_tiempo=[]
        diccionario= {}

        lista_descripcion.append(self.descripcion)
        lista_cantidad.append(self.cantidad)
        lista_precio.append(self.precio)


        lista_tiempo.append(self.fecha)
    
        diccionario["Fecha"]= lista_tiempo
        diccionario["Descripcion"]= lista_descripcion
        diccionario["Cantidad vendida"]= lista_cantidad
        diccionario["Precio"]= lista_precio
        diccionario1= pd.DataFrame(diccionario)

        return diccionario1

    def producto_fecha(self):
            df = pd.read_csv(f"{self.documento}")
            i = df.query(f"Fecha == '{self.fecha}'")
            if i.empty == True:
                return f"No hay movientos con la fecha proporcionada: {self.fecha} \n"
            else:
                return i

    def to_csv(self):
        direct = self.documento
        self.df.to_csv(direct, index=None, mode="a", header=not os.path.isfile(direct))
        