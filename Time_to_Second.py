#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ERROR Handelling
try :
    # While User input time program calculate second and print it , for end user should be typed exit
    while True :
        my_time_to_second = input("")
        # input time number in list
        time_lst = list(my_time_to_second)
        # if type exit , program end
        if my_time_to_second == 'exit':
            break
        # calculate Second
        else:    
            # split numbers with collon (:)
            time_lst = my_time_to_second.split(':')
            # Convert hour to second 
            hour = int(time_lst[0]) * 3600
             # Convert minutes to second 
            minutes = int(time_lst[1]) * 60
            # Second is second not nedd convert
            second = int(time_lst [2])
            # sum hour+minutes+second = second
            print(hour + minutes + second)
except ValueError :
    print("Dont get string")
    
except IndexError:
    print("Please Enter Ture Format example = 10:12:15")

