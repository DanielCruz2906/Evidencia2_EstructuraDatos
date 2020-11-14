# Evidencia2_EstructuraDatos
Evidencia 2 de Estructura de datos y su procesamiento

Objetivos del proyecto:
El objetivo de este proyecto es el de poder crear un programa que pueda llevar el control y registro de detalles de ventas.
En este caso, se llevará el registro de ventas de un negocio de bisutería.
Bisutería se refiere a la industria que produce objetos materiales de adorno que no están hechos de materiales preciosos.

Requerimientos funcionales por cumplir:
Se ofrecerá un menú navegable con las siguientes opciones:
•	Registrar una venta
•	Consultar ventas de un día específico
•	Salir
Para el caso de registrar una venta se considera que en una sola venta pueden venderse uno o más artículos y, para cada uno de ellos, se captura el detalle consistente en:
•	Descripción del artículo
•	Cantidad de piezas vendidas
•	Precio de venta
Al final del registro de cada venta, se informa el monto total a pagar por parte del cliente.
Al final del registro de cada venta, se almacena su detalle, incluyendo la fecha actual del sistema.
Para consultar las ventas de un día específico, se le solicita al usuario la fecha que desea consultar; si existen ventas de la fecha indicada se le muestra al usuario, de lo contrario se le informa que no se registraron ventas para dicha fecha.

Manual de Usuario:
1. Primeros pasos. 

Al iniciar el programa se desplegará el siguiente menú.
Figura 1.1

![Figura 1.1](https://github.com/DanielCruz2906/Evidencia2_EstructuraDatos/blob/main/Capturas/Figura1.1.jpg) 

En esta sección el usuario deberá seleccionar la opción que desee activar.
El usuario deberá introducir el número 1, para registrar una venta; 2, para consultar las ventas realizadas en un día específico; 3, para finalizar el programa.

2. Registrar una venta.
En este caso procederemos insertar el número 1 (registrar una venta) y presionaremos ENTER.
Figura 2.1
![Figura 2.1](https://github.com/DanielCruz2906/Evidencia2_EstructuraDatos/blob/main/Capturas/Figura2.1.jpg) 
Lo siguiente que se desplegará será un submenú al usuario que deberá contestar.
 
Figura 2.2

![Figura 2.2](https://github.com/DanielCruz2906/Evidencia2_EstructuraDatos/blob/main/Capturas/Figura2.2.jpg) 

Deberá introducir la descripción del producto y presionar ENTER.
Así sucederá de igual manera con las siguientes preguntas como se muestra a continuación.
Figura 2.3

![Figura 2.3](https://github.com/DanielCruz2906/Evidencia2_EstructuraDatos/blob/main/Capturas/Figura2.3.jpg) 

Al aplicar ENTER en esta última opción, automáticamente se hará una serie de procesos para exportar la información en un archivo CSV en la ubicación actual donde se encuentre el programa:
Figura 2.4

![Figura 2.4](https://github.com/DanielCruz2906/Evidencia2_EstructuraDatos/blob/main/Capturas/Figura2.4.jpg) 

El dato se guardará al final del documento cada vez que se registre una venta nueva.
Figura 2.5

![Figura 2.5](https://github.com/DanielCruz2906/Evidencia2_EstructuraDatos/blob/main/Capturas/Figura2.5.jpg) 

Al guardar la información de la venta saldrá el siguiente submenú:
Figura 2.6

![Figura 2.6](https://github.com/DanielCruz2906/Evidencia2_EstructuraDatos/blob/main/Capturas/Figura2.6.jpg)  

Donde si insertas el número 1, volverá a la figura 2.2 y repetirá todos los pasos.
Si se inserta el número 0, saldrá del registrador de ventas y desplegará un mensaje con el monto total de la venta y desplegará el menú principal como se muestra en la siguiente captura:
Figura 2.7

![Figura 2.7](https://github.com/DanielCruz2906/Evidencia2_EstructuraDatos/blob/main/Capturas/Figura2.7.jpg) 

3. Consultar Ventas de un día específico.
Lo primero que se hará es introducir el número 2 y presionar ENTER como se muestra a continuación:
Figura 3.1

![Figura 3.1](https://github.com/DanielCruz2906/Evidencia2_EstructuraDatos/blob/main/Capturas/Figura3.1.jpg) 

Al presionar ENTER se despliega un submenú como el que se muestra a continuación:
Figura 3.2

![Figura 3.2](https://github.com/DanielCruz2906/Evidencia2_EstructuraDatos/blob/main/Capturas/Figura3.2.jpg) 

Este submenú pregunta cuál es la fecha para consultar.
Para poder consultar una fecha, deberás insertar la fecha deseada con el siguiente formato:
dd/mm/yyyy donde:
•	dd es el día en número 
•	mm es el mes en número
•	yyyy es el año de manera completa en número
Ejemplo:
14/11/2020 (14 de noviembre de 2020)
Al insertar la fecha se deberá insertar ENTER y se mostrará el siguiente resultado:


Figura 3.3

![Figura 3.3](https://github.com/DanielCruz2906/Evidencia2_EstructuraDatos/blob/main/Capturas/Figura3.3.jpg) 

Al finalizar, volverá a mostrar el menú principal.
Cabe aclarar que en el caso de no tener ventas en una fecha específica que desea consultar el usuario, se desplegará el siguiente mensaje:
Figura 3.4
 
4. Salir
Para culminar el proceso, el usuario deberá introducir el número 3 y enseguida presionar ENTER. De esta manera se terminaría el proceso como se muestra a continuación:
Figura 4.1

![Figura 4.1](https://github.com/DanielCruz2906/Evidencia2_EstructuraDatos/blob/main/Capturas/Figura4.1.jpg) 
