def lectura_de_archivos():
    # lectura partidos politicos
    partidos = []
    with open("./partidos.csv") as partidos_politicos:  # lista de partidos politicos
        datos_partidos = partidos_politicos.readlines()
        datos_partidos.pop(0)
        for i in datos_partidos:  # carga de lista
            partido = i.split(";")[0]
            abrev = i.split(";")[1]
            nro_lista = i.split(";")[2].replace("\n", "")
            partidos.append({"nombre": partido, "lista": abrev, "nro_lista": nro_lista})

    # lectura regiones geograficas
    regiones = []
    with open("./regiones.csv") as regiones_geograficas:  # lista de regiones
        datos_regiones = regiones_geograficas.readlines()
        datos_regiones.pop(0)
        for j in datos_regiones:  # carga de lista
            region = j.split(";")[0]
            codigo = j.split(";")[1].replace("\n", "")
            regiones.append(
                {
                    "nombre": region,
                    "codigo": codigo,
                }
            )

    return partidos, regiones


# lectura de votos y formateo
def obtencion_datos_votacion():
    votos = []
    with open("archivo_votacion.csv") as archivo_votacion:
        votos_raw = archivo_votacion.readlines()
        votos_raw.pop(0)
    for voto in votos_raw:
        voto_datos = voto.split(";")

        dni_voto = voto_datos[0]
        region_voto = voto_datos[1]
        cargo_voto = voto_datos[2]
        partido_voto = voto_datos[3].replace("\n", "")

        voto_dict = {
            "dni": dni_voto,
            "region": region_voto,
            "cargo": cargo_voto,
            "partido": partido_voto,
        }
        votos.append(voto_dict)
    return votos


# organizar votos por region
def filtrado_votos_region():
    votos_por_region = []
    for region in regiones:
        votos_region = [voto for voto in votos if voto["region"] == region["codigo"]]
        votos_por_region.append({"region": region["codigo"], "votos": votos_region})
    return votos_por_region


# organizar votos por poderes dentro de una region
def separacion_poderes_region():
    votos_poderes_region = []
    for votos_region in votos_filtrados_por_region:
        votos_presidente = [
            voto for voto in votos_region["votos"] if voto["cargo"] == "1"
        ]
        votos_diputado = [
            voto for voto in votos_region["votos"] if voto["cargo"] == "2"
        ]
        votos_senador = [voto for voto in votos_region["votos"] if voto["cargo"] == "3"]
        votos_gobernador = [
            voto for voto in votos_region["votos"] if voto["cargo"] == "4"
        ]
        votos_poderes_region.append(
            {
                "region": votos_region["region"],
                "votos_presidente": votos_presidente,
                "votos_diputado": votos_diputado,
                "votos_senador": votos_senador,
                "votos_gobernador": votos_gobernador,
            }
        )
    return votos_poderes_region


# conteo votos presidente por region
def conteo_votos_presidente():
    conteo_votos_presidentes_region = []
    for votos_region_poder in votos_filtrados_cargo_region:
        # conteo votos ejecutivo en blanco
        cant_votos_blanco_presidente = len(
            [
                voto
                for voto in votos_region_poder["votos_presidente"]
                if voto["partido"] == "blanco"
            ]
        )

        votos_partidos_region_ejecutivo = []
        contador_validos = 0
        for partido in partidos:
            cant_votos_partido = len(
                [
                    voto
                    for voto in votos_region_poder["votos_presidente"]
                    if voto["partido"] == partido["lista"]
                ]
            )
            contador_validos += cant_votos_partido
            votos_partidos_region_ejecutivo.append(
                {"partido": partido["lista"], "cant_votos": cant_votos_partido}
            )

        conteo_votos_presidentes_region.append(
            {
                "region": votos_region_poder["region"],
                "votos_blanco": cant_votos_blanco_presidente,
                "votos": votos_partidos_region_ejecutivo,
                "totales_validos": contador_validos,
                "totales": contador_validos + cant_votos_blanco_presidente,
            }
        )
    return conteo_votos_presidentes_region


