## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main() :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
 x = int(input("Enter a positive integer number: "))
 i = 1
 divisors_x = 0

 while i <= x:
	if x % i == 0:
		divisors_x = divisors_x + 1
	i = i + 1

 menors < x
 divisors_menors = 0

 while menors < x:
	if menors % i == 0:
		divisors_menors = divisors_menors + 1
	i = i + 1

 anti_prime = divisors_x > divisors_menors

 if divisors_x > divisors_menors:
	res("anti-prime")
 else:
	res("not anti-prime")

 return(res)
## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main())
