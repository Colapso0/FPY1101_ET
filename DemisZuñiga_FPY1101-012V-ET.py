import os
import random
import csv
import time
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos=[]
def sueldos_A():
    sueldo_random_1= random.randint(300000, 2500000)
    sueldo_random_2= random.randint(300000, 2500000)
    sueldo_random_3= random.randint(300000, 2500000)
    sueldo_random_4= random.randint(300000, 2500000)
    sueldo_random_5= random.randint(300000, 2500000)
    sueldo_random_6= random.randint(300000, 2500000)
    sueldo_random_7= random.randint(300000, 2500000)
    sueldo_random_8= random.randint(300000, 2500000)
    sueldo_random_9= random.randint(300000, 2500000)
    sueldo_random_10= random.randint(300000, 2500000)
    sueldos.append(sueldo_random_1)
    sueldos.append(sueldo_random_2)
    sueldos.append(sueldo_random_3)
    sueldos.append(sueldo_random_4)
    sueldos.append(sueldo_random_5)
    sueldos.append(sueldo_random_6)
    sueldos.append(sueldo_random_7)
    sueldos.append(sueldo_random_8)
    sueldos.append(sueldo_random_9)
    sueldos.append(sueldo_random_10)



def clasificar_sueldos():
    global sueldos
    global trabajadores
    menor=[]
    entre=[]
    mayor=[]
    if not sueldos:
        print("No hay sueldos generados")
        return
    else:
        for i in range(len(sueldos)):
          if sueldos[i] < 800000:
              menor.append(sueldos[i])
          if sueldos[i] >=800000 and sueldos[i] <=2000000:
              entre.append(sueldos[i])
          if sueldos[i] > 2000000:
              mayor.append(sueldos[i])
    print("Sueldos menores a $800.000  TOTAL: ", len(menor))
    print("Nombre empleado", "Sueldo", sep="\t")
    for i in range(len(menor)):
        print(f"{trabajadores[0]}" ,  f"${menor[i]}", sep="\t")
        del trabajadores[0]
    print("Sueldos entre $800.000 y $2.000.000  TOTAL: ", len(entre))
    print("Nombre empleado", "Sueldo", sep="\t")
    for i in range(len(entre)):
        print(f"{trabajadores[0]}" ,  f"${entre[i]}", sep="\t")
        del trabajadores[0]
    print("Sueldos superiores a $2.000.000  TOTAL: ", len(mayor))
    print("Nombre empleado", "Sueldo", sep="\t")
    for i in range(len(mayor)):
        print(f"{trabajadores[0]}" ,  f"${mayor[i]}", sep="\t")
        del trabajadores[0]
        os.system('clear')
    

#def Ver_estadisticas():
    #print("""
    #        1.Sueldo mas alto
    #        2.Sueldo mas bajo
    #        3.Promedio de sueldos
    #        4.Media geometrica
    # """)
    #try:
        #seleccion=int(input("Seleccione una opcion: "))
        #if seleccion ==1:
            #for mayor in sueldos:
                #


def salir():
    archivo="archivo.csv"
    with open(archivo,"w", newline="") as f:
        writer= csv.writer(f)
        writer.writerow(f"{trabajadores}")
        writer.writerow(f"{sueldos}")
    print("Finalizando programa....")
    time.sleep(2)
    print("Desarrollado por Demis Zuñiga")
    print("Rut: 21.311.925-7")
    

while(True):
    print("""
            1.Asignar sueldos aleatorios
            2.Clasificar Sueldos
            3.Ver estadisticas
            4.Reporte de sueldos
            5.Salir del programa
          """)
    try:
        opcion=int(input("Seleccione una opcion: "))
        if opcion==1:
            sueldos_A()
        elif opcion==2:
            clasificar_sueldos()
        elif opcion==5:
            salir()
            break
            
    except ValueError:
        print("Ingrese una opcion valida")