# conteo votos gobernador por provincia
def conteo_votos_gobernador():
    conteo_votos_gobernadores_region = []
    for votos_region_poder in votos_filtrados_cargo_region:
        # conteo votos ejecutivo en blanco
        cant_votos_blanco_gobernador = len(
            [
                voto
                for voto in votos_region_poder["votos_gobernador"]
                if voto["partido"] == "blanco"
            ]
        )

        votos_partidos_region_ejecutivo = []
        contador_validos = 0
        for partido in partidos:
            cant_votos_partido = len(
                [
                    voto
                    for voto in votos_region_poder["votos_gobernador"]
                    if voto["partido"] == partido["lista"]
                ]
            )
            contador_validos += cant_votos_partido
            votos_partidos_region_ejecutivo.append(
                {"partido": partido["lista"], "cant_votos": cant_votos_partido}
            )

        conteo_votos_gobernadores_region.append(
            {
                "region": votos_region_poder["region"],
                "votos_blanco": cant_votos_blanco_gobernador,
                "votos": votos_partidos_region_ejecutivo,
                "totales_validos": contador_validos,
                "totales": contador_validos + cant_votos_blanco_gobernador,
            }
        )
    return conteo_votos_gobernadores_region


# conteo votos senador por provincia
def conteo_votos_senador():
    conteo_votos_senadores_region = []
    for votos_region_poder in votos_filtrados_cargo_region:
        # conteo votos ejecutivo en blanco
        cant_votos_blanco_senador = len(
            [
                voto
                for voto in votos_region_poder["votos_senador"]
                if voto["partido"] == "blanco"
            ]
        )

        votos_partidos_region_ejecutivo = []
        contador_validos = 0
        for partido in partidos:
            cant_votos_partido = len(
                [
                    voto
                    for voto in votos_region_poder["votos_senador"]
                    if voto["partido"] == partido["lista"]
                ]
            )
            contador_validos += cant_votos_partido
            votos_partidos_region_ejecutivo.append(
                {"partido": partido["lista"], "cant_votos": cant_votos_partido}
            )

        conteo_votos_senadores_region.append(
            {
                "region": votos_region_poder["region"],
                "votos_blanco": cant_votos_blanco_senador,
                "votos": votos_partidos_region_ejecutivo,
                "totales_validos": contador_validos,
                "totales": contador_validos + cant_votos_blanco_senador,
            }
        )
    return conteo_votos_senadores_region


# conteo votos diputado por region
def conteo_votos_diputado():
    conteo_votos_diputados_region = []
    for votos_region_poder in votos_filtrados_cargo_region:
        # conteo votos ejecutivo en blanco
        cant_votos_blanco_diputado = len(
            [
                voto
                for voto in votos_region_poder["votos_diputado"]
                if voto["partido"] == "blanco"
            ]
        )

        votos_partidos_region_ejecutivo = []
        contador_validos = 0
        for partido in partidos:
            cant_votos_partido = len(
                [
                    voto
                    for voto in votos_region_poder["votos_diputado"]
                    if voto["partido"] == partido["lista"]
                ]
            )
            contador_validos += cant_votos_partido
            votos_partidos_region_ejecutivo.append(
                {"partido": partido["lista"], "cant_votos": cant_votos_partido}
            )

        conteo_votos_diputados_region.append(
            {
                "region": votos_region_poder["region"],
                "votos_blanco": cant_votos_blanco_diputado,
                "votos": votos_partidos_region_ejecutivo,
                "totales_validos": contador_validos,
                "totales": contador_validos + cant_votos_blanco_diputado,
            }
        )
    return conteo_votos_diputados_region


