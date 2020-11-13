import pandas as pd
import sys
import datetime
import csv
import os
from Functions.opciones import Venta

#diccionario= {}
contador=1
formato=("uwu-"*25 + "\n")
direct="Seguimiento.csv"

while True:
    try:
        print("Que movimiento deseas hacer")
        menu=input("1:Registrar una venta\n2:Consultar ventas de un dia en especifico\n3:Salir\n")
        print("\n")
        lista_mult=[]
        
        if menu == "1":
            ciclo=1
            while ciclo == 1:
                                
                print(formato)
                
                ahora = datetime.datetime.now()
                ahora1=ahora.strftime('%d/%m/%Y')
                
                v_descripcion= input(f"Descripcion del producto {contador}: \n")
                
                v_cantidad= int(input("Cuantas piezas se vendieron: \n"))
                
                v_precio=float(input("Cual es el precio del producto: \n"))
                
                lista_mult.append(v_cantidad * v_precio)
                
                diccionario1 = Venta(v_descripcion,v_cantidad,v_precio,ahora1).venta_producto()
            
                Venta(documento=direct,df=diccionario1).to_csv()
                
                contador+=1

                print(formato)

                print("Ingresa el numero 1 si deseas seguir registrando ventas\n\nIngresa el numero 0 si deseas salir del registrador de ventas\n")
                
                ciclo=int(input(":"))
                
                print(formato)
                
                print("")
        
            a=sum(lista_mult)

            print(formato)

            print(f"\nEl monto total es de {a} pesos\n")
            
            print(formato)
            
            print("PROCESO REALIZADO\n")
        
        elif menu == "2":
            op = input("¿Cual es la fecha que quieres consultar?\n")
            i = Venta(fecha=op,documento=direct).producto_fecha()
            print("\n")
            print(i)
            print("\n")

        elif menu == "3":
            print("Culminación del Proceso Actual")
            break
            
        else:
            print(f"\nLa opción {menu} no es válida\n")

    except:
        print(f"Ocurrió un problema {sys.exc_info()[0]}\n")
