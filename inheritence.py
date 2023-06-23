#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("hello world")


# # Inheritence

# In[4]:


class parent:
    def test_parent(self):
        print("this is my parent class")


# In[5]:


class child(parent):
    pass


# In[6]:


child_obj=child()


# In[11]:


child_obj.test_parent()


# In[12]:


class class1:
    def test_class1(self):
        print("this is my class1")


# In[13]:


class class2(class1):
    def test_class2(self):
        print("this is my class2")


# In[14]:


class class3(class2):
    def test_class3(self):
        print("this is my class3")


# In[15]:


obj_class3=class3()


# In[16]:


obj_class3.test_class1()


# In[17]:


obj_class3.test_class2()


# In[18]:


obj_class3.test_class3()


# In[19]:


class class1:
    def test_class1(self):
        print("this is my class1")


# In[20]:


class class2:
    def test_class2(self):
        print("this is my class2")


# In[21]:


obj_class3=class3()


# In[22]:


obj_class3.test_class1()


# In[23]:


obj_class3.test_class1()


# In[24]:


obj_class3.test_class2()


# # Abstraction

# In[33]:


class pwskills:
    def student_details(self):
        pass
    def student_assignment(self):
        pass
    def student_marks(self):
        pass


# In[38]:


import abc 

class pwskills:
    
    def student_details(self):
        pass
    def student_assignment(self):
        pass
    def student_marks(self):
        pass


# In[39]:


import abc


class pwskills:
    
    @abc.abstractmethod
    def student_details(self):
        pass
    @abc.abstractmethod
    def student_assignment(self):
        pass
    @abc.abstractmethod
    def student_marks(self):
        pass


# In[40]:


class data_science(pwskills):
    def student_details(self):
        return"it will try to return a details of data science masters"
    def student_assignments(self):
        return"it will return a details of student assignment for data science masters"


# In[41]:


ds=data_science()
ds.student_details()


# In[52]:


class web_dev(pwskills):
    def student_details(self):
        return"it will try to return a details of web dev"
    def student_assignments(self):
        return"it will return a details of student assignment for data science masters"


# In[53]:


wb=web_dev()
wb.student_details()


# In[57]:


def test():
    print("this is the start of my fun")
    print(4+5)
    print("this is the end of my fun")


# In[58]:


test()


# In[59]:


def deco(func):
    def inner_deco():
        print("this is the start of my fun")
        func()
        print("this is the end of my fun")
    return inner_deco


# In[60]:


def test1():
    print(4+5)


# In[61]:


test1()


# In[66]:


@deco
def test1():
    print(4+5)


# In[67]:


test1()


# In[68]:


import time 
def timer_test(func):
    def timer_test_inner():
        start=time.time()
        func()
        end=time.time()
        print(end-start)
    return timer_test_inner


# In[69]:


def test2():
    print(45+67)


# In[70]:


test2()


# In[77]:


@timer_test
def test2():
    print(1234+5678)


# In[78]:


test2()


# In[79]:


@timer_test
def test3():
    for i in range(10000000):
        pass


# In[80]:


test3()


# In[ ]:




