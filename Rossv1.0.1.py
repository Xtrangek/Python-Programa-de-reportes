from asyncio.windows_events import NULL
from calendar import c
from distutils.log import error
from platform import system
import re
from sqlite3 import enable_shared_cache
from tkinter import E
from turtle import clear
import mysql.connector
from datetime import datetime
import os
from fpdf import FPDF

breaker = False

conexion1 = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "Fran123."
)

cursor1 = conexion1.cursor()
cursor1.execute("CREATE DATABASE IF NOT EXISTS REPORTES")
cursor1.execute("use REPORTES")
cursor1.execute("CREATE TABLE IF NOT EXISTS TIPO_VIAJE(ID_TipoViaje INT NOT NULL AUTO_INCREMENT, tipo_viaje VARCHAR(15) NOT NULL, PRIMARY KEY (ID_TipoViaje));")
cursor1.execute("INSERT INTO tipo_viaje(tipo_viaje) SELECT 'FORANEO' FROM dual WHERE NOT EXISTS (SELECT * FROM TIPO_VIAJE WHERE TIPO_VIAJE = 'FORANEO');")
cursor1.execute("INSERT INTO tipo_viaje(tipo_viaje) SELECT 'LOCAL' FROM dual WHERE NOT EXISTS (SELECT * FROM TIPO_VIAJE WHERE TIPO_VIAJE = 'LOCAL');")
cursor1.execute("INSERT INTO tipo_viaje(tipo_viaje) SELECT 'MIXTO' FROM dual WHERE NOT EXISTS (SELECT * FROM TIPO_VIAJE WHERE TIPO_VIAJE = 'MIXTO');")
cursor1.execute("CREATE TABLE IF NOT EXISTS COORDINADORES(ID_Coor INT NOT NULL AUTO_INCREMENT, nombre VARCHAR(100) NOT NULL, Viajes_fac INT(3) NOT NULL, cajas_asignadas INT(10), PRIMARY KEY (ID_Coor));")
cursor1.execute("CREATE TABLE IF NOT EXISTS OPERADORES(ID_Op INT NOT NULL AUTO_INCREMENT, nombre VARCHAR(100) NOT NULL, num_tractor INT(10), Tviajes INT(3) NOT NULL, Viajes_real INT(3) NOT NULL, Coordinador_Asig INT(10) NOT NULL, PRIMARY KEY (ID_Op), FOREIGN KEY(Tviajes) REFERENCES TIPO_VIAJE(ID_TipoViaje), FOREIGN KEY(Coordinador_Asig) REFERENCES COORDINADORES(ID_Coor) ON DELETE CASCADE);")

