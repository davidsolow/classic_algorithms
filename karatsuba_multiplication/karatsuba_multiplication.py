def Karatsuba(x, y):
  if x < 10 and y < 10:   #Base case, assume single digit multiplication is a primitive
    return x * y

  xlength = len(str(x))   #Get number of digits to use to parse out inputs
  ylength = len(str(y))
  n = max(xlength, ylength)
  n_over_2 = round(n/2)   #used to split inputs down the middle

  a = x // (10 ** n_over_2)   #Karatsuba components
  b = x % (10 ** n_over_2)
  c = y // (10 ** n_over_2)
  d = y % (10 ** n_over_2)

  ac = Karatsuba(a, c)    #Recursive calls
  bd = Karatsuba(b, d)
  ad_plus_bc = Karatsuba(a + b, c+d) - ac - bd

  return (10 ** (2*n_over_2))*ac + (10 ** n_over_2)*ad_plus_bc + bd

# Inputs

x = int(3141592653589793238462643383279502884197169399375105820974944592)
y = int(2718281828459045235360287471352662497757247093699959574966967627)

# Check Solution

print(x*y)
print(Karatsuba(x,y))
print(x*y == Karatsuba(x,y))