#!/usr/bin/env python
# coding: utf-8

# ___
# 
# Mr. Yogesh P Murumkar (Mob. 9657080906)
# 
# https://www.youtube.com/c/yogeshmurumkar
# ___
# # Python Course Exercises 1
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners.

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[3]:


7**4


# ** Split this string:**
# 
#     s = "Hi there Yogesh!"
#     
# **into a list. **

# In[4]:


s="Hi there Yogesh!"


# In[5]:


s.split()


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[1]:


planet = "Earth"
diameter = 12742


# In[2]:


print("The daimeter of () is () kilometer.".format(planet,daimeter))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[3]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[1]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[8]:


lst[3][1][2][0]


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[9]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[10]:


d['k1'][3]['tricky'][3]['target'][3] 


# ** What is the main difference between a tuple and a list? **

# In[23]:


# Tuple is immutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[20]:


def fun1(email1):
    return email.split('@')[-1] 


# In[21]:


fun1('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[27]:


def findDog(st)
return 'dog'in st.lower().split()


# In[28]:


findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[30]:


def countDog(st):
    count=0
    for word in st.lower().split():
        if word == 'dog':
            count += 1
    return count


# In[31]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[34]:


seq = ['soup','dog','salad','cat','great']


# In[35]:


list(fliter(lanbda word: word[0]=='s',seq))


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[36]:


def caught_speeding(speed, is_birthday):
    pass


# In[42]:


caught_speeding(81,True)


# In[43]:


caught_speeding(81,False)


# In[ ]:


Question
Given a string print number num by extracting all the
digits from the string as in string
Print negative number if the first character in 
string is '-'
eg.
-123abcd should return -123,abcd456-->456,fdhfh78dsd89--->7889,-56dssd78-->5678


# In[ ]:


Q2
WAP to check whether a number is palindrome or not on following conditions.
1. take input number
2. add number and its reverse
3. check that number is palindrome or not,if not then sum and its reverse


# In[ ]:


Write a python function to find and display the five 
digit number in which the first digit is two more than 
the second,the second digit is two more than the third,
the fourth digit is two less than the third, and the 
last digit is two more than
the fourth.The sum of the third,fourth and fifth digits
equals the first.The sum of all the digits is 19


# In[12]:


def fivedigitnumber():

   #Let us keep i as a constant and then complete the relation of other terms

   for i in range(9,0,-1):
       d1=i
       d2 = i-2
       d3=i-4
       d4=i-6
       d5=i-4

       #checking the condition

       if d3+d4+d5==d1:

           if (d1+d2+d3+d4+d5)==19:

               return(int(str(d1)+str(d2)+str(d3)+str(d4)+str(d5)))

print(fivedigitnumber())

    
    
    
    
    
    
    
    


# In[ ]:





# # Great job!
