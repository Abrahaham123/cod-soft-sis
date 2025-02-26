#practica 8 
#esaú 25/02/25
#2J


#!/usr/bin/env python
# coding: utf-8

# In[3]:


monumentos={
    "Delhi":"Red fort",
    "Paris":"Torre Eifel",
    "Nueva york":"Estatua de la libertad",
    "Rio de janeiro":"Cristo redentor"

}
ciudad=input("Ingresa el nombre de la ciudad")
print("El monumento es ", monumentos[ciudad])


# In[9]:


edad = float(input("Igresa la edad que deseas saber si es posible votar"))
if edad >= 18:
    print("es posible votar")
else:
    print("Eres menor de edad, no puedes votar")


# In[19]:


numero1=input("Ingresa el primer numero")
numero2=input("Ingresa el ssegundo numero")
if numero1>numero2:
    print(numero1,"es mayor que",numero2)
elif numero2>numero1:
  print(numero2,"es mayor que",numero1)


# In[31]:


edades=[]
edad1=int(input("ingresa tu edad"))
edades.append(edad1)
edad2=int(input("ingresa tu edad"))
edades.append(edad2)
edad3=int(input("ingresa tu edad"))
edades.append(edad3)
edad4=int(input("ingresa tu edad"))
edades.append(edad4)

print("La edad menor es",min(edades))


# In[ ]:




