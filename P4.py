import pandas as pd
import matplotlib.pyplot as mplt

data = pd.read_csv("disney_plus_titles.csv")
datatvg = []
for i in data.iloc:
    if i["type"] == "Movie":
        if i["rating"] == "TV-G":
            datatvg.append(i)

datatvpg = []
for i in data.iloc:
    if i["type"] == "Movie":
        if i["rating"] == "TV-PG":
            datatvpg.append(i)

duracionestvg = []
for i in datatvg:
    duracionestvg.append(i["duration"])

duracionestvpg = []
for i in datatvpg:
    duracionestvpg.append(i["duration"])

def sacar_espaciomin(list):
    list2 = []
    for i in list:
        list2.append(int(i[:-4]))
    return list2

duracionestvg = sacar_espaciomin(duracionestvg)
duracionestvpg = sacar_espaciomin(duracionestvpg)

mayortvg = 182
mayortvpg = 148

lista_indicestvg = []
for i in range(len(duracionestvg)):
    lista_indicestvg.append(i+1)

lista_indicestvpg = []
for i in range(len(duracionestvpg)):
    lista_indicestvpg.append(i+1)

fig, ax = mplt.subplots()
ax.scatter(lista_indicestvg, duracionestvg)
mplt.show()

fig, ax = mplt.subplots()
ax.scatter(lista_indicestvpg, duracionestvpg)
mplt.show()

