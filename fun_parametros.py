# -*- coding: utf-8 -*-
def foreign_exchange_calculator(ammount):#funcion con parametros
    mex_to_col_rate = 145.97

    return mex_to_col_rate * ammount #retorno de la funcion
def run():
    print('CALCULADORA DE DIVISAS')
    print('convierte pesos mexicanos a pesos colombianos.')
    print('')
    #tipado en el input
    ammount = float(input('Ingresa la cantidad de pesos mexicanos que quieres convertir '))
    
    result = foreign_exchange_calculator(ammount)
    #asiganamos la funcion a una variable
    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, result))
    #otra manera de concatenar /recomendado
    print('')
if __name__ == "__main__":
    run()