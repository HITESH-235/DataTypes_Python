print( "HELLO WORLD" , "\n" )

# Numeric (Int, float, complex)

print("INTEGERS :")
a0 = 108
print( "a0 =" , a0 , "\n" , type(a0) ,"\n" , type(a0) is int , "\n" )
#---------------------------------------------------------------------------------
print("FLOAT :")
a1 = 3.14
print( "a1 =" , a1 , "\n" , type(a1) , "\n" , type(a1) is float )
a2 = 2.5e4      # 2.5 x 10^4
print( "a2 =" , a2 , "\n" , type(a2) , "\n" , type(a2) is float , "\n" )
# ---------------------------------------------------------------------------------
print("COMPLEX NUMBERS :")
a3 = -2 - 5j
# (-2) is real part & (-5) is the imaginary & j = square root of (-1)
print( "a3 =" , a3 , "\n" , type(a3) , "\n" , type(a3) is complex )
a4 = 4j
# Remember that only j should be used to represent
print( "a4 =" , a4 , "\n" , type(a4) , "\n" , type(a4) is complex , "\n" )
# ---------------------------------------------------------------------------------
# Operations of complex numbers
print( "-2-5j + 0 + 4j = " , a3 + a4 )                   #ADDITION
print( "-2 - 5j - ( 0 - 4j ) = " , a3 - a4 )             #SUBTRACTION
print( "( -2 - 5j ) x ( 0 - 4j ) = " , a3*a4 )           #MULTIPLICATION
print( "( -2 - 5j ) / ( 0 - 4j ) = " , a3/a4 , "\n" )  #DIVISION
# ---------------------------------------------------------------------------------
# Other methods of complex numbers
print( a3.real , "&"  , a3.imag) 
print( a4.real , "&"  , a4.imag)
print( "Conjugate of a3 & a4 :" , a3.conjugate() , "&" , a4.conjugate() )
print( "1 // Absolute value of a3 & a4 :" , "%.2f" % abs(a3) , "&" , "%.2f" % abs(a4) )
# OR :
print( "2 // Absolute value of a3 and a4 :" , format( abs(a3) , ".2f" ) , "&" , format( abs(a4) , ".2f") , "\n" )
# ---------------------------------------------------------------------------------


