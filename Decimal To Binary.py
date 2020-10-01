def dectobinary(n):          #Made a recursive Loop where the remainder of
        if n==1:             # the decimal gets divided by 2 
            return(str(1)) 
        else:
           return(str(n%2)+dectobinary(n//2))
# To run the program
s=dectobinary(293)
print(s)
'''Output = 101001001'''
