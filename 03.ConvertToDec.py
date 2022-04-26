import time
print( "HELLO WORLD" , "\n" )

# Converting Binary, Octal, Hexadecimal into decimal

# ---------------------------------------------------------------------------------
# Finding the base of given quantity

init_num = input( "Enter any Binary / Octal / Hexadecimal number : " )
start = time.time()
init_num = init_num.upper()
dict_hex2 = { 10 : "A" , 11 : "B" , 12 : "C" , 13 : "D" , 14 : "E" , 15 : "F" }

def decbin(n) :
        sum_bin = ""
        while n > 0 :
                r = n%2
                sum_bin += str(r)
                n = n//2
        return(sum_bin[ ::-1 ])

def decoct(n) :
        sum_oct = ""
        while n > 0 :
                r = n%2
                sum_oct += str(r)
                n = n//2
        return(sum_oct[ ::-1 ])

def dechex(n) :
        sum_hex = ""
        while n > 0 :
                r = n%16
                if r > 9:
                        r = dict_hex2[r]
                sum_hex += str(r)
                n = n//16             
        return( sum_hex[ ::-1 ])  
                

        
def bin(n) :
        n = str( n[2:] )
        length = len(n)
        sum_bin = 0
        for i in range( 0 , length ) :
                try:
                       sum_bin+= pow( 2 , i )*int( n[ -( i + 1 ) ] )
                except ValueError :
                        return( "Uh Oh!! Something went wrong" )
                except TypeError :
                        return( "Uh Oh!! Something went wrong" )
                except KeyError :
                        return( "Uh Oh!! Something went wrong" )    
        return(sum_bin)

def oct(n) :
        n = str( n[2:])
        length = len(n)
        sum_oct = 0
        for i in range( 0 , length ) :
                try:
                        sum_oct+= pow( 8 , i )*int( n[ -( i +1 ) ] )
                except ValueError :
                        return( "Uh Oh!! Something went wrong" )
                except TypeError :
                        return( "Uh Oh!! Something went wrong")
                except KeyError :
                        return( "Uh Oh!! Something went wrong" )    
        return(sum_oct)    
                                                            
def hex(n) :
        n = str( n[2:] )
        length = len(n)
        sum_hex = 0
        dict_hex = { "A" : 10 , "B" : 11 , "C" : 12 , "D" : 13 , "E" : 14 , "F" : 15 }
        for i in range( 0 , length ) :
                try :
                        if type( int( n[ -( i + 1 ) ] ) ) == int :
                                sum_hex+= (pow( 16 , i )*int( n[ -( i + 1 ) ] ) ) 
                except ValueError:
                        try :
                                sum_hex+= ( pow( 16 , i )*dict_hex[ n[ -( i + 1 ) ] ] ) 
                        except ValueError :
                                return( "Uh Oh!! Something went wrong" )                                
                        except TypeError :
                                return( "Uh Oh!! Something went wrong" )              
                        except KeyError :
                                return( "Uh Oh!! Something went wrong" )                                       
        return(sum_hex)          

def base_calc(num) :
        num = str(num)
        if num[1] == "B" :
                bin_final = bin(num)
                bin_oct = decoct(bin_final)
                bin_hex = dechex(bin_final)
                return( "Decimal = {x}".format( x = bin_final ) ,"Octal = {y}".format( y = bin_oct ), "Hexadecimal = {z}".format( z = bin_hex ) )
        elif num[1] == "O" :
                oct_final = oct(num)
                oct_bin = decbin(oct_final)
                oct_hex = dechex(oct_final)
                return( "Decimal = {x}".format( x = oct_final ) ,"Binary = {y}".format( y = oct_bin ), "Hexadecimal = {z}".format( z = oct_hex ) )
        elif num[1] == "X" :
                hex_final = hex(num)
                hex_bin = decbin(hex_final)
                hex_oct = decoct(hex_final)
                return( "Decimal = {x}".format( x = hex_final ) ,"Binary = {y}".format( y = hex_bin ), "Decimal = {z}".format( z = hex_oct ) )
        else :
                print(num)
                exit()

base = base_calc(init_num)
print(base)
# ---------------------------------------------------------------------------------
end = time.time()
print( "TIME TAKEN =" , end - start )