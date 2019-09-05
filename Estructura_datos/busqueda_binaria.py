# -*- coding: utf-8 -*-
import random

def binary_search(numbers, number_to_find, low, high):
    
    if low > high:
        return False

    mid = int((low + high) / 2)

    if numbers[mid] == number_to_find:
        return True

    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    
    else:
        return binary_search(numbers, number_to_find, mid +1, high)

    

if __name__ == "__main__":
    #numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]
    size = int(input('Ingresa tamaño de la lista: ')) 
    numbers = [random.randint(0,100) for i in range(size)] #creo la lista aleatoria de n numero entre 0 - 100
    numbers = sorted(numbers) # Ordeno la lista de menor a mayor
    number_to_find = int(input('Ingresa un numero: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El número: {}, si esta en la lista.'.format(number_to_find))
    else:
        print('El número: {}, No esta en la lista.'.format(number_to_find))