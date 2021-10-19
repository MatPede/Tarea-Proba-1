import pandas as pd
import math
import matplotlib.pyplot as mplt

data = pd.read_csv("disney_plus_titles.csv")
dataComedy= []
for i in data.iloc:
    if i["type"] == "Movie":
        if "Comedy" in i["listed_in"]:
            dataComedy.append(i)

dataFamily= []
for i in data.iloc:
    if i["type"] == "Movie":
        if "Family" in i["listed_in"]:
            dataFamily.append(i)

duracionesComedy = []
for i in dataComedy:
    duracionesComedy.append(i["duration"])

duracionesFamily = []
for i in dataFamily:
    duracionesFamily.append(i["duration"])

def sacar_espaciomin(list):
    list2 = []
    for i in list:
        list2.append(int(i[:-4]))
    return list2

duracionesComedy = sacar_espaciomin(duracionesComedy)
duracionesFamily = sacar_espaciomin(duracionesFamily)

duracionesComedy.sort()
duracionesFamily.sort()

mayorComedy = duracionesComedy[-1]
mayorFamily = duracionesFamily[-1]

cantidad_intervalos_Comedy = int(1+3.22*math.log(mayorComedy, 10)) + 1
cantidad_intervalos_Family = int(1+3.22*math.log(mayorFamily, 10)) + 1

