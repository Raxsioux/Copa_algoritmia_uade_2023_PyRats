from random import randint
 
# Cargar Regiones Geograficas
def carga_regiones(regiones, codigo):
    print('Ingresar regiones geograficas **Finalizar carga con FIN**')

    regiones_geograficas = []

    # Carga nombre y codigo
    while True:
        contador_region_geografica = len(regiones)+1
        
        # Ingreso de regiones geograficas
        region = input(
            f'Ingresar la region geografica {contador_region_geografica} : ').strip()
        while region == '' or region in regiones:
            region = input(
                f'La region geografica ya ha sido ingresada o no es valida, por favor re-ingresar region {contador_region_geografica}: ').strip()

        #Ingreso de FIN
        if region == 'FIN':
            if len(regiones) > 0:
                break
            else:
                print('Se debe ingresar al menos una region geografica')
                region = input(
                    f'Ingresar la region {contador_region_geografica}: ').strip()
                while region == '' or region in regiones or region == 'FIN':
                    region = input(
                        f'Error! Re-Ingrese la region {contador_region_geografica}: ').strip()

        # Agregar nombre
        regiones.append(region)

        # Generar codigo para cada region
        if (len(region)) >= 3:
            abr = region[:2]
        else:
            abr = region[0]
        nro = randint(100, 999)
        cod = (str(contador_region_geografica)+abr+str(nro))
        codigo.append(cod)

        # Agregar region y codigo
        dic_regiones = {
            'nombre': region,
            'codigo': cod,
        }

        regiones_geograficas.append(dic_regiones)

    # Archivo regiones geograficas
    with open('regiones.csv', 'w') as archivo:
        archivo.write('nombre;codigo\n')
        for i in range(len(regiones_geograficas)):
            archivo.write(f'{regiones_geograficas[i]["nombre"]};{regiones_geograficas[i]["codigo"]}\n')


    return regiones, codigo

# Carga partidos políticos
def carga_partidos(nombre_rep, abrev_rep, lista_rep):
    print("Ingresar partidos políticos **Finalizar carga con FIN**")

    partidos = []

    while True:
        # Ingreso del partido
        nombre = input('Ingresar el nombre del partido político: ').strip()
        while nombre == '' or nombre in nombre_rep:
            nombre = input(
                'El nombre del partido político no es valido, por favor re-ingresar nombre: ').strip()

        #Ingreso de FIN
        if nombre == 'FIN':
            if len(partidos) > 0:
                break
            else:
                print('Se debe ingresar al menos un partido')
                nombre = input('Ingresar el nombre del partido político: ').strip()
                while nombre == '' or nombre in nombre_rep or nombre == 'FIN':
                    nombre = input(
                        'Error! Reingrese el nombre del partido politico: ').strip()

        # Agregar nombre
        nombre_rep.append(nombre)

        # Ingreso de abreviatura
        abrev = input('Ingresar la abreviatura del partido: ').strip()
        while abrev.isalnum() == False or abrev in abrev_rep:
            abrev = input(
                'La abreviatura no es valida, por favor re-ingresar abreviatura').strip()

        # Agregar abreviatura
        abrev_rep.append(abrev)

        # Ingreso lista
        try:
            lista = int(input("Ingrese la lista del partido: "))
        except:
            lista = ''

        while str(lista) == '' or lista == 0 or lista in lista_rep:
            try:
                lista = int(
                    input('El numero de lista no es valido, por favor re-ingresar la lista: '))
            except:
                lista = ''

        # Agregar lista
        lista_rep.append(lista)

        # Cargos politicos
        dicPartidos = {
            'nombre': nombre,
            'abreviatura': abrev,
            'lista': lista,
            'cargos': {
                'presidencia': 1,
                'diputado': 2,
                'senador': 3,
                'gobernadores':4
        }}

        # Agregar partido
        partidos.append(dicPartidos)

    # Carga de archivo
    with open('partidos.csv', 'w') as archivo:
        archivo.write('nombre;abreviatura;lista\n')
        for i in range(len(partidos)):
            archivo.write(f'{partidos[i]["nombre"]};{partidos[i]["abreviatura"]};{partidos[i]["lista"]}\n')

    return nombre_rep, abrev_rep, lista_rep


regiones = []
codigo = []
carga_regiones(regiones, codigo)

partido_nombre = []
partido_abreviatura = []
partido_lista = []
carga_partidos(partido_nombre, partido_abreviatura, partido_lista)


# Printeo de pantalla
ion = "-"
print(ion*90)
print('REGIONES GEOGRAFICAS'.center(90, ' '))
print(ion*90)
print('NOMBRE'.center(45, ' '), 'CODIGO O ABREVIATURA'.center(45, ' '))
print(ion*90)
for i in range(len(regiones)):
    print((str(regiones[i]).title()).center(45, ' '),
          (str(codigo[i])).center(45, ' '))
    print(ion*90)

print(' ')

print(ion*90)
print('PARTIDOS POLITICOS'.center(90, ' '))
print(ion*90)
print('NOMBRE'.center(30, ' '), 'ABREVIATURA'.center(
    30, ' '), 'LISTA'.center(30, ' '))
print(ion*90)
for i in range(len(partido_nombre)):
    print((str(partido_nombre[i]).title()).center(30, ' '),
            (str(partido_abreviatura[i]).upper()).center(30, ' '),
            (str(partido_lista[i])).center(30, ' '))
    print(ion*90)