# conteo de poblacion por region sin contar los votos cargados con el mismo documento
def conteo_poblacion_por_region():
    cant_poblacion = []
    poblacion_por_region = []
    for p in range(len(votos)):
        cant_poblacion.append(votos[p]["dni"])
    total_poblacion = len(set(cant_poblacion))  # poblacion total en toda la nacion

    for r in range(len(votos_filtrados_por_region)):  # poblacion total por region
        poblacion = []
        for i in range(len(votos_filtrados_por_region[r]["votos"])):
            poblacion.append(
                votos_filtrados_por_region[r]["votos"][i]["dni"]
            ) 
        poblacion = set(poblacion)
        poblacion_por_region.append(
            {
                "poblacion_total": total_poblacion,
                "region": votos_filtrados_por_region[r]["votos"][r]["region"],
                "habitantes": len(poblacion),
            }
        )
    return poblacion_por_region


# asignacion de bancas por region segun cantidad de poblacion
# en el congreso de la nacion se dicta que son 257 bancas de diputados divididos en todas las regiones
# dichas bancas corresponden a un minimo de 5 por region, y se le sumara 1 cada 161.000 habitantes
# estos datos son tomados a partir del censo efectuada cada 10 años, aunque este mismo esta desactualizado.


# en el trabajo se dispone de 130 bancas de diputados
# por un tema de cantidad de poblacion, regiones y bancas totales de diputados en las que se trabaja el codigo
# Se le asignara un minimo de 3 bancas de diputados a cada region
# luego se divira la cantidad total de poblacion/bancas disponibles
# ese resultado sera un aproximado sobre cada cuantos habitantes por region, se le otorgara 1 banca a la misma
# cabe la posibilidad de al usar resultados enteros queden bancas sin asignar, por lo cual seran asignadas a las region con mayor poblacion
def asigncacion_bancas_diputados():
    bancas_iniciales = 130
    bancas_minimas_por_region = 3
    bancas_disponibles = bancas_iniciales - (
        bancas_minimas_por_region * len(poblacion_por_region)
    )
    bancas_por_habitantes = (
        poblacion_por_region[0]["poblacion_total"]
    ) // bancas_disponibles
    bancas_por_region = []
    bancas_otorgadas = 0
    region_mayor_habitantes = 0
    region_mayor = 0
    for p in range(len(poblacion_por_region)):
        bancas_para_region = (
            poblacion_por_region[p]["habitantes"] // bancas_por_habitantes
        )
        if poblacion_por_region[p]["habitantes"] > region_mayor_habitantes:
            region_mayor = p
            region_mayor_habitantes = poblacion_por_region[p]["habitantes"]
        bancas_otorgadas += bancas_para_region
        bancas_por_region.append(
            {
                "region": poblacion_por_region[p]["region"],
                "bancas": ((bancas_minimas_por_region) + bancas_para_region),
            }
        )
    bancas_sobrantes = bancas_disponibles - bancas_otorgadas
    if bancas_sobrantes > 0:
        bancas_por_region[region_mayor]["bancas"] += bancas_sobrantes
    return bancas_por_region


