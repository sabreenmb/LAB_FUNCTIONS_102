"""# LAB_FUNCTIONS_102


### hint
a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)    
Also , you can think of it as A Prime Number is a number that cannot be made by multiplying other whole numbers


#### for example, primes between `25` and `50` are:
```
29   
31   
37   
41   
43   
47   
```

"""
def find_primes(num1:int ,num2:int):
    print(f"primes between {num1} and {num2} are:")
    for i in range(num1,num2):
        
        if(i==1 or i==2):
            print(i)
            continue
        is_prime=True

        # to optimize the performance 
        for x in range(2,int(i**0.5)+1):
            if(i%x==0):
                is_prime=False
                break
        if(is_prime):
            print(i)


find_primes(1,100)