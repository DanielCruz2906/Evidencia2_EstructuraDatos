import pandas as pd
import sys
import datetime
import csv
import os
from Functions.opciones import Venta, to_csv

#diccionario= {}
contador=1
formato=("*"*40 + "\n")


while True:
    try:
        print("Que movimiento deseas hacer")
        menu=input("1:Registrar una venta\n2:Consultar ventas de un dia en especifico\n3:Salir\n")
        lista_mult=[]
        
        if menu == "1":
            ciclo=1
            while ciclo == 1:
                                
                print(formato)
            
                v_descripcion= input(f"Descripcion del producto {contador}: ")
                
                v_cantidad= int(input("Cuantas piezas se vendieron: "))
                
                v_precio=float(input("Cual es el precio del producto: "))
                
                lista_mult.append(v_cantidad * v_precio)
                
                diccionario1 = Venta(v_descripcion,v_cantidad,v_precio).venta_producto()
            
                direct="Seguimiento.csv"

                to_csv(direct,diccionario1)
                
                contador+=1

                print(formato)

                print("Ingresa el numero 1 si deseas seguir registrando ventas\nIngresa el numero 0 si deseas salir del registrador de ventas")
                
                ciclo=int(input(":"))
                
                print(formato)
                
                print("")
        
            a=sum(lista_mult)

            print(formato)

            print(f"El monto total es de {a} pesos")
            
            print(formato)
            
            print("PROCESO REALIZADO")
        
                    
        elif menu == "2":
            print("Fecha")
        
        elif menu == "3":
            print("Culminación del Proceso Actual")

        else:
            print(f"La opción {menu} no es válida")
                     
    except:
        print(f"Ocurrió un problema {sys.exc_info()[0]}")
