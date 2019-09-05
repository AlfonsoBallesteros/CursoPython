# -*- coding: utf-8 -*-
mi_diccionario = {} #creo el diccionario
mi_diccionario['primer_elemento'] = 'Hola' #asigno una llave y a valor 
mi_diccionario['segundo_elemento'] = 'Adios'

print(mi_diccionario['primer_elemento']) #accedo al valor atraves de la llave

print('---------------------------------')

calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['calculo'] = 10
calificaciones['web'] = 9
calificaciones['bases_de_datos'] = 10

for key in calificaciones: #iterar atraves de las llaves
    print(key)

for value in calificaciones.values(): #iterar atraves de los valores
    print(value)

for key, value in calificaciones.items(): #iteramos las llaves y el valor
    print('llave: {}, valor: {}'.format(key, value))

print('---------------------------------------')

suma_de_calificaciones = 0

# no llamar la variable que itera igual al diccionario -> calificaciones != calificaciones.values()
for calificacion in calificaciones.values():
    suma_de_calificaciones += calificacion

print(suma_de_calificaciones)
size = len (calificaciones)
print(size)
promedio = suma_de_calificaciones / size
print('Tu promedio es: {}'.format(promedio))