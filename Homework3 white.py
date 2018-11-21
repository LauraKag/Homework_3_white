# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 22:31:59 2018

@author: laura
"""
#%%
#Create a Student class that has the following attributes:

#name
#last name
#age
#master (either MCSBT or MDBI)
#Make sure you parametrize all those fields in the constructor.

class Class:
    def __init__(self,name,lastname,age,master):
        self.name=name
        self.lastname=lastname
        self.age=age
        self.master=master
    
alejandro=Class("Alejandro", "Meneses", "27", "MCSBT")
agata=Class("Agata", "Kaczmarek", "31","MDBI")
anastasia=Class("Anastasia", "Lasunina", "25", "MDBI")
anniken=Class("Anikken", "Barstad Gjeruldsen", "27", "MDBI")
candela=Class("Candela", "Noya", "24", "MDBI")
daniil=Class("Daniil", "Osipov", "21", "MDBI")
david=Class("David", "Barrero Gonzalez", "31", "MCSBT")
edem=Class("Edem", "Francois", "28", "MCSBT")
eduardo=Class("Eduardo", "Paraja", "23", "MDBI")
florian=Class("Florian", "Diegruber", "25", "MCSBT")
hannah=Class("Hannah", "Oldorf", "23", "MCBT")
isabella=Class("Isabella", "Rosenthal", "27", "MDBI")
javier=Class("Javier", "Fernandez", "24", "MCSBT")
lukas=Class("Lukas", "Hauser", "28","MDBI")
leila=Class("Leila", "Tazi", "27", "MCSBT")
laura=Class("Laura", "Kageneck", "23", "MCSBT")
monica=Class("Monica", "Alvarenga","28", "MDBI")
natalie=Class("Natalie", "Cedeno", "26", "MDBI")
octacio=Class("Octavio", "Ramírez", "28", "MDBI")
tancredi=Class("Tancredi", "Bernard", "21", "MCSBT")
yasmine=Class("Yasmine", "Lyagoubi", "23", "MDBI")

#Example
print(agata.name)





