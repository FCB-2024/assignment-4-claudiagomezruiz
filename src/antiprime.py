import sys
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE 
## COMMAND LINE SPECIFIED BELOW
def main() :
    ## YOU CODE SHOULD START HERE AST THE SAME
    ## IDENTATION AS THIS COMMENT


    #variables
    a = 1 #porque es el primer posible divisor
    g = 1
    y = 0
    divisor_count = 0 #es la variable que irá sumando divisores, por eso empieza e

    x = int (sys.argv [1])
    
    #contar los divisores de x while a <= x:
    while a <= x:
        if x % a == 0:
            divisor_count += 1
        a += 1

    while g < x:
        divisor_count2 = 0
        b =1
        while b <= g:
            if g % b == 0:
                divisor_count2 += 1
            b += 1
        if divisor_count2 >= y:
            y = divisor_count2
        g += 1

    ## THE LAST LINES OF YOUR CODE SHOULD EITHER
    ## RETURN THE VALUE "anti-prime" or "not anti-prime"
    ## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
    ## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE ## "anti-prime" or "not anti-prime"
    if divisor_count > y:
        return ("anti-prime")
    else:
        return ("not anti-prime")

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__":
    # Crida la funció principal i imprimeix el resultat
    print(main())
