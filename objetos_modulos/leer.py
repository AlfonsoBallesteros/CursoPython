# -*- coding: utf-8 -*-
def run():
    c = 0
    with open('aleph.txt') as f:
        for line in f:
            c += line.count('Beatriz')
    
    print('Beatriz se encuentra {} veces en el texto'.format(c))

if __name__ == "__main__":
    run()