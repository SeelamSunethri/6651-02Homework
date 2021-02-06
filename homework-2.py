#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('\n Enter a number between 1-100')

# Algorithm
count = 0
lrange = 1
hrange = 100
mid = 50

while True:
    answer = input('Numerical value is higher, lower or equal to ' + str(mid) + ':')
    if answer == 'lower':
        hrange = mid
        mid = int((lrange + mid)/2)
    elif answer == 'higher':
        lrange = mid
        mid = int((hrange + mid) / 2)
    elif answer == 'equal':
        break
    else:
        print('Unrecognizable answer. Use: "lower", "higher", "equal"')
    count += 1

print('Steps to complete', count, 'to guess your number.')
print('do you want to play more')
val=input('yes or no\n')
if val == 'no':
    print('bye')


# In[4]:


s="tyson"
y=list(s)
print(y)


# In[7]:


print("".join(y))


# In[ ]:




