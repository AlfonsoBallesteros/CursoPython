# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    make_square(dave) #llamamos funcion 

    turtle.mainloop()

def make_square(dave):
    print('Ingrese tamano del cuadrado')
    length = int(input())

    for i in range(6): #ciclo for 
        make_line_and_turn(dave, length) #llamamos funcion con dos parametros
        dave.left(60)
        for i in range(3):
            make_line_and_turn(dave, length)

def make_line_and_turn(dave, length): #dibujar el cuadrado
    dave.forward(length)
    dave.left(90)

if __name__ == "__main__":
    main()