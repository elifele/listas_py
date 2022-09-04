#acceso de elementos de lista por indice

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Uranos", "Neptuno"]

print (F"El primer planeta es: {planetas [0]} ")
print (F"El segundo planeta es: {planetas [1]} ")
print (F"El tercer planeta es: {planetas [2]} ")

print()

#modificar valores de una lista

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Uranos", "Neptuno"]

planetas [3] = "Planeta rojo"

print(f"Marte es tambien conocido como: {planetas[3]} ")

print(planetas)

print()

#Determinación de la longitud de una lista

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Uranos", "Neptuno"]

numeros_de_planetas = len(planetas)

print(f"Los numeros de planetas son: {numeros_de_planetas} ")

print()

#Incorporacion de valores a listas

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Uranos", "Neptuno"]

planetas.append("Pluton")

numeros_de_planetas = len(planetas)

print(f"En relidad hay {numeros_de_planetas} planetas en el sistema solar")

print(planetas)

print()

#Eliminacion de valores de listas

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Uranos", "Neptuno", "Pluton"]

planetas.pop()

numeros_de_planetas = len(planetas)

print(f"No, hay definitivamente {numeros_de_planetas} planetas en el sistema solar ")

print(planetas)

print()

#Busqueda de un valor de una lista

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Uranos", "Neptuno"]

tierra_index = planetas.index("Tierra")

print(f"tierra es el {tierra_index + 1} planeta del sistemma solar ")

print()

#almacenamiento de numeros en listas 

gravedad_planetas = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

bus_peso = 12650 # en kg

print(f"En al tierra un autobus de dos pisos pesa: {bus_peso} Kg ")
print(f"En mercurio un autobus de dos pisos pesa: {gravedad_planetas[0]}Kg ")

print()

#uso de la funcion (max) y funcion (min) en las listas

gravedad_planetas = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

bus_peso = 12650 #kg

print(f"En la tierra un autobus de dos pisos pesa {bus_peso} kg ") 
print(f"El peso ligero de un autobus en en el sistema solar {bus_peso * min(gravedad_planetas)} Kg")
print(f"El peso  pesado de un autobus en el sistema solar {bus_peso * max(gravedad_planetas)} Kg ")

print()

#Segmentacion de listas

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Uranos", "Neptuno"]

planetas_antes_tierra = planetas[0:2]

print(f"Planetas antes de la tierra: {planetas_antes_tierra} ")

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Uranos", "Neptuno"]

planetas_despues_tierra = planetas[3:]

print(f"Planetas despues de la tierra: {planetas_despues_tierra} ")

print()

#Combinación de listas, unir dos listas 

grupo_amaltea = ["Metis", "Adrastea", "Amaltea", "Tebe"]
grupo_galiliano = ["Io", "Europa", "Ganimedes", "Calisto"]

lunas_satelitales_regulares = grupo_amaltea + grupo_galiliano 

print(f"Las lunas satelitales regulares de jupiter son: {lunas_satelitales_regulares} ")

print()

#Ordenar lista en orden alfabetico

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Uranos", "Neptuno"]

ordenar = planetas.sort()

print(planetas)

inverso = planetas.sort(reverse=True)#para ordenar lista de orden inverso

print(planetas)










































