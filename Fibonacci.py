#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Get How Many NUmbers To Print Fibonacci and try to get integer number

try :
    n = int(input("How many numbers for Fibonacci :"))
    # count for end while 
    count = 0
    # define variable for program
    n1 = 0
    n2 = 1
    fibo = 0
    # run if n <= 0
    if n <= 0 :
        print("Please Possitive number")
    # fibonacci 1 equal to 1
    elif n == 1 :
        print ("FiboNacci = " , n)

    else :
        # True while count <= n  
        while count <= n:
            # fibo start from 0 
            print(fibo,end = ",")
            # fibo = 0 + 1 = 1
            fibo = n1 + n2
            # update value n2 = n1 and n1=fibo for calculate fibonacci = fibo = (n - 2) + (n - 1)
            n2 = n1
            n1 = fibo   
            # increase count for end while
            count +=1
# if n is string error
except ValueError:
    print("Sorry, I didn't understand that.")
    

