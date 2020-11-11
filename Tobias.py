import pandas as pd

diccionario= {}
lista_descripcion=[]
lista_cantidad=[]
lista_precio=[]
lista_mult=[]
contador=1
formato=("*"*40 + "\n")
while True:
    print("Que movimiento deseas hacer")
    menu=int(input("1:Registrar una venta\n2:Consultar ventas de un dia en especifico\n3:Salir\n"))
    if menu == 1:
        v_producto=int(input("Cuantas ventas va a registrar: "))
        print(formato)
        for ventas in range(v_producto):
            v_descripcion= input(f"Descripcion del producto {contador}: ")
            lista_descripcion.append(v_descripcion)
            v_cantidad= int(input("Cuantas piezas se vendieron: "))
            lista_cantidad.append(v_cantidad)
            v_precio=float(input("Cual es el precio del producto: "))
            lista_precio.append(v_precio)
            
            lista_mult.append(v_cantidad * v_precio)
            
            contador+=1
            
        
        diccionario["Descripcion"]= lista_descripcion
        diccionario["Cantidad vendida"]= lista_cantidad
        diccionario["Precio"]= lista_precio
        
        diccionario1= pd.DataFrame(diccionario)
        
        for nombre in range(1,v_producto+1):
            diccionario1.index=[lista_descripcion]
        
        print("PROCESO REALIZADO")
        
        sub_menu=int(input("Desea ver el monto total (1: Si, 2: No): "))
        if sub_menu == 1:
            
            a=sum(lista_mult)
            print(formato)
            print(f"El monto total es de {a} pesos")
            
        print(formato)
        
    if menu == 2:
        print(diccionario1)
        break
        
            
            
            
        
        
        