def armstrong(n):
    temp=n
    a=n+1
    b=n-1
    sop=0
    digits=len(str(n))
    while(n):
        digit=n%10
        sop+=digit**digits
        n=n//10
        if(sop==n):
            print(n,"is armstrong number")
        else:
            print(n,"not an armstrong number")
        if(sop==n+1):
            print(a,"is armstrong number")
        else:
            print(a,"not an armstrong number")   
        if(sop==n-1):
           print(b,"is armstrong number")    
        else:
            print(b,"not an armstrong number")    
armstrong(153)               
        
        
#factorial of first 5 numbers using python compressions
def factorial(num):
    return 1 if num == 0 else num * factorial(num - 1)
op=[factorial(i) for i in range(1,6)] 
print(op)     
        