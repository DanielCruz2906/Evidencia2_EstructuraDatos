import pandas as pd
import sys
import datetime
import csv
import os

diccionario= {}
contador=1
formato=("*"*40 + "\n")

try:
    while True:
        print("Que movimiento deseas hacer")
        menu=int(input("1:Registrar una venta\n2:Consultar ventas de un dia en especifico\n3:Salir\n"))
        lista_mult=[]
        
        if menu == 1:
            ciclo=1
            while ciclo == 1:
                                
                lista_descripcion=[]
                lista_cantidad=[]
                lista_precio=[]
                lista_tiempo=[]
            
                print(formato)
            
                v_descripcion= input(f"Descripcion del producto {contador}: ")
                lista_descripcion.append(v_descripcion)
                v_cantidad= int(input("Cuantas piezas se vendieron: "))
                lista_cantidad.append(v_cantidad)
                v_precio=float(input("Cual es el precio del producto: "))
                lista_precio.append(v_precio)
                lista_mult.append(v_cantidad * v_precio)
                   
                           
                ahora = datetime.datetime.now()
                ahora1=ahora.strftime('%d/%m/%Y')
                lista_tiempo.append(str(ahora1))
                            
                diccionario["Descripcion"]= lista_descripcion
                diccionario["Cantidad vendida"]= lista_cantidad
                diccionario["Precio"]= lista_precio
                diccionario["Tiempo"]= lista_tiempo
                diccionario1= pd.DataFrame(diccionario)
            
                direct="Seguimiento.cvs"
                diccionario1.to_csv(direct, index=None, mode="a", header=not os.path.isfile(direct))
                
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
        
                    
        if menu == 2:
            
            break
            
            
except:
    print(f"Ocurrió un problema {sys.exc_info()[0]}")

             
        