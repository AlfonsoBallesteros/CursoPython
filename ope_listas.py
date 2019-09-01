# -*- coding: utf-8 -*-
mi_lista = []
print(type(mi_lista))
mi_lista.append(1)
print(mi_lista)
mi_lista_2 = [2, 3, 4]

mi_lista_3 = mi_lista + mi_lista_2 #agrega los elementos de una lsta al principio de la otra
print(mi_lista_3)

mi_lista_4 = ['a']

mi_lista_5 = mi_lista_4 * 10 #añade el elemento las veces que se multiplica

print(mi_lista_5)

#acceder a diferentes elemntos de la lista
lista = [1,2,3,4,5,6]
print(lista[1:])
print(lista[1:3])
print(lista[1:6:2])
print(lista[::-1])

othe_lista = ['juan', 'pedro', 'pepe']
othe_lista[1] = 'laura' #modifico el elemnto en la posicion dada
print(othe_lista)
othe_lista.append('stella') #agrega un elemento a la lista
print(othe_lista)
nombre = ''
nombre = othe_lista.pop() #Eliminamos el ultimo elemento de lista
print(othe_lista)
print(nombre == 'stella') #verificamos el elemento eliminado
lista_des = [2,5,8,7,4,1,3,6,9,0]
lista_des.sort() #Ordenar lista
print(lista_des)
othe_lista.extend(lista_des) #operacion suma con funcion
print(othe_lista)
utiles = ['lapiz', 'cuadernos', 'calcualdora']
del utiles[0]
print(utiles)

Casa= 'casa'
Lista_casa = list(Casa) #pasar de un String a una lista
print(Lista_casa)

Lista_casa[0]='C'
print(Lista_casa)
str_casa = ''.join(Lista_casa) #de lista a String
print(str_casa)