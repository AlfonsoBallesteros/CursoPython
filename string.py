# -*- coding: utf-8 -*-
my_string = 'platzi'
my_other_string = 'EDIFICIO'
digito = '258'
print(my_string[0]) #acceder a la letra atraves de su posicion
print(len(my_string)) #devuelve la longitud del string 
#empiza en 1
print(my_string[len(my_string) - 1])
#upper -> String en mayusculas
print(my_string.upper())
#isupper -> verifica si esta en mayusculas
print(my_other_string.isupper())
#lower -> String en minisculas
print(my_other_string.lower())
#islower -> verifica si es en minisculas
print(my_string.islower())
#find -> devuelve la poscion de la letra del String
print(my_string.find('l'))
#isdigit -> verifica si es un digito
print(digito.isdigit())
#endswith -> verifica si termina con [letra]
print(my_string.endswith('i'))
#startswith -> verifica si comienza con [letra]
print(my_string.startswith('p'))
#split -> 
print(my_string.split())
#join -> parte el String en letras
print(' * '.join(my_string))