import sys

def main():

    #Si hi ha arguments passats per la línia de comandes
    x = int(sys.argv[1])  #Agafa el primer argument passat com a número
    
    # Inicialitza variables
    i = 1
    divisors_x = 0

    # Compta el nombre de divisors de x
    while i <= x:
        if x % i == 0:
            divisors_x += 1
        i += 1

    # Inicialitza la variable per als números menors
    menors = x - 1
    divisors_menors = 0

    # Compta els divisors del nombre més gran que és menor que x
    i = 1  # Reinicialitza i
    while i <= menors:
        if menors % i == 0:
            divisors_menors += 1
        i += 1

    # Determina si x és anti-prime
    if divisors_x > divisors_menors:
        result = "anti-prime"
    else:
        result = "not anti-prime"

    return result

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__":
    # Crida la funció principal i imprimeix el resultat
    print(main())
