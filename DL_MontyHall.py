
# coding: utf-8

# In[1]:


import numpy as num 
import random 


# In[6]:


#Funcion que definira lo que hay dentro de las puertas
def sort_doors():
    a = ['goat', 'goat', 'car']
    #Se usa la funcion random.shuffle para desordenar la lista
    return random.shuffle(a)
print (sort_doors())


# In[10]:


#Funcion para escoger la puerta aleatoriamente
def choose_door():
    #Se usa la funcion random.randrange para deolver un numero aleatorio
    return random.randrange(3)
print (choose_door())


# In[ ]:


#Funcion que revelara lo que hay detras de a puerta
def reveal_door(lista, choice):
    for i in range(len(lista)):
        #Cuando la posicion sea distinta de la posicion actual cambiar el valor por el de cabra
        if i != choice:
            if lista[i] == 'goat':
                lista[i] = 'GOAT_MONTY'
                return lista
                break


# In[ ]:


#Funcion que definira si el jugador cambio o no cambio de puerta
def finish_game(lista, choice, change):
    if change == 'False':
        return lista[choice]
    else:
        for i in range(len(lista)):
            a = lista[choice]
            if lista[i] == 'GOAT_MONTY':
                b = lista[i]
            lista.remove(b)
            lista.remove(a)
        return lista

