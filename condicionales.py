# -*- coding: utf-8 -*-
#descuento atarves de membresia
def run(cuenta):
    membresia = int(input('Digite el tipo de membresia (1, 2 o 3): '))
    
    if membresia == 1:
        descuento = cuenta * 0.1
        pagar = float(cuenta - descuento)
        print("el total a apgar es de ${}".format(pagar))
    elif membresia == 2:
        descuento = cuenta * 0.15
        pagar = float(cuenta - descuento)
        print("el total a apgar es de ${}".format(pagar))
    elif membresia == 3:
        descuento = cuenta *0.20
        pagar = float(cuenta - descuento)
        print("el total a apgar es de ${}".format(pagar))
    else:
        print('Error digite nuevamente')
        run(cuenta)

if __name__ == "__main__":
    cuenta = float(input('Digite el total de la cuenta: $ '))
    run(cuenta)