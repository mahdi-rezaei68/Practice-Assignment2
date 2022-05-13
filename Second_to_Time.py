#!/usr/bin/env python
# coding: utf-8

# In[2]:


try :
    # While User input second program calculate hour:minute:second and print it , for end user should be typed exit
    while True :
        my_second_to_time = input("")
        if my_second_to_time == 'exit':
            break
        else:    
            # convert str to int for calculate 
            my_second_to_time = int(my_second_to_time)
            # Convert second to hour
            hour = (my_second_to_time) // 3600
            # convert second to minutes 
            minutes = int(((my_second_to_time / 3600) % (1)) * (60))
            # convert second TO second , need calculate complex
            second = int(round((((my_second_to_time / 3600) % (1)) * (60) % 1) * 60))
            print(hour,":",minutes,":",second)
except ValueError :
    print("Dont get string")
    
except IndexError:
    print("Please Enter Ture Format example = 10:12:15")


# In[3]:


try :
    # While User input second program calculate hour:minute:second and print it , for end user should be typed exit
    while True :
        my_second_to_time = input("")

        if my_second_to_time == 'exit':
            break

        else: 
            # convert str to int for calculate 
            my_second_to_time = int(my_second_to_time)
            # Convert second to hour
            hour = (my_second_to_time) // 3600
            # convert second to minutes 
            minutes = my_second_to_time // 60 % 60
            # convert second TO second , need calculate complex
            second = my_second_to_time / 60 % 60 % 1 * 60 // 1
            # second round for true calculate , you can test with and whithout round and see Results
            print(hour,":",minutes,":",round(second))
except ValueError :
    print("Dont get string")
    
except IndexError:
    print("Please Enter Ture Format example = 10:12:15")


# In[ ]:




