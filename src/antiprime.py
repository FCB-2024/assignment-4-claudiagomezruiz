## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys

def main() :
    ## YOU CODE SHOULD START HERE AST THE SAME
    ## IDENTATION AS THIS COMMENT
    x = int(sys.argv[1])  # Agafem el valor de la línia de comandes

    def comptar_divisors(x):
        c = 0
        divisor = 1
        while divisor <= x:
            if x % divisor == 0:
                c += 1
            divisor += 1
        return c

    # Comptem els divisors de n
    divisors_x = comptar_divisors(x)
    es_antiprime = True  # Suposem que n és antiprime
    i = 1
    while i < x:
        if comptar_divisors(i) >= divisors_x:
            es_antiprime = False  # Si algun nombre més petit té tants o més divisors, no és antiprime
            break  # Ja podem parar la cerca
        i += 1

    ## THE LAST LINES OF YOUR CODE SHOULD EITHER
    ## RETURN THE VALUE "anti-prime" or "not anti-prime"
    ## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
    ## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
    ## "anti-prime" or "not anti-prime"
    if es_antiprime:
        return "anti-prime"
    else:
        return "not anti-prime"

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

    ## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
    ## TO RUN THIS PROGRAM AS, FOR INSTANCE:
    ## $ python antiprime.py 6
    ## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
    ## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
    print(main())