# dhont diputados
def sistema_dhont():
    # calculos dhont por region
    resultados_dhont_general = []
    bancas = bancas_diputados
    for votos_diputados_region in votos_diputado_conteo_region:
        votos_por_partido = votos_diputados_region["votos"]
        region = votos_diputados_region["region"]
        nro_bancas = [
            regiones_bancas["bancas"]
            for regiones_bancas in bancas
            if region == regiones_bancas["region"]
        ][0]
        resultados_dhont_region = []
        for i in range(1, nro_bancas + 1):
            for votos_partido in votos_por_partido:
                div_dhont = float(f"{(votos_partido['cant_votos']/i):.2f}")
                resultados_dhont_region.append(
                    {"partido": votos_partido["partido"], "resultado_dhont": div_dhont}
                )
        resultados_dhont_general.append(
            {
                "region": votos_diputados_region["region"],
                "resultados_dhont": sorted(
                    resultados_dhont_region,
                    key=lambda d: d["resultado_dhont"],
                    reverse=True,
                )[:nro_bancas],
            }
        )

    # calculo dhont por partido-region
    dhont_cant_bancas_region = []
    for dhont_region in resultados_dhont_general:
        ocurrencias_partidos_region = []
        for partidos_ganadores in dhont_region["resultados_dhont"]:
            ocurrencias_partidos_region.append(partidos_ganadores["partido"])

        cant_banca_partido = {}
        for partido in partidos:
            cont_partido = ocurrencias_partidos_region.count(partido["lista"])
            cant_banca_partido[partido["lista"]] = cont_partido
        dhont_cant_bancas_region.append(
            {
                "region": dhont_region["region"],
                "cant_bancas_partido": cant_banca_partido,
            }
        )
    return dhont_cant_bancas_region


def asignacion_camara_senadores():
    camara_senadores_region = []
    for i in range(len(votos_senador_conteo_region)):
        camara_senadores = []
        mayoria = 0
        partido_mayoria = ""
        primera_minoria = 0
        partido_primera_minoria = ""
        for j in range(len(votos_senador_conteo_region[i])):
            votos = votos_senador_conteo_region[i]["votos"][j]["cant_votos"]
            if votos > mayoria:
                mayoria = votos
                partido_mayoria = votos_senador_conteo_region[i]["votos"][j]["partido"]
            elif votos > primera_minoria and votos < mayoria:
                primera_minoria = votos
                partido_primera_minoria = votos_senador_conteo_region[i]["votos"][j][
                    "partido"
                ]
        camara_senadores.append(
            {"mayoria": partido_mayoria, "primera_minoria": partido_primera_minoria}
        )
        camara_senadores_region.append(
            {
                "region": votos_senador_conteo_region[i]["region"],
                "senadores": camara_senadores,
            }
        )


