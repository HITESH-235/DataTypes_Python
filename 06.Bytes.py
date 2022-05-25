import time

print("\nHello World\n")
start = time.time()

# ---------------------------------------------------------------------------------
#Bytes is another type of array with some differences.
#bytes must be in range(0, 256).
#editing is not allowed in the function byte().
#But it is allowed in bytearray().
x = [ 10 , 20 , 30 , 0 , 10 ]
y = bytes(x)
# y[ 3 ] = 256 #will give error
for i in y :
        print(i)

print('\n')
# ---------------------------------------------------------------------------------
z = bytearray(x)
z[ 3 ] = 255
for i in z : 
        print(i)

end = time.time()
print( "\nTIME TAKEN (nanoseconds)  =" , (end - start)*10**9 , "\n" )