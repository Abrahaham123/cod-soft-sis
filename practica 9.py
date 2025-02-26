#!/usr/bin/env python
# coding: utf-8

# In[9]:


for i in range(0,9):
    print(i)


# In[11]:


for  i in range(1, 21, 2):
    print(i)


# In[15]:


for i in range(10, 0,-1):
   print(i)


# In[17]:


numero=int (input("Ingresa el numero que deseas multiplicar"))
for i in range(1,11):
    print(i ," x ",numero, " = ",i * numero)


# In[31]:


numero="1234567890"
contador=1
numero=input("Ingresa el numero")
numero2=list(numero)
for numero3 in numero2:
     contador += int (numero)*contador
     print("Producto ",contador)


# In[ ]:




