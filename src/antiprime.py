import sys

def main():

    #Si hi ha arguments passats per la línia de comandes
    x = int(sys.argv[1])  #Agafa el primer argument passat com a número
    
    # Inicialitza variables
    

    def comptar_divisors(x):
        i = 1
        divisors_x = 0
    # Compta el nombre de divisors de x
        while i <= x:
            if x % i == 0:
                divisors_x += 1
            i += 1
        return divisors_x #ensenya el nombre de divisors que té


#Ara he comptat els divisors només de x, vull saber els divisors dels seus nombres inferiors:
#Perquè ens guardi el número de divisors_x, com que s'elimina, creeem una nova variable que és divisors_x2 perquè ens el guardi i el compararem més tard.

    divisors_x2 = comptar_divisors(x)

 #fem una suposició:
    
    es_antiprime = True
    comptador = 1
    while comptador < x:
        if comptar_divisors(x) >= divisors_x2:
            es_antiprime = False
            break
        comptador += 1   

    if es_antiprime:
        return ("anti-prime")
    else:
        return ("not anti-prime")

   

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__":
    # Crida la funció principal i imprimeix el resultat
    print(main())
