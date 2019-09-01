# -*- coding: utf-8 -*-
import turtle

result_world = []

def draw_hanged(error):
    if error == 1:
        turtle.up()
        turtle.goto(-150, -150)
        turtle.down()
        turtle.forward(100)
    elif error == 2:
        turtle.up()
        turtle.goto(-100, -150)
        turtle.down()
        turtle.left(90)
        turtle.forward(300)
    elif error == 3:
        turtle.up()
        turtle.goto(-100, 150)
        turtle.down()
        turtle.left(-90)
        turtle.forward(150)
    elif error == 4:
        turtle.up()
        turtle.goto(50, 150)
        turtle.down()
        turtle.left(-90)
        turtle.forward(50)
    elif error == 5:
        turtle.up()
        turtle.goto(50, 100)
        turtle.down()
        turtle.dot(50)
    elif error == 6:
        turtle.up()
        turtle.goto(50, 100)
        turtle.down()
        turtle.forward(200)
    elif error == 7:
        turtle.up()
        turtle.goto(0, -100)
        turtle.down()
        turtle.left(90)
        turtle.forward(100)
    elif error == 8:
        turtle.up()
        turtle.goto(0, 0)
        turtle.down()
        turtle.forward(100)
    else:
        turtle.up()
        turtle.goto(0, 50)
        turtle.down()
        turtle.color('red')
        turtle.forward(100)
        turtle.write('M U E R E')
        turtle.done()
        print('M U E R E')
def print_line(size):
    for i in range(size):
        result_world.insert(i, '_')
    print('Tamano de la palabra {}\n'.format(size))
    print('{}\n'.format(result_world))
def guess_world(word, letter, size):
    error = 0
    for i in range(size):
        if letter == word[i]:
            result_world[i] = word[i]
        else:
            error += 1
    if error == size:
        return False, result_world
    else:
        return True, result_world

if __name__ == "__main__":
    
    turtle.setup(500, 500)
    turtle.title("A H O R C A D O")

    error = 0

    word = list('universidad')
    size = len(word)
    print_line(size)

    while error < 9:
        letter = str(input('\nIngresar letra: '))
        result, list_word = guess_world(word, letter, size)
        if result:
            print(list_word)
            if word == list_word:
                print('C O N G R A T U L A T I O N S')
                turtle.up()
                turtle.goto(-100, 200)
                turtle.down()
                turtle.color('green')
                turtle.write('C O N G R A T U L A T I O N S')
                turtle.done()
                break
        else:
            error += 1
            print('Errores {}'.format(error))
            print(list_word)
            draw_hanged(error)