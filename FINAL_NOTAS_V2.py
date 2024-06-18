import csv

#Funcion para traer y leer el archivo CSV
def obtener_fichero_calificaciones():
    lista = []
    with open(r"C:\Users\bruno\Downloads\calificaciones.csv", "r", newline="") as archivo:
        lector_csv = csv.reader(archivo, delimiter=";")
        pos = 0
        for linea in lector_csv:
            if pos != 0:
                for i in range(2, len(linea)): #Se parte desde la linea dos para que lo recorra con un for
                    if linea[i] == '': #Reemplazo de las casillas vacias por 0.0
                        linea[i] = '0.0' 
                Apellidos = linea[0]
                nombre = linea[1]
                Asistencia = float(linea[2].replace('%', '')) #Se quita % para que el numero lo pueda convertir en float
                Parcial1 = float(linea[3].replace(',', '.')) #Se reemplaza , por . para que pueda pasar ser un float
                Parcial2 = float(linea[4].replace(',', '.'))
                Ordinario1 = float(linea[5].replace(',', '.'))
                Ordinario2 = float(linea[6].replace(',', '.'))
                Practicas = float(linea[7].replace(',', '.'))
                OrdinarioPracticas = float(linea[8].replace(',', '.'))
                alumno = {
                    'Apellidos': Apellidos,
                    'nombre': nombre,
                    'Asistencia': Asistencia,
                    'Parcial1': Parcial1,
                    'Parcial2': Parcial2,
                    'Ordinario1': Ordinario1,
                    'Ordinario2': Ordinario2,
                    'Practicas': Practicas,
                    'OrdinarioPracticas': OrdinarioPracticas,
                }
                lista.append(alumno) 
                print("Calificaciones de", nombre, Apellidos)
                print("Asistencia:", Asistencia)
                print("Parcial 1:", Parcial1)
                print("Parcial 2:", Parcial2)
                print("Ordinario 1:", Ordinario1)
                print("Ordinario 2:", Ordinario2)
                print("Prácticas:", Practicas)
                print("Ordinario Prácticas:", OrdinarioPracticas)
                print()
            else:
                pos = 1
    return lista

#Funcion para añadir las notas de X alumno
def añadir_nota_final(alumno):
    if alumno['Ordinario1']:
        parcial1 = alumno['Ordinario1']
    elif alumno['Parcial1']:
        parcial1 = alumno['Parcial1']
    else:
        parcial1 = 0
        
    if alumno['Ordinario2']:
        parcial2 = alumno['Ordinario2']
    elif alumno['Parcial2']:
        parcial2 = alumno['Parcial2']
    else:
        parcial2 = 0
        
    if alumno['OrdinarioPracticas']:
        practicas = alumno['OrdinarioPracticas']
    elif alumno['Practicas']:
        practicas = alumno['Practicas']
    else:
        practicas = 0
        
    #Calculo final de notas parciales y nota final    
    alumno['Final1'] = parcial1
    alumno['Final2'] = parcial2
    alumno['FinalPracticas'] = practicas
    alumno['NotaFinal'] = parcial1 * 0.3 + parcial2 * 0.3 + practicas * 0.4
    return alumno

calificaciones = obtener_fichero_calificaciones()
for alumno in calificaciones:
    añadir_nota_final(alumno)