# creacion archivos
def creacion_archivos():
    # creacion archvios presidente
    for votos_presidente in votos_presidente_conteo_region:
        nombre_provincia = [
            prov["nombre"]
            for prov in regiones
            if prov["codigo"] == votos_presidente["region"]
        ][0]
        with open(
            f"./{nombre_provincia.upper()}_PRESIDENTE.csv", "w"
        ) as archivo:
            archivo.write("region;lista;votos;porcentaje\n")
            
            for votos_lista in votos_presidente["votos"]:
                porcentaje = (
                    votos_lista["cant_votos"] / votos_presidente["totales"] * 100
                )
                nro_lista = [
                    part["nro_lista"]
                    for part in partidos
                    if part["lista"] == votos_lista["partido"]
                ][0]
                archivo.write(
                    f"{votos_presidente['region']};{nro_lista};{votos_lista['cant_votos']};{porcentaje:.2f}%\n"
                )
            porc_blanco = (
                votos_presidente["votos_blanco"] / votos_presidente["totales"] * 100
            )
            archivo.write(
                f"{votos_presidente['region']};VOTOS_BLANCO;{votos_presidente['votos_blanco']};{porc_blanco:.2f}%\n"
            )

    # creacion archvios diputado
    for i in range(len(votos_diputado_conteo_region)):
        votos_diputado=votos_diputado_conteo_region[i]        
        nombre_provincia = [
            prov["nombre"]
            for prov in regiones
            if prov["codigo"] == votos_diputado["region"]
        ][0]
        with open(
            f"./{nombre_provincia.upper()}_DIPUTADO.csv", "w"
        ) as archivo:
            archivo.write("region;lista;votos;bancas;porcentaje\n")
            
            for votos_lista in votos_diputado["votos"]:
                porcentaje = votos_lista["cant_votos"] / votos_diputado["totales"] * 100
                nro_lista = [
                    part["nro_lista"]
                    for part in partidos
                    if part["lista"] == votos_lista["partido"]
                ][0]
                archivo.write(
                    f"{votos_diputado['region']};{nro_lista};{votos_lista['cant_votos']};{votos_diputado_dhont[i]['cant_bancas_partido'][str(votos_lista['partido'])]};{porcentaje:.2f}%\n"
                )
            porc_blanco = (
                votos_diputado["votos_blanco"] / votos_diputado["totales"] * 100
            )
            archivo.write(
                f"{votos_diputado['region']};VOTOS_BLANCO;{votos_diputado['votos_blanco']};--,{porc_blanco:.2f}%\n"
            )
    # creacion archivos senador
    for votos_senador in votos_senador_conteo_region:
        nombre_provincia = [
            prov["nombre"]
            for prov in regiones
            if prov["codigo"] == votos_senador["region"]
        ][0]
        with open(
            f"./{nombre_provincia.upper()}_SENADOR.csv", "w"
        ) as archivo:
            archivo.write("region;lista;votos;porcentaje\n")
            for votos_lista in sorted(votos_senador["votos"], key=lambda d: d["cant_votos"], reverse=True)[:2]:
                porcentaje = votos_lista["cant_votos"] / votos_senador["totales"] * 100
                nro_lista = [
                    part["nro_lista"]
                    for part in partidos
                    if part["lista"] == votos_lista["partido"]
                ][0]
                archivo.write(
                    f"{votos_senador['region']};{nro_lista};{votos_lista['cant_votos']};{porcentaje:.2f}%\n"
                )
            porc_blanco = votos_senador["votos_blanco"] / votos_senador["totales"] * 100
            archivo.write(
                f"{votos_senador['region']};VOTOS_BLANCO;{votos_senador['votos_blanco']};{porc_blanco:.2f}%\n"
            )

    # creacion archvios gobernador
    for votos_gobernador in votos_gobernador_conteo_region:
        nombre_provincia = [
            prov["nombre"]
            for prov in regiones
            if prov["codigo"] == votos_gobernador["region"]
        ][0]
        with open(
            f"./{nombre_provincia.upper()}_GOBERNADOR.csv", "w"
        ) as archivo:
            archivo.write("region;lista;votos;porcentaje\n")
            for votos_lista in votos_gobernador["votos"]:
                porcentaje = (
                    votos_lista["cant_votos"] / votos_gobernador["totales"] * 100
                )
                nro_lista = [
                    part["nro_lista"]
                    for part in partidos
                    if part["lista"] == votos_lista["partido"]
                ][0]
                archivo.write(
                    f"{votos_gobernador['region']};{nro_lista};{votos_lista['cant_votos']};{porcentaje:.2f}%\n"
                )
            porc_blanco = (
                votos_gobernador["votos_blanco"] / votos_gobernador["totales"] * 100
            )
            archivo.write(
                f"{votos_gobernador['region']};VOTOS_BLANCO;{votos_gobernador['votos_blanco']};{porc_blanco:.2f}%\n"
            )


