import time

print( "HELLO WORLD" , "\n" )
start = time.time()

# ---------------------------------------------------------------------------------
# Converting binary, octal, hexadecimal numbers into decimal

x1 = 0o225                 # An octal number(0 to 7)
# "0o"(Zero and letter o) is always added to a octal number(to avoid error)

x2 = 0b101100001       # A binary number(0,1)
# "0b" is always added to a binary number(to avoid error)

x3 = 0x23d5       # A hexadecimal number(0 to 9, A to F)(A/a = 10 to F/f = 15)
# "0x" is always added to a hexadecimal number(to avoid error)

y1 = int(x1)
y2 = int(x2)
y3 = int(x3) # The int() converts any type of other bases to decimal
print( "Octal 225 =" , y1 )
print( "Binary 101100001 =" , y2 )
print( "Hexadecimal 23d5 =" , y3 , "\n" )
# ---------------------------------------------------------------------------------
# Converting a string containing binary, octal, hexadecimal number into decimal

x11 = "225"
x22 = "101100001"
x33 = "23d5"

y11 = int( x11 , 8 ) #Write the value first then its base
y22 = int( x22 , 2 )
y33 = int( x33 , 16 )
print( "Octal 225 =" , y11 )
print( "Binary 101100001 =" , y22 )
print( "Hexadecimal 23d5 =" , y33 , "\n" )
# ---------------------------------------------------------------------------------
'''Like the int() changes any number into decimal, if possible, 
bin(), oct(), and hex() do the same for others to convert them into binary, octal, & hexadecimal respectively'''

z = 10 #a decimal number
y4 = bin(z)
y5 = oct(z)
y6 = hex(z)
print("10 in binary, octal, hexadecimal :")
print("Binary -" , y4)
print("Octal -" , y5)
print("Hexadecimal -" , y6)
#But these can't convert a string with decimal num
#In simple words, these inbuilt function can only take 1 argument
# ---------------------------------------------------------------------------------
end = time.time()
print( "TIME TAKEN (nanoseconds)  =" , (end - start)*10**9 )