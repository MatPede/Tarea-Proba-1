import matplotlib.pyplot as mplt

data1 = open("disney_plus_titles.csv", "r", encoding="utf8")
data = data1.read()
data1.close()

data1 = data.split("\n")
datos = data1.pop(0)
data = []

for i in data1:
    a = i.split(',')
    data.append(a)

data.pop(-1)

# funciones necesarias para crear la lista con todos los datos


def crear_listapop(lista, valor1, valor2):
    lista_pop = []
    for i in range(len(lista)):
        if valor1 <= i <= valor2:
            lista_pop.append(i + 1)
    return lista_pop


def crear_lista_datos_agrupados_en_comillas(lista, valor1, valor2):
    listax = []
    for i in range(len(lista)):
        if valor1 <= i <= valor2:
            a = lista[i]
            a = limpiar_comillas(a)
            listax.append(a)
    return listax


def popearx(lista, listapop):
    decontador = 0
    for i in listapop:
        lista.pop(i - decontador)
        decontador += 1


def limpiar_comillas(string):
    if string[0] == '\"':
        string = string[1:]
    if string[-1] == '\"':
        string = string[:-1]
    return(string)


def listar_comillas(lista):
    es_lista = False
    paso = False
    for i in range(len(lista)):
        if paso == False:
            if es_lista == False:
                contador_lista = 0
                contador_lista2 = 0

            if len(lista[i]) > 0:
                if lista[i][0] == '\"':
                    contador_lista = i
                    es_lista = True

                elif lista[i][-1] == '\"':
                    contador_lista2 = i
                    es_lista = False
                    listax = crear_lista_datos_agrupados_en_comillas(
                        lista, contador_lista, contador_lista2)
                    lista_pop = crear_listapop(
                        lista, contador_lista, contador_lista2)
                    lista.insert(contador_lista, listax)
                    popearx(lista, lista_pop)
                    paso = True


for j in range(len(data)):
    for i in range(11):
        listar_comillas(data[j])

datos = datos.split(",")

# hasta aca funciona y cree 2 listas, data es toda la informacion del dataset
# y datos dice a que se refiere cada dato de cada pelicula,
# ej: nombre, año de lanzamiento, etc...

años_creados = []
años_creados_i = []
for i in range(len(data)):
    años_creado = int(data[i][7])
    if años_creado > 2009 and años_creado < 2022:
        años_creados.append(años_creado)
        años_creados_i.append(i)

años_agregados = []
for i in range(len(data)):
    if len(data[i][6]) > 0:
        año_agregado = data[i][6][1]
        año_agregado = int(año_agregado[1:])
        if i in años_creados_i:
            años_agregados.append(año_agregado)

lista_años_creados_cantidades = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista_años_agregados_cantidades = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista_años = [2010, 2011, 2012, 2013, 2014,
              2015, 2016, 2017, 2018, 2019, 2020, 2021]

for i in años_agregados:
    for j in range(len(lista_años)):
        if i == lista_años[j]:
            lista_años_agregados_cantidades[j] += 1

for i in años_creados:
    for j in range(len(lista_años)):
        if i == lista_años[j]:
            lista_años_creados_cantidades[j] += 1

fig, ax = mplt.subplots()
ax.scatter(lista_años, lista_años_agregados_cantidades,
           label="Cantidad de elementos que fueron agregados en cada año")
ax.scatter(lista_años, lista_años_creados_cantidades,
           label="Cantidad de elementos según su año de lanzamiento")
ax.legend(loc='upper left')
mplt.show()
