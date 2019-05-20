print("hey user !!! calculate your loan amount")

l=input(" please enter the cost of loan ")
i=input(" please enter the interest rate")
n =input(" please enter the number of installments ")
l=float(l)
i=float(i)
n=float(n)
i=(i/100)
m=l*(i*(i+1)*n)/((1+i)*n-1) # remember here m=l*(i(i+1)n)/((1+i)n-1) this would give error , n u can deduce why !!!!
print ( " your monthly payment will be %f" %m)
print(" HAVE A NICE DAY !!!")