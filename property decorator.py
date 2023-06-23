#!/usr/bin/env python
# coding: utf-8

# In[1]:


class pwskills:
    def student_details(self,name,mail_id,number):
        print(name,mail_id,number)


# In[3]:


pw=pwskills()


# In[4]:


pw.student_details("sagar","sagar318@gmail.com",1234567890)


# In[15]:


class pwskills1:
    def student_details(self,name,mail_id,number):
        print(name,mail_id,number)
        
    @staticmethod
    def mentor_class(list_mentor):
        print(list_mentor)
        
    def mentor(self,mentor_list):
        print(mentor_list)


# In[9]:


pw1=pwskills1()


# In[10]:


pwskills1.mentor_class(["sagar","krish"])


# In[11]:


pw1.mentor_class(["sagar","sudh"])


# In[16]:


pwskills1.mentor_class(["sagar","sudh"])


# In[21]:


class pwskills1:
    def student_details(self,name,mail_id,number):
        print(name,mail_id,number)
    @staticmethod
    def mentor_mail_id(mail_id):
        print(mail_id)
        
    @staticmethod
    def mentor_class(list_mentor):
        print(list_mentor)
        pwskills1.mentor_mail_id(["sagards318@gmail.com","sudh@gmail.com"])
    @classmethod
    def class_name(cls,slass_name):
        cls.mentor_class(["sagar","sudh"])
    def mentor(self,mentor_list):
        print(mentor_list)
        self.mentor_class(["sagar","sudh"])


# In[23]:


pw1=pwskills1()


# In[24]:


pw1.student_details("mohan","mohan@gmail.com","1234567890")


# In[26]:


pw1.mentor_mail_id(["sagards318@gmailcom","dbddns@gmail.com"])


# In[27]:


pw1.class_name("data_science_masters")


# In[28]:


pwskills1.mentor_mail_id(["sagar@gmail.com","fwejnsji@gmail.com"])


# In[ ]:





# # special(magic or dunder)

# In[29]:


dir(int)


# In[30]:


a=10


# In[31]:


a+5


# In[32]:


a.__add__(6)


# In[33]:


dir(str)


# In[35]:


class pwskills:
    def __init__(self):
        print("this is my init")


# In[37]:


pw=pwskills()


# In[38]:


class pwskills:
    def __new__(cls):
        print("this is my new")
    def __init__(self):
        print("this is my init")


# In[39]:


pw=pwskills()


# In[50]:


class pwskills1:
    def __init__(self):
        self.mobile_number=1234567890
        
    def __str__(self):
        return"this is a magic method which will print somthing for object"


# In[51]:


pw1=pwskills1()


# In[52]:


pw1


# In[53]:


print(pw1)


# In[54]:


dir(dict)


# In[56]:


dir(tuple)


# In[ ]:





# # property decorator

# In[67]:


class pwskills:
    def __init__(self,course_price,course_name):
        self.__course_price=course_price
        self.course_name=course_name


# In[68]:


pw=pwskills(3500,"data science masters")


# In[69]:


pw.course_name


# In[70]:


pw.course_price


# In[73]:


pw._pwskills__course_price


# In[90]:


class pwskills:
    def __init__(self,course_price,course_name):
        self.__course_price=course_price
        self.course_name=course_name
    @property
    def course_price_access(self):
        return self.__course_price
    @course_price_access.setter
    def course_price_set(self,price):
        if price <=3500:
            pass
        else:
            self._course_price=price
            
        @course_price_access.deleter
        def course_price_del(self):
            del self._course_price
##  _=private
## __=protected


# In[75]:


pw=pwskills(3500,"data science masters")


# In[76]:


pw.course_price_access


# In[84]:


pw.course_price__set=2300


# In[80]:


pw.course_name


# In[85]:


pw.course_price_access


# In[88]:


pw.course_price__set=4500


# In[89]:


pw.course_price_access


# In[94]:


del pw.course_price_del


# In[ ]:




