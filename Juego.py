import random
import psycopg2
import os

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

    1. Jugar
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

            A = random.randint(1,6)
            B = random.randint(1,6)
            C = A+B
            iniciar = int(input('Escriba su numero de la suerte para comenzar a jugar: '))
            try:

                if C == 8:
                    R = 'Has ganado'
                    print("Usted obtuvo " + str(A) + " En el primer dado")
                    print("Usted obtuvo " + str(B) + " En el segundo dado")
                    print("Usted obtuvo " + str(C) + " En total, Gano")
                elif C == 7:
                    R = 'Has perdido'
                    print("Usted obtuvo " + str(A) + " En el primer dado")
                    print("Usted obtuvo " + str(B) + " En el segundo dado")
                    print("Usted obtuvo " + str(C) + " En total, Perdio")
                else:
                    R = 'Vuelve a tirar'
                    print("Usted obtuvo " + str(A) + " En el primer dado")
                    print("Usted obtuvo " + str(B) + " En el segundo dado")
                    print("Usted obtuvo " + str(C) + " En total, Vuelva a tirar")
                cursor.execute("insert into juego (numero_obtenido, resultado) VALUES (%s,%s);",(C, R))
                conexion.commit()
                os.system('pause')
                break
            except ValueError:
                print('dato incorrecto')
                print('Vuelva a ingresar los numeros')
                os.system('pause')
    elif seleccion == 2:
        cursor = conexion.cursor()
        SQL = 'select*from juego;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        os.system('pause')
    elif seleccion == 3:
        cursor.close()
        conexion.close()
        break
