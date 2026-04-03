#practiced problem  To get prime number using function and loops 

def is_prime(num):
    if num==1:
       return False #notprimt
    elif num==2:
        return True #is_prime
    else:
        if num>1:
            newnum=num-1
            result=True
            while newnum>1:
                if num%newnum==0:
                    result=False
                    return result # is divisible by other number not prime
                newnum=newnum-1
                
            return result    
    

print(is_prime(75))
        
       #output: False 
       
       
