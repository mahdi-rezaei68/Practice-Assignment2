#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Type exit For End\n")

sum_numbers = 0 
# While user enter number get input and sum numbers , for end user should be enter exit
while True:
    numbers = input("Please Enter NUmbers For Sum ")
    if numbers == 'exit':
        break
    sum_numbers = float(sum_numbers) + float(numbers) 
print(sum_numbers)
    

