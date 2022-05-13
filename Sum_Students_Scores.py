#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Get Numbers Of Students in students_counts Variable
students_counts = int(input("students count : "))
# define varibles 
# for true while
count = 0
# for sum scores students
sum_scores = 0
# for score student (n)
n = 1
# while count < students_counts this True
while count < students_counts :
    # get student scores
    scores = int(input("Enter score student {} : ".format(n)))
    # sum student scores
    sum_scores += scores
    # for end while
    count += 1
    # for score student (n)
    n = n + 1
# print avarege student scores
print("Average Of Student Scores : ",sum_scores/students_counts)

