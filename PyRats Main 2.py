import random

#obtencion de datos de regiones etapa 1
def leerRegiones():
    codigosRegiones = []
    with open("./regiones.csv") as archivo:
        datosRegiones = archivo.readlines()
        datosRegiones.pop(0)
        for datos in datosRegiones:
            codigo = datos.split(";")[1].replace("\n", "")
            codigosRegiones.append(codigo)
    return codigosRegiones

#obtencion de datos de partidos etapa 1
def leerPartidos():
    abrevPartidos = []
    with open("./partidos.csv") as archivo:
        datosPartidos = archivo.readlines()
        datosPartidos.pop(0)
        for datos in datosPartidos:
            codigo = datos.split(";")[1].replace("\n", "")
            abrevPartidos.append(codigo)
    return abrevPartidos


#creacion de documentos segun la cantidad de registros 
def registros():
    documentos = []
    for i in range(n):
        dni = random.randint(1, 100000000)
        while documentos.count(dni) >= 4: #(pueden llegar a repetirse documentos, pero nunca mas de 4 veces ya que no hay mas cargos)
            dni = random.randint(1, 100000000)
        documentos.append(dni)
    return documentos


# asignacion de documentos a regiones
def asignacion(documentos):   
    poblacion = []
    habitantes = list(set(documentos)) #usamos un set para eliminar documentos repetidos en cada una de las regiones
    for i in range(len(habitantes)):
        poblacion.append({"dni": habitantes[i], "region": random.choice(codigos)})

    for i in range(len(poblacion)):
        poblacion[i]["count"] = documentos.count(poblacion[i]["dni"]) #creamos un count para saber cuantas veces se registro el  documento en la region, lo cual sera la cantidad de votos que hizo
    return poblacion


def votos(poblacion,abreviaturas,cargos_politicos):
    votos = []
    sesgo = random.choice(abreviaturas) #creacion del sesgo hacia un partido aleatorio
    abreviaturas.append('blanco')       #posibilidad de voto en blanco para algun cargo
    for i in range(len(poblacion)):
        cargos=list(cargos_politicos.values())
        for j in range(poblacion[i]["count"]):
            cargo_elegido=random.choice(cargos)
            if i % 2 ==0 and j%2 == 0:          #sesgo
                votos.append(
                    {
                        "dni": poblacion[i]["dni"],
                        "region": poblacion[i]["region"],
                        "cargo": cargo_elegido,
                        "partido": sesgo,
                    }
                )          
            else:
                votos.append(
                    {
                        "dni": poblacion[i]["dni"],
                        "region": poblacion[i]["region"],
                        "cargo": cargo_elegido,
                        "partido": random.choice(abreviaturas)
                    }
                )
            cargos.remove(cargo_elegido) 
    return votos

#conteo de votos por region
def conteoRegion():
    sufragioFiltrados = [suf for suf in sufragio if suf['partido'] != 'blanco']
    votosRegion = []
    for cod in codigos:
        contadorVotosRegion = 0
        for voto in sufragioFiltrados:
            if voto['region'] == cod:
                contadorVotosRegion += 1
        votosRegion.append({'codigo':cod,
                            'votos': contadorVotosRegion,})
        
    #informe por pantalla con los totales de los votos procesados para cada region, sin contar los votos en blanco
    ion='-'
    print(ion*60)
    print('Votos totales'.center(60, ' '))
    print(ion*60)
    print('Region'.center(30, ' '), 'Cantidad'.center(30, ' '))
    print(ion*60)
    for i in range(len(votosRegion)):
        print((str(votosRegion[i]["codigo"])).center(30, ' '),
              (str(votosRegion[i]["votos"])).center(30, ' '))
        print(ion*60)




#cargos politicos
cargos_politicos={
    'presidencia': 1,
    'diputado': 2,            
    'senador': 3,
    'gobernadores':4
}

# lectura de archivos etapa 1
codigos = leerRegiones()
abreviaturas = leerPartidos()

# Ingreso registros con validacion de que sea numero natural mayor a 1
try:
    n = int(input("Ingresar cantidad de registros de votos: "))
except:
    n = -1

while n <1 or n>(len(cargos_politicos)*100000000): #al hacer n>len(cargos_politicos)*100000000, tomamos en cuenta q la cantidad de documentos validos que puede haber son de exactamente 100000000,
                                                    #si cada votante puede ejercer 4 votos maximos, 
                                                    #ya que solo hay 4 cargos, si n es mayor a la cantidad de votantes*cantidad de cargos posibles a votar,
                                                    # habra mas registros que cantidad de votos maximos y se generara un bucle infinito en la funcion registro
                                        
    try:
        n = int(input('La cantidad de registros ingresada es invalida o excede la cantida de registros posibles, por favor reingresar cantidad: '))
    except:
        n = -1







# carga de documentos, regiones y sufragios
sufragio=votos(asignacion(registros()),abreviaturas,cargos_politicos)


#creacion del archivo
with open('archivo_votacion.csv', 'w') as archivo:
        archivo.write('DNI;Region;Cargo;Partido\n')
        for i in range(len(sufragio)):
            archivo.write(f'{sufragio[i]["dni"]};{sufragio[i]["region"]};{sufragio[i]["cargo"]};{sufragio[i]["partido"]}\n')


#conteo de votos e impresion por pantalla
conteoRegion()