# interfaz por pantalla
def mostrar_info():
    print("\n")
    print("**************")
    print("*            *")
    print("* BIENVENIDO *")
    print("*            *")
    print("**************")
    print("\n")
    print("1. Consulta de resultados Presidente y Vicepresidente")
    print("2. Consulta de resultados Gobernador y Vicegobernador")
    print("3. Consulta de resultados Senadores")
    print("4. Consulta de resultados Diputados")
    while True:
        eleccion = input("Ingrese una opcion: (FIN terminara el programa) ").strip()
        while eleccion not in ["1", "2", "3", "4", "FIN"]:
            eleccion = input("Ingrese una opcion valida: ").strip()
        if eleccion == "FIN":
            return

        # datos presidente
        elif eleccion == "1":
            for votos_presidente in votos_presidente_conteo_region:
                nombre_provincia = [
                    prov["nombre"]
                    for prov in regiones
                    if prov["codigo"] == votos_presidente["region"]
                ][0]
                poblacion_provincia = [
                    pob["habitantes"]
                    for pob in poblacion_por_region
                    if pob["region"] == votos_presidente["region"]
                ][0]
                print("\n")
                ion = "-"
                print(f"****{nombre_provincia.upper()}****".center(100, " "))
                print("ELECCIONES GENERALES 2023".center(100, " "))
                print("CATEGORIA: Presidente".center(100, " "))
                print(f"Electores Habilitados {poblacion_provincia}".center(100, " "))
                print(
                    f"Porcentaje de Votantes {(poblacion_provincia/poblacion_por_region[0]['poblacion_total']*100):.2f}".center(
                        100, " "
                    )
                )
                print(ion * 100)
                print(
                    "N LISTA".center(25, " "),
                    "PARTIDO POLITICO".center(25, " "),
                    "VOTOS".center(25, " "),
                    "%".center(25, " "),
                )
                print(ion * 100)
                for votos in sorted(
                    votos_presidente["votos"],
                    key=lambda d: d["cant_votos"],
                    reverse=True,
                ):
                    porcentaje = votos["cant_votos"] / votos_presidente["totales"] * 100
                    nombre_partido = [
                        part["nombre"]
                        for part in partidos
                        if part["lista"] == votos["partido"]
                    ][0]
                    nro_lista = [
                        part["nro_lista"]
                        for part in partidos
                        if part["lista"] == votos["partido"]
                    ][0]
                    print(
                        f"{nro_lista}".center(25, " "),
                        f"{nombre_partido}".center(25, " "),
                        f"{votos['cant_votos']}".center(25, " "),
                        f"{porcentaje:.2f}".center(25, " "),
                    )
                print(ion * 100)
                print(
                    f"VOTOS POSITIVOS | {votos_presidente['totales_validos']} | ".rjust(
                        94
                    ),
                    f"{(votos_presidente['totales_validos'] / votos_presidente['totales'] * 100):.2f}%".rjust(
                        6
                    ),
                )
                print(
                    f"VOTOS EN BLANCO | {votos_presidente['votos_blanco']} | ".rjust(
                        94
                    ),
                    f"{(votos_presidente['votos_blanco'] / votos_presidente['totales'] * 100):.2f}%".rjust(
                        6
                    ),
                )
                print(
                    f"TOTAL | {votos_presidente['totales']} | ".rjust(94),
                    f"100%".rjust(6),
                )

                print("\n")
                print("*" * 100)
                print("\n")

        # datos gobernador
        elif eleccion == "2":
            for votos_gobernador in votos_gobernador_conteo_region:
                nombre_provincia = [
                    prov["nombre"]
                    for prov in regiones
                    if prov["codigo"] == votos_gobernador["region"]
                ][0]
                poblacion_provincia = [
                    pob["habitantes"]
                    for pob in poblacion_por_region
                    if pob["region"] == votos_gobernador["region"]
                ][0]
                print("\n")
                ion = "-"
                print(f"****{nombre_provincia.upper()}****".center(100, " "))
                print("ELECCIONES GENERALES 2023".center(100, " "))
                print("CATEGORIA: GOBERNADOR".center(100, " "))
                print(f"Electores Habilitados {poblacion_provincia}".center(100, " "))
                print(
                    f"Porcentaje de Votantes {(poblacion_provincia/poblacion_por_region[0]['poblacion_total']*100):.2f}".center(
                        100, " "
                    )
                )
                print(ion * 100)
                print(
                    "N LISTA".center(25, " "),
                    "PARTIDO POLITICO".center(25, " "),
                    "VOTOS".center(25, " "),
                    "%".center(25, " "),
                )
                print(ion * 100)
                for votos in sorted(
                    votos_gobernador["votos"],
                    key=lambda d: d["cant_votos"],
                    reverse=True,
                ):
                    porcentaje = votos["cant_votos"] / votos_gobernador["totales"] * 100
                    nombre_partido = [
                        part["nombre"]
                        for part in partidos
                        if part["lista"] == votos["partido"]
                    ][0]
                    nro_lista = [
                        part["nro_lista"]
                        for part in partidos
                        if part["lista"] == votos["partido"]
                    ][0]
                    print(
                        f"{nro_lista}".center(25, " "),
                        f"{nombre_partido}".center(25, " "),
                        f"{votos['cant_votos']}".center(25, " "),
                        f"{porcentaje:.2f}".center(25, " "),
                    )
                print(ion * 100)
                print(
                    f"VOTOS POSITIVOS | {votos_gobernador['totales_validos']} | ".rjust(
                        94
                    ),
                    f"{(votos_gobernador['totales_validos'] / votos_gobernador['totales'] * 100):.2f}%".rjust(
                        6
                    ),
                )
                print(
                    f"VOTOS EN BLANCO | {votos_gobernador['votos_blanco']} | ".rjust(
                        94
                    ),
                    f"{(votos_gobernador['votos_blanco'] / votos_gobernador['totales'] * 100):.2f}%".rjust(
                        6
                    ),
                )
                print(
                    f"TOTAL | {votos_gobernador['totales']} | ".rjust(94),
                    f"100%".rjust(6),
                )

                print("\n")
                print("*" * 100)
                print("\n")

        # datos senador
        elif eleccion == "3":
            for votos_senador in votos_senador_conteo_region:
                nombre_provincia = [
                    prov["nombre"]
                    for prov in regiones
                    if prov["codigo"] == votos_senador["region"]
                ][0]
                poblacion_provincia = [pob['habitantes'] for pob in poblacion_por_region if pob['region'] == votos_senador["region"]][0]
                print("\n")
                ion = "-"
                print(f"****{nombre_provincia.upper()}****".center(100, " "))
                print("ELECCIONES GENERALES 2023".center(100, " "))
                print("CATEGORIA: SENADOR".center(100, " "))
                print(
                    f"Electores Habilitados {poblacion_provincia}".center(
                        100, " "
                    )
                )
                print(
                    f"Porcentaje de Votantes {(poblacion_provincia/poblacion_por_region[0]['poblacion_total']*100):.2f}".center(
                        100, " "
                    )
                )
                print(ion * 100)
                print(
                    "N LISTA".center(25, " "),
                    "PARTIDO POLITICO".center(25, " "),
                    "VOTOS".center(25, " "),
                    "%".center(25, " "),
                )
                print(ion * 100)
                for votos in sorted(
                    votos_senador["votos"], key=lambda d: d["cant_votos"], reverse=True
                )[:2]:
                    porcentaje = votos["cant_votos"] / votos_senador["totales"] * 100
                    nombre_partido = [
                        part["nombre"]
                        for part in partidos
                        if part["lista"] == votos["partido"]
                    ][0]
                    nro_lista = [
                        part["nro_lista"]
                        for part in partidos
                        if part["lista"] == votos["partido"]
                    ][0]
                    print(
                        f"{nro_lista}".center(25, " "),
                        f"{nombre_partido}".center(25, " "),
                        f"{votos['cant_votos']}".center(25, " "),
                        f"{porcentaje:.2f}".center(25, " "),
                    )
                print(ion * 100)
                print(
                    f"VOTOS POSITIVOS | {votos_senador['totales_validos']} | ".rjust(
                        94
                    ),
                    f"{(votos_senador['totales_validos'] / votos_senador['totales'] * 100):.2f}%".rjust(
                        6
                    ),
                )
                print(
                    f"VOTOS EN BLANCO | {votos_senador['votos_blanco']} | ".rjust(94),
                    f"{(votos_senador['votos_blanco'] / votos_senador['totales'] * 100):.2f}%".rjust(
                        6
                    ),
                )
                print(
                    f"TOTAL | {votos_senador['totales']} | ".rjust(94), f"100%".rjust(6)
                )

                print("\n")
                print("*" * 100)
                print("\n")

        # datos diputado
        elif eleccion == "4":
            for i in range(len(votos_diputado_conteo_region)):
                votos_diputado=votos_diputado_conteo_region[i]
                nombre_provincia = [
                    prov["nombre"]
                    for prov in regiones
                    if prov["codigo"] == votos_diputado["region"]
                ][0]
                poblacion_provincia = [
                    pob["habitantes"]
                    for pob in poblacion_por_region
                    if pob["region"] == votos_diputado["region"]
                ][0]
                print("\n")
                ion = "-"
                print(f"****{nombre_provincia.upper()}****".center(100, " "))
                print("ELECCIONES GENERALES 2023".center(100, " "))
                print("CATEGORIA: DIPUTADO".center(100, " "))
                print(f"Electores Habilitados {poblacion_provincia}".center(100, " "))
                print(
                    f"Porcentaje de Votantes {(poblacion_provincia/poblacion_por_region[0]['poblacion_total']*100):.2f}".center(
                        100, " "
                    )
                )
                print(ion * 100)
                print(
                    "N LISTA".center(20, " "),
                    "PARTIDO POLITICO".center(20, " "),
                    "VOTOS".center(20, " "),
                    "BANCAS".center(20, " "),
                    "%".center(20, " "),
                )
                print(ion * 100)
                for votos in sorted(votos_diputado["votos"], key=lambda d: d["cant_votos"], reverse=True):

                    porcentaje = votos["cant_votos"] / votos_diputado["totales"] * 100
                    nombre_partido = [
                        part["nombre"]
                        for part in partidos
                        if part["lista"] == votos["partido"]
                    ][0]
                    nro_lista = [
                        part["nro_lista"]
                        for part in partidos
                        if part["lista"] == votos["partido"]
                    ][0]
                    print(
                        f"{nro_lista}".center(20, " "),
                        f"{nombre_partido}".center(20, " "),
                        f"{votos['cant_votos']}".center(20, " "),
                        f"{votos_diputado_dhont[i]['cant_bancas_partido'][str(votos['partido'])]}".center(20, " "),
                        f"{porcentaje:.2f}".center(20, " "),
                    )
                print(ion * 100)
                print(
                    f"VOTOS POSITIVOS | {votos_diputado['totales_validos']} | ".rjust(
                        94
                    ),
                    f"{(votos_diputado['totales_validos'] / votos_diputado['totales'] * 100):.2f}%".rjust(
                        6
                    ),
                )
                print(
                    f"VOTOS EN BLANCO | {votos_diputado['votos_blanco']} | ".rjust(94),
                    f"{(votos_diputado['votos_blanco'] / votos_diputado['totales'] * 100):.2f}%".rjust(
                        6
                    ),
                )
                print(
                    f"TOTAL | {votos_diputado['totales']} | ".rjust(94),
                    f"100%".rjust(6),
                )
                print("*" * 100)
                print("\n")


###################################################

partidos, regiones = lectura_de_archivos()

votos = obtencion_datos_votacion()

votos_filtrados_por_region = filtrado_votos_region()

votos_filtrados_cargo_region = separacion_poderes_region()

poblacion_por_region = conteo_poblacion_por_region()

votos_presidente_conteo_region = conteo_votos_presidente()

votos_gobernador_conteo_region = conteo_votos_gobernador()

votos_senador_conteo_region = conteo_votos_senador()

camara_senadores=asignacion_camara_senadores()

votos_diputado_conteo_region = conteo_votos_diputado()
bancas_diputados = asigncacion_bancas_diputados()
votos_diputado_dhont = sistema_dhont()

archivos_conteo_votos = creacion_archivos()
mostrar_info()

