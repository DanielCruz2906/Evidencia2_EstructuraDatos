import pandas as pd
import sys
import datetime
import csv
import os
from Functions.opciones import Venta
from os import system,name
def limpiar():
    if name == "nt":
        system("cls")
    else:
        system("clear")

#diccionario= {}
contador=1
direct="Seguimiento.csv"
limpiar()
while True:
    try:
        print("┌──────────────────────────────────────────────┐")
        print("█         Que movimiento deseas hacer          █")
        print("█ [1]:Registrar una venta                      █\n█ [2]:Consultar ventas de un dia en especifico █\n█ [3]:Salir                                    █\n█                                              █")
        print("└──────────────────────────────────────────────┘")
        menu=input("Opcion:")
        lista_mult=[]
        
        if menu == "1":
            ciclo=1
            while ciclo == 1:
                
                ahora = datetime.datetime.now()
                ahora1=ahora.strftime('%d/%m/%Y')
                limpiar()
                print("┌────────────────────────────────────────────────────────────────┐")
                v_descripcion= input(f"█  Descripcion del producto {contador}: ")
                
                v_cantidad= int(input("█  Cuantas piezas se vendieron: "))
                
                v_precio=float(input("█  Cual es el precio del producto: "))
                print("└────────────────────────────────────────────────────────────────┘")
                lista_mult.append(v_cantidad * v_precio)
                
                diccionario1 = Venta(v_descripcion,v_cantidad,v_precio,ahora1).venta_producto()
            
                Venta(documento=direct,df=diccionario1).to_csv()
                
                contador+=1
                print("")
                print("┌──────────────────────────────────────────────────────────────────┐\n█                       ¿Que deseas hacer?\n█  [1]:Si deseas seguir registrando ventas\n█  [0]:Si deseas salir del registrador de ventas")
                print("└──────────────────────────────────────────────────────────────────┘")
                ciclo=int(input("Opcion:"))
                
                limpiar()
                
                print("")
        
            a=sum(lista_mult)
            print("┌──────────────────────────────────────────────┐\n█               PROCESO REALIZADO\n█")
            print(f"█  El monto total es de {a} pesos\n└──────────────────────────────────────────────┘")
            
        elif menu == "2":
            limpiar()
            op = input("               Formato:dd/mm/YYYY          \n┌──────────────────────────────────────────────┐\n█   ¿Cual es la fecha que quieres consultar?   █\n└──────────────────────────────────────────────┘\nOpcion:")
            print("")
            limpiar()
            i = Venta(fecha=op,documento=direct).producto_fecha()
            print(i)
            

        elif menu == "3":
            limpiar()
            print("┌──────────────────────────────────┐\n█  Culminación del Proceso Actual  █\n└──────────────────────────────────┘")
            break
            
        else:
            limpiar()
            print("┌──────────────────────────────────────────────┐")
            print(f"█  La opción {menu} no es válida")
            print("└──────────────────────────────────────────────┘")
    except:
        limpiar()
        print("┌──────────────────────────────────────────────┐")
        print(f"█  Ocurrió un problema {sys.exc_info()[0]}")
        print("└──────────────────────────────────────────────┘")