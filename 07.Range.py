import time

print("\nHello World\n")
start = time.time()

# ---------------------------------------------------------------------------------
#RANGE
x = range(10)
for i in x :
        print(i)

x1 = range( 30 , 40 , 2 )
for i in x1 :
        print(i)

x2 = list(range(10))
print(x2)

end = time.time()
print( "\nTIME TAKEN (nanoseconds)  =" , (end - start)*10**9 , "\n" )