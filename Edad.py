from datetime import date
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

y = date.today().year
m = date.today().month 
d = date.today().day

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

            year = int(input('Escriba su año de nacimiento '))
            month = int(input('Escriba su mes de nacimiento '))
            day = int(input('Escriba su dia de nacimiento '))
            try:

                if day > d and month >= m:
                    dd = (d + 30) - day
                    mm = ((m-1) + 12) - month
                    yy = (y-1) - year
                    a = 'No ha cumplido años'
                    print(str(yy) + " Años "+ str(mm)+" Meses "+ str(dd)+ " Dias ")
                    print(a)
                elif day > d and month < m:
                    dd = (d + 30) - day
                    mm = m - month
                    yy = y - year
                    a = 'Ya cumplio años'
                    print(str(yy) + " Años "+ str(mm)+" Meses "+ str(dd)+ " Dias ")
                    print(a)
                elif day < d and month > m:
                    dd = d - day
                    mm = (m + 12) - month
                    yy = (y-1) - year
                    a = 'Ya cumplio años'
                    print(str(yy) + " Años "+ str(mm)+" Meses "+ str(dd)+ " Dias ")
                    print(a)
                else: 
                    dd = d - day
                    mm = m - month
                    yy = y - year
                    a = 'Ya cumplio años'
                    print(str(yy) + " Años "+ str(mm)+" Meses "+ str(dd)+ " Dias ")
                    print(a)

                cursor.execute("insert into datos (actual_año, cumpleaños) VALUES (%s,%s);",(yy, a))
                conexion.commit()
                os.system('pause')
                break
            except ValueError:
                print('dato incorrecto')
                print('Vuelva a ingresar los numeros')
                os.system('pause')
    elif seleccion == 2:
        cursor = conexion.cursor()
        SQL = 'select*from datos;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        os.system('pause')
    elif seleccion == 3:
        cursor.close()
        conexion.close()
        break
            



