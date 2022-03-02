import math
import os
from numpy import fix
import psycopg2

try:
    conexion = psycopg2.connect(
        host = 'localhost',
        port = '5432',
        user = 'postgres',
        password = 'Paco0109',
        dbname = 'Edad'
    )
    print ('Se logro establecer conexion')
except psycopg2.Error as e:
    print ('no se logro establecer la conexion')
    print('Verifique los parametros')

cursor = conexion.cursor()

while True:
    print('''

    Seleccione que desea hacer

    1. ingresar datos
    2. ver Historial
    3. salir
    ''')
    seleccion = input('Seleccione lo que quiera realizar: ')
    try:
        seleccion = int(seleccion)
    except ValueError:
        print('Ingrese un dato valido')
        os.system('pause')
    if seleccion == 1:
        while True: 
            n = input('Ingrese un numero entre 0 y 999: ')
            try:
                
                n = int(n)
                c=fix(n/100)
                d=fix((n - c*100)/10)
                u=fix(n - c*100 - d*10)
                cursor.execute("insert into udc (numero, centenas, decenas, unidades) VALUES (%s,%s,%s,%s);",(n,c,d,u))
                c = str(c)
                d = str(d)
                u = str(u)
                print('Centenas del numero:  '+c)
                print('Decenas del numero:  '+d)
                print('Unidades del numero:  '+u)
                conexion.commit()
                os.system('pause')
                break
            except ValueError:
                print('dato incorrecto')
                print('Vuelva a ingresar los numeros')
                os.system('pause')
    elif seleccion == 2:
        cursor = conexion.cursor()
        SQL = 'select*from udc;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        os.system('pause')
    elif seleccion == 3:
        cursor.close()
        conexion.close()
        break