while True:
    os.system("cls")
    print ("\n\nSeleccione la opcion con el numero correspondiente, seguido de un ENTER:\n\n1.-Actualizar/visualizar datos.\n2.-Realizar reporte.\n3.-Salir del programa.")

    opcion2 = input ("")

    if opcion2 == "1":
        os.system("cls")
        while True:
            os.system("cls")

            print("\n\nSeleccione la opcion con el numero correspondiente, seguido de un ENTER:\n\n1.-Actualizar Coordinadores.\n2.-Actualizar Operadores.\n3.-Regresar al menu anterior.")

            opcion3 = input("")
            #coordinadores
            if opcion3 == "1":
                os.system("cls")
                while True:
                    #Visualizar tablas de Coordinador y operadores a cargo. 
                    sqlCoor = "SELECT * FROM COORDINADORES "
        
                    cursor1 = conexion1.cursor()
                    cursor1.execute(sqlCoor)

                    Coordinadores = cursor1.fetchall()
        
                    for row in Coordinadores:
                        print("ID = ", row[0], )
                        print("Nombre = ", row[1], )
                        print("Viajes por facturar = ", row[2], )
                        print("Cajas Asignadas = ", row[3], "\n")
                        
                        
                    os.system("pause")
                    os.system("cls")
                
                    print ("\nPara agregar/eliminar/editar operadores a cargo, regresa al menu anterior en la opcion '2.-Editar Operadores'")
                    print ("\n\nSeleccione la opcion con el numero correspondiente, seguido de un ENTER:\n\n1.-Editar Coordinador.\n2.-Eliminar Coordinador.\n3.-Agregar Coordinador.\n4.-Regresar al menu anterior.\n5.-Salir del programa.")
                    
                    opcion4 = input ("")
                    #Editar
                    if opcion4 == "1":
                        while True:
                            os.system("cls")
                            #Visualizar tablas de Coordinador. 
                            sqlCoor = "SELECT * FROM COORDINADORES "
        
                            cursor1 = conexion1.cursor()
                            cursor1.execute(sqlCoor)

                            Coordinadores = cursor1.fetchall()
                            for row in Coordinadores:
                                print("ID = ", row[0], )
                                print("Nombre = ", row[1], )
                                print("Viajes por facturar = ", row[2], )
                                print("Cajas Asignadas = ", row[3], "\n")
                        
                            ID_Coor = input("\nIngrese el ID del Coordinador que desea editar: ")
                             
                            sqlCoor = ("SELECT * FROM Coordinadores WHERE ID_Coor = %s")  
                            sqlerrorCoor = ("SELECT COUNT(*) FROM Coordinadores WHERE ID_Coor = %s")
                           
                            os.system("cls")
                            cursor1 = conexion1.cursor()

                            cursor1.execute(sqlerrorCoor,(ID_Coor,))
                                
                            if cursor1.fetchone()[0]:
                                    cursor1.execute(sqlCoor,(ID_Coor,))
                                    Coordinadores = cursor1.fetchall()
                                    for row in Coordinadores:
                                        print("ID = ", row[0], )
                                        print("Nombre = ", row[1], )
                                        print("Viajes por facturar = ", row[2], )
                                        print("Cajas Asignadas = ", row[3], "\n")
                                    print ("1.-Cambiar Nombre.\n2.-Cajas Asignadas.\n3.-Viajes Facturados.\n4.-Regresar al menu anterior.\n5.-Salir del programa.")
                                    opcion5 = input("")
                                    #Nombre
                                    if opcion5 == "1":
                                        os.system("cls")
                                        nombre_Coor = input("Ingrese el nuevo nombre: ")
                                        sqleditCoor = "UPDATE `reportes`.`coordinadores` SET `nombre` = %s WHERE `id_Coor` = %s"
                                        cursor1 = conexion1.cursor()
                                        cursor1.execute(sqleditCoor,(nombre_Coor,ID_Coor,))
                                        os.system("cls")
                                        cursor1 = conexion1.cursor()
                                        cursor1.execute(sqlCoor,(ID_Coor,))
                                        Coordinadores = cursor1.fetchall()
                                        for row in Coordinadores:
                                            print("ID = ", row[0], )
                                            print("Nombre = ", row[1], )
                                            print("Viajes por facturar = ", row[2], )
                                            print("Cajas Asignadas = ", row[3], "\n")
                                        os.system("pause")
                                        os.system("cls")
                                        while True:
                                            resp = input("¿Desea seguir editando? Responda con un si o no: ")
                                            if resp == "si":
                                                break
                                            elif resp == "no":
                                                os.system("cls")
                                                break
                                            else:
                                                print("Opcion incorrecta, escriba correctamente si o no")
                                                os.system("pause")
                                                os.system("cls")
                                        if breaker:
                                            break
                                        if resp == "no":
                                            break
                                    #Cajas asignadas
                                    elif  opcion5 == "2":
                                        os.system("cls")
                                        print("\nPor favor, ingrese un numero entero, si no tendrá problemas.")
                                        cajas_Coor = input("Ingrese el nuevo numero de cajas asignadas: ")
                                        sqleditCoor = "UPDATE `reportes`.`coordinadores` SET `cajas_asignadas` = %s WHERE `id_Coor` = %s"
                                        cursor1 = conexion1.cursor()
                                        cursor1.execute(sqleditCoor,(cajas_Coor,ID_Coor,))
                                        os.system("cls")
                                        cursor1 = conexion1.cursor()
                                        cursor1.execute(sqlCoor,(ID_Coor,))
                                        Coordinadores = cursor1.fetchall()
                                        for row in Coordinadores:
                                            print("ID = ", row[0], )
                                            print("Nombre = ", row[1], )
                                            print("Viajes facturar = ", row[2], )
                                            print("Cajas Asignadas = ", row[3], "\n")
                                        os.system("pause")
                                        os.system("cls")
                                        while True:
                                            resp = input("¿Desea seguir editando? Responda con un si o no: ")
                                            if resp == "si":
                                                break
                                            elif resp == "no":
                                                os.system("cls")
                                                break
                                            else:
                                                print("Opcion incorrecta, escriba correctamente si o no")
                                                os.system("pause")
                                                os.system("cls")
                                        if breaker:
                                            break
                                        if resp == "no":
                                            break
                                    #Viajes facturados
                                    elif opcion5 == "3":
                                        os.system("cls")
                                        print("\nPor favor, ingrese un numero entero, si no tendrá problemas.")
                                        vfac_Coor = input("Ingrese el nuevo numero de viajes por facturar: ")
                                        sqleditCoor = "UPDATE `reportes`.`coordinadores` SET `viajes_fac` = %s WHERE `id_Coor` = %s"
                                        cursor1 = conexion1.cursor()
                                        cursor1.execute(sqleditCoor,(vfac_Coor,ID_Coor,))
                                        os.system("cls")
                                        cursor1 = conexion1.cursor()
                                        cursor1.execute(sqlCoor,(ID_Coor,))
                                        Coordinadores = cursor1.fetchall()
                                        for row in Coordinadores:
                                            print("ID = ", row[0], )
                                            print("Nombre = ", row[1], )
                                            print("Viajes por facturar = ", row[2], )
                                            print("Cajas Asignadas = ", row[3], "\n")
                                        os.system("pause")
                                        os.system("cls")
                                        while True:
                                            resp = input("¿Desea seguir editando? Responda con un si o no: ")
                                            if resp == "si":
                                                break
                                            elif resp == "no":
                                                os.system("cls")
                                                break
                                            else:
                                                print("Opcion incorrecta, escriba correctamente si o no")
                                                os.system("pause")
                                                os.system("cls")
                                        if breaker:
                                            break
                                        if resp == "no":
                                            break
                                    elif opcion5 == "4":
                                        os.system("cls")
                                        break
                                    elif opcion5 == "5":
                                        conexion1.commit()
                                        conexion1.close()
                                        exit()
                                    else: 
                                        print("Opcion incorrecta")
                                        os.system("pause")
                                        os.system("cls")
                            else:
                                print("El identificador que ingreso no existe, favor de ingresar uno existente.")
                                break          
                        if breaker:
                            break    
                    #Eliminar
                    elif opcion4 == "2":
                        os.system("cls")
                        while True:
                            #Visualizar tablas de Coordinador.
                            sqlCoor = "SELECT * FROM COORDINADORES "
                            cursor1 = conexion1.cursor()
                            cursor1.execute(sqlCoor)

                            Coordinadores = cursor1.fetchall()
                            for row in Coordinadores:
                                print("ID = ", row[0], )
                                print("Nombre = ", row[1], )
                                print("Viajes por facturar = ", row[2], )
                                print("Cajas Asignadas = ", row[3], "\n")
                            
                            ID_Coor = input("\nIngrese el ID del Coordinador que desea eliminar: ") 
                            sqlCoor = ("SELECT * FROM Coordinadores WHERE ID_Coor = %s")  
                            sqlerrorCoor = ("SELECT COUNT(*) FROM Coordinadores WHERE ID_Coor = %s")

                            os.system("cls")
                            cursor1 = conexion1.cursor()

                            cursor1.execute(sqlerrorCoor,(ID_Coor,))

                            if cursor1.fetchone()[0]:
                                cursor1.execute(sqlCoor,(ID_Coor,))
                                Coordinadores = cursor1.fetchall()
                                for row in Coordinadores:
                                    print("ID = ", row[0], )
                                    print("Nombre = ", row[1], )
                                    print("Viajes por facturar = ", row[2], )
                                    print("Cajas Asignadas = ", row[3], "\n")
                                print ("¿Seguro que desea borrar este Operador?\n")
                                print ("Recuerda que si eliminas un Coordinador, los operadores asignados se eliminarian tambien (recomendable editar)")
                                print ("1.-Si.\n2.-No.")
                                opcion5 = input("")
                                if opcion5 == "1":
                                    os.system("cls")
                                    sqldeleteCoor = "DELETE FROM `reportes`.`coordinadores` WHERE ID_Coor = %s"
                                    cursor1 = conexion1.cursor()
                                    cursor1.execute(sqldeleteCoor,(ID_Coor,))
                                    os.system("cls")
                                    cursor1 = conexion1.cursor()
                                    sqlCoor = "SELECT * FROM COORDINADORES"
                                    cursor1.execute(sqlCoor)
                                    Coordinadores = cursor1.fetchall()
                                    for row in Coordinadores:
                                        print("ID = ", row[0], )
                                        print("Nombre = ", row[1], )
                                        print("Viajes por facturar = ", row[2], )
                                        print("Cajas Asignadas = ", row[3], "\n")
                                    os.system("pause")
                                    os.system("cls")
                                    while True:
                                        resp = input("¿Desea seguir eliminando? Responda con un si o no: ")
                                        if resp == "si":
                                            break
                                        elif resp == "no":
                                            os.system("cls")
                                            break
                                        else:
                                            print("Opcion incorrecta, escriba correctamente si o no")
                                            os.system("pause")
                                            os.system("cls")
                                    if breaker:
                                        break
                                    if resp == "no":
                                        break
                                elif opcion5 == "2":
                                        os.system("cls")
                                        break
                                else: 
                                    print("Opcion incorrecta")
                                    os.system("pause")
                                    os.system("cls")
                            else:
                                print("El identificador que ingreso no existe, favor de ingresar uno existente.")
                                break
                        if breaker:
                            break
                    #Agregar
                    elif opcion4 == "3":
                        os.system("cls")
                        while True:
                            #Visualizar tablas de Coordinador.
                            sqlCoor = "SELECT * FROM COORDINADORES "
                            cursor1 = conexion1.cursor()
                            cursor1.execute(sqlCoor)

                            Coordinadores = cursor1.fetchall()
                            for row in Coordinadores:
                                print("ID = ", row[0], )
                                print("Nombre = ", row[1], )
                                print("Viajes por facturar = ", row[2], )
                                print("Cajas Asignadas = ", row[3], "\n")
                            
                            sqlinsertCoor = "INSERT INTO COORDINADORES(nombre, viajes_fac, cajas_asignadas) values (%s,%s,%s)"
                            os.system("cls")
                            cursor1 = conexion1.cursor()

                            nombre = input("Ingresa el nombre y apellido del Coordinador: ")
                            os.system("cls")
                            print("Por favor, ingresa un valor numerico entero sino tendrás problemas.")
                            viajes_fac = int(input("Ingresa el numero de viajes facturados: "))
                            os.system("cls")
                            print("Por favor, ingresa un valor numerico entero sino tendrás problemas.")
                            cajas_asignadas = int(input("Ingresa el numero de cajas asignadas: "))
                            os.system("cls")

                            cursor1.execute(sqlinsertCoor,(nombre, viajes_fac, cajas_asignadas))
                            cursor1.execute(sqlCoor)

                            Coordinadores = cursor1.fetchall()
                            for row in Coordinadores:
                                print("ID = ", row[0], )
                                print("Nombre = ", row[1], )
                                print("Viajes por facturar = ", row[2], )
                                print("Cajas Asignadas = ", row[3], "\n")
                            while True:
                                resp = input("¿Desea seguir agregando? Responda con un si o no: ")
                                if resp == "si":
                                    break
                                elif resp == "no":
                                    os.system("cls")
                                    break
                                else:
                                    print("Opcion incorrecta, escriba correctamente si o no")
                                    os.system("pause")
                                    os.system("cls")
                            if breaker:
                                break
                            if resp == "no":
                                break
                        if breaker:
                            break
                        
                    elif opcion4 == "4":
                        break
                    elif opcion4 == "5":
                        conexion1.commit()
                        conexion1.close()
                        exit()
                    else:
                        print("Opcion incorrecta")
                        os.system("pause")
                        os.system("cls")
                if breaker:
                   break
            #operadores
            elif opcion3 == "2":
                os.system("cls")
                while True:
                    #Visualizar tabla Operadores.
                    sqlOpera = "SELECT `OPERADORES`.`ID_OP`,    `OPERADORES`.`NOMBRE`,    `OPERADORES`.`NUM_TRACTOR`, `TIPO_VIAJE`.`TIPO_VIAJE`,`OPERADORES`.`VIAJES_REAL`, `COORDINADORES`.`NOMBRE` FROM OPERADORES LEFT JOIN TIPO_VIAJE ON TVIAJES = ID_TIPOVIAJE LEFT JOIN COORDINADORES ON COORDINADOR_ASIG = ID_COOR;"

                    cursor1 = conexion1.cursor()
                    cursor1.execute(sqlOpera)

                    Operadores = cursor1.fetchall()

                    for row in Operadores:
                        print("ID = ", row[0], )
                        print("Nombre = ", row[1], )
                        print("Numero de tractor asignado = ", row[2], )
                        print("Tipo de viajes asignados = ", row[3], )
                        print("Viajes realizados = ", row[4], )
                        print("Coordinador asignado = ", row[5], "\n")

                    os.system("pause")
                    
                    print ("\n\nSeleccione la opcion con el numero correspondiente, seguido de un ENTER:\n\n1.-Editar Operador.\n2.-Eliminar Operador.\n3.-Agregar Operador.\n4.-Regresar al menu anterior.\n5.-Salir del programa.")
                    opcion4 = input ("")
                    #Editar
                    if opcion4 == "1":
                        os.system("cls")
                        while True:
                            #Visualizar tabla Operadores
                            sqlOpera = "SELECT `OPERADORES`.`ID_OP`,    `OPERADORES`.`NOMBRE`,    `OPERADORES`.`NUM_TRACTOR`,    `TIPO_VIAJE`.`TIPO_VIAJE`, `OPERADORES`.`VIAJES_REAL`, `COORDINADORES`.`NOMBRE` FROM OPERADORES LEFT JOIN TIPO_VIAJE ON TVIAJES = ID_TIPOVIAJE LEFT JOIN COORDINADORES ON COORDINADOR_ASIG = ID_COOR;"
                            
                            cursor1 = conexion1.cursor()
                            cursor1.execute(sqlOpera)

                            Operadores = cursor1.fetchall()
                            for row in Operadores:
                                print("ID = ", row[0], )
                                print("Nombre = ", row[1], )
                                print("Numero de tractor asignado = ", row[2], )
                                print("Tipo de viajes asignados = ", row[3], )
                                print("Viajes realizados = ", row[4], )
                                print("Coordinador asignado = ", row[5], "\n")

                            ID_Op = input("\nIngrese el ID del Operador que desea editar: ")
                             
                            sqlOpera = ("SELECT `OPERADORES`.`ID_OP`,    `OPERADORES`.`NOMBRE`,    `OPERADORES`.`NUM_TRACTOR`,   `TIPO_VIAJE`.`TIPO_VIAJE`,`OPERADORES`.`VIAJES_REAL`, `COORDINADORES`.`NOMBRE` FROM OPERADORES LEFT JOIN TIPO_VIAJE ON TVIAJES = ID_TIPOVIAJE LEFT JOIN COORDINADORES ON COORDINADOR_ASIG = ID_COOR WHERE ID_OP = %s;")  
                            sqlerrorOpera = ("SELECT COUNT(*) FROM OPERADORES WHERE ID_Op = %s")

                            os.system("cls")
                            cursor1 = conexion1.cursor()

                            cursor1.execute(sqlerrorOpera,(ID_Op,))

                            if cursor1.fetchone()[0]:
                                cursor1.execute(sqlOpera,(ID_Op,))
                                Operadores = cursor1.fetchall()
                                for row in Operadores:
                                    print("ID = ", row[0], )
                                    print("Nombre = ", row[1], )
                                    print("Numero de tractor asignado = ", row[2], )
                                    print("Tipo de viajes asignados = ", row[3], )
                                    print("Viajes realizados = ", row[4], )
                                    print("Coordinador asignado = ", row[5], "\n")
                                    print ("1.-Cambiar Nombre.\n2.-Cambiar numero de tractor.\n3.-Tipo de viajes asignados.\n4.-Cambiar viajes realizados.\n5.-Cambiar coordinador asignado.\n6.-Regresar al menu anterior.\n7.-Salir del programa.")
                                opcion5 = input("")
                                #Nombre
                                if opcion5 == "1":
                                    os.system("cls")
                                    nombre_Op = input("Ingrese el nuevo nombre: ")
                                    sqleditOp = "UPDATE `reportes`.`operadores` SET `nombre` = %s WHERE `id_Op` = %s"
                                    cursor1 = conexion1.cursor()
                                    cursor1.execute(sqleditOp,(nombre_Op,ID_Op,))
                                    os.system("cls")
                                    cursor1 = conexion1.cursor()
                                    cursor1.execute(sqlOpera,(ID_Op,))
                                    Operadores = cursor1.fetchall()
                                    for row in Operadores:
                                        print("ID = ", row[0], )
                                        print("Nombre = ", row[1], )
                                        print("Numero de tractor asignado = ", row[2], )
                                        print("Tipo de viajes asignados = ", row[3], )
                                        print("Viajes realizados = ", row[4], )
                                        print("Coordinador asignado = ", row[5], "\n")
                                    os.system("pause")
                                    os.system("cls")
                                    while True:
                                        resp = input("¿Desea seguir editando? Responda con un si o no: ")
                                        if resp == "si":
                                            break
                                        elif resp == "no":
                                            os.system("cls")
                                            break
                                        else:
                                            print("Opcion incorrecta, escriba correctamente si o no")
                                            os.system("pause")
                                            os.system("cls")
                                    if breaker:
                                        break
                                    if resp == "no":
                                        break
                                #Numero de tractor
                                elif opcion5 == "2":
                                    os.system("cls")
                                    print("\nPor favor, ingrese un numero entero, si no tendrá problemas.")
                                    numTrac_Op = input("Ingrese el nuevo numero de tractor: ")
                                    sqleditOp = "UPDATE `reportes`.`operadores` SET `num_tractor` = %s WHERE `id_Op` = %s"
                                    cursor1 = conexion1.cursor()
                                    cursor1.execute(sqleditOp,(numTrac_Op,ID_Op,))
                                    os.system("cls")
                                    cursor1 = conexion1.cursor()
                                    cursor1.execute(sqlOpera,(ID_Op,))
                                    Operadores = cursor1.fetchall()
                                    for row in Operadores:
                                        print("ID = ", row[0], )
                                        print("Nombre = ", row[1], )
                                        print("Numero de tractor asignado = ", row[2], )
                                        print("Tipo de viajes asignados = ", row[3], )
                                        print("Viajes realizados = ", row[4], )
                                        print("Coordinador asignado = ", row[5], "\n")
                                    os.system("pause")
                                    os.system("cls")
                                    while True:
                                        resp = input("¿Desea seguir editando? Responda con un si o no: ")
                                        if resp == "si":
                                            break
                                        elif resp == "no":
                                            os.system("cls")
                                            break
                                        else:
                                            print("Opcion incorrecta, escriba correctamente si o no")
                                            os.system("pause")
                                            os.system("cls")
                                    if breaker:
                                        break
                                    if resp == "no":
                                        break
                                #Tipo de viajes
                                elif opcion5 == "3":
                                    os.system("cls")
                                    sqleOpViajes = "SELECT * FROM TIPO_VIAJE"
                                    cursor1 = conexion1.cursor()
                                    cursor1.execute(sqleOpViajes)

                                    Tipoviajes = cursor1.fetchall()
                                    for row in Tipoviajes:
                                        print("ID = ", row[0], )
                                        print("TIPO DE VIAJE = ", row[1], "\n")
                                    
                                    
                                    tipoviaje_Op = input("Ingrese el numero ID del tipo de viaje que desea registrar para el operador: ")
                                    sqleditOp = "UPDATE `reportes`.`operadores` SET `Tviajes` = %s WHERE `id_Op` = %s"
                                    sqlerrorOperaViaje = "SELECT COUNT(*) FROM TIPO_VIAJE WHERE ID_TIPOVIAJE = %s"

                                    os.system("cls")
                                    cursor1 = conexion1.cursor()
                                    cursor1.execute(sqlerrorOperaViaje,(tipoviaje_Op,))

                                    if cursor1.fetchone()[0]:

                                        cursor1 = conexion1.cursor()
                                        cursor1.execute(sqleditOp,(tipoviaje_Op,ID_Op,))
                                        os.system("cls")
                                        cursor1 = conexion1.cursor()
                                        cursor1.execute(sqlOpera,(ID_Op,))
                                        Operadores = cursor1.fetchall()
                                        for row in Operadores:
                                            print("ID = ", row[0], )
                                            print("Nombre = ", row[1], )
                                            print("Numero de tractor asignado = ", row[2], )
                                            print("Tipo de viajes asignados = ", row[3], )
                                            print("Viajes realizados = ", row[4], )
                                            print("Coordinador asignado = ", row[5], "\n")
                                        os.system("pause")
                                        os.system("cls")
                                        while True:
                                            resp = input("¿Desea seguir editando? Responda con un si o no: ")
                                            if resp == "si":
                                                break
                                            elif resp == "no":
                                                os.system("cls")
                                                break
                                            else:
                                                print("Opcion incorrecta, escriba correctamente si o no")
                                                os.system("pause")
                                                os.system("cls")
                                        if breaker:
                                            break
                                        if resp == "no":
                                            break
                                    else:
                                        print("El identificador que ingreso no existe, favor de ingresar uno existente.")
                                        break
                                #Viajes realizados
                                elif opcion5 == "4":
                                    os.system("cls")
                                    print("\nPor favor, ingrese un numero entero, si no tendrá problemas.")
                                    Viajesreal_Op = input("Ingrese el nuevo numero de viajes realizados: ")
                                    sqleditOp = "UPDATE `reportes`.`operadores` SET `viajes_real` = %s WHERE `id_Op` = %s"
                                    cursor1 = conexion1.cursor()
                                    cursor1.execute(sqleditOp,(Viajesreal_Op,ID_Op,))
                                    os.system("cls")
                                    cursor1 = conexion1.cursor()
                                    cursor1.execute(sqlOpera,(ID_Op,))
                                    Operadores = cursor1.fetchall()
                                    for row in Operadores:
                                        print("ID = ", row[0], )
                                        print("Nombre = ", row[1], )
                                        print("Numero de tractor asignado = ", row[2], )
                                        print("Tipo de viajes asignados = ", row[3], )
                                        print("Viajes realizados = ", row[4], )
                                        print("Coordinador asignado = ", row[5], "\n")
                                    os.system("pause")
                                    os.system("cls")
                                    while True:
                                        resp = input("¿Desea seguir editando? Responda con un si o no: ")
                                        if resp == "si":
                                            break
                                        elif resp == "no":
                                            os.system("cls")
                                            break
                                        else:
                                            print("Opcion incorrecta, escriba correctamente si o no")
                                            os.system("pause")
                                            os.system("cls")
                                    if breaker:
                                        break
                                    if resp == "no":
                                        break
                                #Coordinador asignado
                                elif opcion5 == "5":
                                    os.system("cls")
                                    sqlOpCoor = "SELECT * FROM COORDINADORES"
                                    cursor1 = conexion1.cursor()
                                    cursor1.execute(sqlOpCoor)

                                    OpCoor = cursor1.fetchall()
                                    for row in OpCoor:
                                        print("ID = ", row[0], )
                                        print("Nombre = ", row[1], )
                                        print("Viajes por facturar = ", row[2], )
                                        print("Cajas Asignadas = ", row[3], "\n")
                                                                        
                                    Coor_Op = input("Ingrese el numero ID del Coordinador que desea asignar: ")
                                    sqleditOp = "UPDATE `reportes`.`operadores` SET `Coordinador_Asig` = %s WHERE `id_Op` = %s"
                                    sqlerrorOperaCoor = "SELECT COUNT(*) FROM COORDINADORES WHERE ID_Coor = %s"

                                    os.system("cls")
                                    cursor1 = conexion1.cursor()
                                    cursor1.execute(sqlerrorOperaCoor,(Coor_Op,))

                                    if cursor1.fetchone()[0]:

                                        cursor1 = conexion1.cursor()
                                        cursor1.execute(sqleditOp,(Coor_Op,ID_Op,))
                                        os.system("cls")
                                        cursor1 = conexion1.cursor()
                                        cursor1.execute(sqlOpera,(ID_Op,))
                                        Operadores = cursor1.fetchall()
                                        for row in Operadores:
                                            print("ID = ", row[0], )
                                            print("Nombre = ", row[1], )
                                            print("Numero de tractor asignado = ", row[2], )
                                            print("Tipo de viajes asignados = ", row[3], )
                                            print("Viajes realizados = ", row[4], )
                                            print("Coordinador asignado = ", row[5], "\n")
                                        os.system("pause")
                                        os.system("cls")
                                        while True:
                                            resp = input("¿Desea seguir editando? Responda con un si o no: ")
                                            if resp == "si":
                                                break
                                            elif resp == "no":
                                                os.system("cls")
                                                break
                                            else:
                                                print("Opcion incorrecta, escriba correctamente si o no")
                                                os.system("pause")
                                                os.system("cls")
                                        if breaker:
                                            break
                                        if resp == "no":
                                            break
                                    else:
                                        print("El identificador que ingreso no existe, favor de ingresar uno existente.")
                                        break
                                elif opcion5 == "6":
                                    os.system("cls")
                                    break
                                elif opcion5 == "7":
                                    conexion1.commit()
                                    conexion1.close()
                                    exit()
                                else: 
                                    print("Opcion incorrecta")
                                    os.system("pause")
                                    os.system("cls")

                            else:
                                print("El identificador que ingreso no existe, favor de ingresar uno existente.")
                                break          
                        if breaker:
                            break    
                    #Eliminar
                    elif opcion4 == "2":
                        os.system("cls")
                        while True:
                            #Visualizar tabla Operadores
                            sqlOpera = "SELECT `OPERADORES`.`ID_OP`,    `OPERADORES`.`NOMBRE`,    `OPERADORES`.`NUM_TRACTOR`, `TIPO_VIAJE`.`TIPO_VIAJE`,`OPERADORES`.`VIAJES_REAL`, `COORDINADORES`.`NOMBRE` FROM OPERADORES LEFT JOIN TIPO_VIAJE ON TVIAJES = ID_TIPOVIAJE LEFT JOIN COORDINADORES ON COORDINADOR_ASIG = ID_COOR;"
                            
                            cursor1 = conexion1.cursor()
                            cursor1.execute(sqlOpera)

                            Operadores = cursor1.fetchall()
                            for row in Operadores:
                                print("ID = ", row[0], )
                                print("Nombre = ", row[1], )
                                print("Numero de tractor asignado = ", row[2], )
                                print("Tipo de viajes asignados = ", row[3], )
                                print("Viajes realizados = ", row[4], )
                                print("Coordinador asignado = ", row[5], "\n")

                            ID_Op = input("\nIngrese el ID del Operador que desea eliminar: ")
                             
                            sqlOpera = ("SELECT `OPERADORES`.`ID_OP`,    `OPERADORES`.`NOMBRE`,    `OPERADORES`.`NUM_TRACTOR`,   `TIPO_VIAJE`.`TIPO_VIAJE`,`OPERADORES`.`VIAJES_REAL`, `COORDINADORES`.`NOMBRE` FROM OPERADORES LEFT JOIN TIPO_VIAJE ON TVIAJES = ID_TIPOVIAJE LEFT JOIN COORDINADORES ON COORDINADOR_ASIG = ID_COOR WHERE ID_OP = %s;")  
                            sqlerrorOpera = ("SELECT COUNT(*) FROM OPERADORES WHERE ID_Op = %s")

                            os.system("cls")
                            cursor1 = conexion1.cursor()

                            cursor1.execute(sqlerrorOpera,(ID_Op,))

                            if cursor1.fetchone()[0]:
                                cursor1.execute(sqlOpera,(ID_Op,))
                                Operadores = cursor1.fetchall()
                                for row in Operadores:
                                    print("ID = ", row[0], )
                                    print("Nombre = ", row[1], )
                                    print("Numero de tractor asignado = ", row[2], )
                                    print("Tipo de viajes asignados = ", row[3], )
                                    print("Viajes realizados = ", row[4], )
                                    print("Coordinador asignado = ", row[5], "\n")
                                print ("¿Seguro que desea borrar este Operador?\n")
                                print ("1.-Si.\n2.-No.")
                                opcion5 = input("")
                                if opcion5 == "1":
                                    os.system("cls")
                                    sqldeleteCoor = "DELETE FROM `reportes`.`operadores` WHERE ID_Op = %s"
                                    cursor1 = conexion1.cursor()
                                    cursor1.execute(sqldeleteCoor,(ID_Op,))
                                    os.system("cls")
                                    cursor1 = conexion1.cursor()
                                    sqlOpera = ("SELECT `OPERADORES`.`ID_OP`,    `OPERADORES`.`NOMBRE`,    `OPERADORES`.`NUM_TRACTOR`, `TIPO_VIAJE`.`TIPO_VIAJE`,`OPERADORES`.`VIAJES_REAL`, `COORDINADORES`.`NOMBRE` FROM OPERADORES LEFT JOIN TIPO_VIAJE ON TVIAJES = ID_TIPOVIAJE LEFT JOIN COORDINADORES ON COORDINADOR_ASIG = ID_COOR;")  
                                    cursor1.execute(sqlOpera)
                                    Operadores = cursor1.fetchall()
                                    for row in Operadores:
                                        print("ID = ", row[0], )
                                        print("Nombre = ", row[1], )
                                        print("Numero de tractor asignado = ", row[2], )
                                        print("Tipo de viajes asignados = ", row[3], )
                                        print("Viajes realizados = ", row[4], )
                                        print("Coordinador asignado = ", row[5], "\n")
                                    os.system("pause")
                                    os.system("cls")
                                    while True:
                                        resp = input("¿Desea seguir eliminando? Responda con un si o no: ")
                                        if resp == "si":
                                            break
                                        elif resp == "no":
                                            os.system("cls")
                                            break
                                        else:
                                            print("Opcion incorrecta, escriba correctamente si o no")
                                            os.system("pause")
                                            os.system("cls")
                                    if breaker:
                                        break
                                    if resp == "no":
                                        break
                                elif opcion5 == "2":
                                        os.system("cls")
                                        break
                                else: 
                                    print("Opcion incorrecta")
                                    os.system("pause")
                                    os.system("cls")
                            else:
                                print("El identificador que ingreso no existe, favor de ingresar uno existente.")
                                break
                        if breaker:
                            break
                    #Agregar
                    elif opcion4 == "3":
                        os.system("cls")
                        while True:
                            #Visualizar tablas de Coordinador.
                            sqlOpera = "SELECT `OPERADORES`.`ID_OP`,    `OPERADORES`.`NOMBRE`,    `OPERADORES`.`NUM_TRACTOR`, `TIPO_VIAJE`.`TIPO_VIAJE`,`OPERADORES`.`VIAJES_REAL`, `COORDINADORES`.`NOMBRE` FROM OPERADORES LEFT JOIN TIPO_VIAJE ON TVIAJES = ID_TIPOVIAJE LEFT JOIN COORDINADORES ON COORDINADOR_ASIG = ID_COOR;"
                            
                            cursor1 = conexion1.cursor()
                            cursor1.execute(sqlOpera)

                            Operadores = cursor1.fetchall()
                            for row in Operadores:
                                print("ID = ", row[0], )
                                print("Nombre = ", row[1], )
                                print("Numero de tractor asignado = ", row[2], )
                                print("Tipo de viajes asignados = ", row[3], )
                                print("Viajes realizados = ", row[4], )
                                print("Coordinador asignado = ", row[5], "\n")
                            
                            sqlinsertOp = "INSERT INTO OPERADORES(nombre, num_tractor, tviajes, viajes_real, coordinador_asig) values (%s,%s,%s,%s,%s)"
                            os.system("cls")
                            cursor1 = conexion1.cursor()

                            nombreOp = input("Ingresa el nombre y apellido del Operador: ")
                            os.system("cls")
                            print("Por favor, ingresa un valor numerico entero sino tendrás problemas.")
                            numerotractOp = int(input("Ingresa el numero de tractor asignado: "))
                            os.system("cls")
                    
                            sqleOpViajes = "SELECT * FROM TIPO_VIAJE"
                            cursor1 = conexion1.cursor()
                            cursor1.execute(sqleOpViajes)

                            Tipoviajes = cursor1.fetchall()
                            for row in Tipoviajes:
                                print("ID = ", row[0], )
                                print("TIPO DE VIAJE = ", row[1], "\n")
                                    
                            print("Por favor, ingresa un valor numerico entero sino tendrás problemas.")
                            Tiviaje = int(input("Ingresa el numero ID del tipo de viaje: "))
                            os.system("cls")
                            print("Por favor, ingresa un valor numerico entero sino tendrás problemas.")
                            ViajesRealz = int(input("Ingresa el numero de viajes realizados: "))
                            os.system("cls")
                            sqlOpCoor = "SELECT * FROM COORDINADORES"
                            cursor1 = conexion1.cursor()
                            cursor1.execute(sqlOpCoor)

                            OpCoor = cursor1.fetchall()
                            for row in OpCoor:
                                print("ID = ", row[0], )
                                print("Nombre = ", row[1], )
                                print("Viajes por facturar = ", row[2], )
                                print("Cajas Asignadas = ", row[3], "\n")
                            print("Por favor, ingresa un valor numerico entero sino tendrás problemas.")
                            OperadorAsign = int(input("Ingresa el numero ID del coordinador a asignar: "))
                            os.system("cls")

                            cursor1.execute(sqlinsertOp,(nombreOp, numerotractOp, Tiviaje, ViajesRealz, OperadorAsign))
                            cursor1.execute(sqlOpera)

                            Operadores = cursor1.fetchall()
                            for row in Operadores:
                                print("ID = ", row[0], )
                                print("Nombre = ", row[1], )
                                print("Numero de tractor asignado = ", row[2], )
                                print("Tipo de viajes asignados = ", row[3], )
                                print("Viajes realizados = ", row[4], )
                                print("Coordinador asignado = ", row[5], "\n")
                            while True:
                                resp = input("¿Desea seguir agregar? Responda con un si o no: ")
                                if resp == "si":
                                    break
                                elif resp == "no":
                                    os.system("cls")
                                    break
                                else:
                                    print("Opcion incorrecta, escriba correctamente si o no")
                                    os.system("pause")
                                    os.system("cls")
                            if breaker:
                                break
                            if resp == "no":
                                break
                        if breaker:
                            break
                    elif opcion4 == "4":
                        break
                    elif opcion4 == "5":
                        conexion1.commit()
                        conexion1.close()
                        exit()
                    else:
                        print("Opcion incorrecta")
                        os.system("pause")
                        os.system("cls")
                if breaker:
                    break
                    
            elif opcion3 == "3":
                break
            else:
                print("Opcion incorrecta. Por favor intentelo de nuevo.")
                os.system("pause")
                os.system("cls")
        if breaker:
            break
    
    elif opcion2 == "2":
            #Realizar reporte a pdf
        while True:
            sqlPDF = "SELECT * FROM COORDINADORES "
            cursor1 = conexion1.cursor()
            cursor1.execute(sqlPDF)

            CoorPdf = cursor1.fetchall()

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size = 13)
            pdf.cell(200, 10, txt = "REPORTE DE COORDINADORES", ln = 1, align = 'C')
            for row in CoorPdf:
                ID_CR = row[0]
                ID_COR = row[0]
                pdf.cell(100, 5, txt = "NOMBRE: " + row[1], ln = 3, align = 'L')
                pdf.cell(100, 5, txt = "VIAJES POR FACTURAR: " + str(row[2]), ln = 3, align = 'L')
                pdf.cell(100, 5, txt = "CAJAS ASIGNADAS: " + str(row[3]), ln = 3, align = 'L')
                pdf.cell(100, 5, txt = "OPERADORES SIGNADOS: ", ln = 3, align = 'L')
                sqlOpAsing = "SELECT `operadores`.`nombre` FROM Coordinadores RIGHT JOIN operadores ON ID_Coor = Coordinador_Asig where ID_Coor = %s;"
                cursor1 = conexion1.cursor()
                cursor1.execute(sqlOpAsing,(ID_CR,))
                operadores_asignados = cursor1.fetchall()
                for a in operadores_asignados:
                    pdf.cell(100, 5, txt = "      " + (a[0]), ln = 3, align = 'L')
                pdf.cell(100, 10, txt = "", ln = 3, align = 'L')
                sqlSumaViajes = "SELECT SUM(VIAJES_REAL) FROM OPERADORES WHERE COORDINADOR_ASIG = %s"
                cursor1 = conexion1.cursor()
                cursor1.execute(sqlSumaViajes,(ID_CR,))
                viajestotales = cursor1.fetchall()
                for b in viajestotales:
                    pdf.cell(100, 5, txt = "TOTAL DE VIAJES REALIZADOS: " + str(b[0]), ln = 3, align = 'L')
                sqlViajesFacturados = "SELECT ( SELECT SUM(`VIAJES_REAL`) FROM `OPERADORES` WHERE COORDINADOR_ASIG = %s) - ( SELECT `VIAJES_FAC` FROM `COORDINADORES` WHERE ID_COOR = %s)"
                cursor1 = conexion1.cursor()
                cursor1.execute(sqlViajesFacturados,(ID_CR,ID_COR, ))
                viajesfacturados = cursor1.fetchall()
                for c in viajesfacturados:
                    pdf.cell(100, 5, txt = "VIAJES FACTURADOS: " + str(c[0]), ln = 3, align = 'L')
                pdf.cell(100, 5, txt = "----------------------------------------------------------------------------------------------------", ln = 3, align = 'L')
                pdf.cell(200, 10, txt = "", ln = 3, align = 'L')
            pdf.output("REPORTE.pdf")
            path = 'REPORTE.pdf'
            os.system(path)
            os.system("cls")
            print ("¿Deseas seguir realizando cambios o salir?\n")
            print ("1.-Continuar.\n2.-Salir.")
            opcion6 = input("")
            if opcion6 == "1":
                break
            if opcion6 == "2":
                conexion1.commit()
                conexion1.close()
                exit()
        if breaker:
            break
    elif opcion2 == "3":
        conexion1.commit()
        conexion1.close()
        exit()
    
    else:
        print("Opcion incorrecta")
        os.system("pause")
        os.system("cls")

                 




##########################################################################################################################################







