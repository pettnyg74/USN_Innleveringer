# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:29:32 2025

@author: Petter Nygård
@mail pettnyg@gmail.com

"""
# #Oppgave 1
# #Regn ut alder basert på input
# from datetime import date

# #Ber om fødselsår
# alder = int(input('Hvilket år er du født?'))

# #Finner årstallet i dag
# dato = date.today()
# aarstall = int(dato.strftime("%Y"))
# #Regner ut alder uavhegig av dato
# alder = aarstall-alder

# print("Du er eller blir",  alder  ,"år nå i", aarstall)


#Oppgave 2
import math
# Regn ut antall pizzaer til oppgitt antall elever. Beregn 1/4 pizza pr elev
#Antall elever
antallElever = int(input("Skriv inn antall elever"))

#Antall hele pizzaer
pizzaer = int(math.ceil(antallElever/4))

print("Det må handles inn",pizzaer,"til festen.")


