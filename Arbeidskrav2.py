# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:29:32 2025

@author: Petter Nygård
@mail pettnyg@gmail.com

"""
#Oppgave 1
#Regn ut alder basert på input
from datetime import date

#Ber om fødselsår
alder = int(input('Hvilket år er du født?'))

#Finner årstallet i dag
dato = date.today()
aarstall = int(dato.strftime("%Y"))
#Regner ut alder uavhegig av dato
alder = aarstall-alder

print("Du er eller blir",  alder  ,"år nå i", aarstall)


#Oppgave 2
import math
# Regn ut antall pizzaer til oppgitt antall elever. Beregn 1/4 pizza pr elev
#Antall elever
antallElever = int(input("Skriv inn antall elever:"))

#Regner ut antall hele pizzaer
pizzaer = int(math.ceil(antallElever/4))

print("Det må handles inn",pizzaer,"til festen.")

#Oppgave 3
#Regn om fra grader til radianer
import numpy as np
#Oppgi antall grader
v_grad = float(input("Skriv inn gradtallet:"))

#Omregning til Radianer
v_rad = v_grad*np.pi/180

print(v_grad,"grader tilsvarer",v_rad,"radianer.")

#Oppgave 4
#a)
#Opprett dictionary
data = {"Norge":["Oslo", 0.634], "England": ["London", 8.982], "Frankrike": ["Paris", 2.161], "Italia": ["Roma", 2.873]}

#b)
#Gi ut info om land som tastes inn
#Ber om landet

finnLand = str(input("Skriv inn et land:"))

def hentLand(land):
    if data.get(land) is not None:

        landInfo = data.get(land)
        hovedstad = landInfo[0]
        innbyggere = str(landInfo[1])
        out =  str(hovedstad)+" er hovedstaden i "+ land +", og det er "+innbyggere+" mill. innbyggere i "+ hovedstad
        
    
    else:
        out = "Kunne ikke finne landet du spurte etter.Har du husket stor forbokstav?"
    
    return out
    

print(hentLand(finnLand))


#c)
#Legg til nytt land med hovedstad og innbyggerantall
nyttLand = str(input("Legg til et land:"))
nyHovedstad = str(input("Hva er hovedstaden?:"))
nyttInnbyggerantall = str(input("Antall innbyggere i hovedstaden?:"))
#Oppdaterer dictionary
data.update({nyttLand: [nyHovedstad,nyttInnbyggerantall]})

#Print oppdatert dictionary til skjerm
for x,y in data.items():
    print(x,y[0],y[1])

#Oppgave 5
#Lag funksjon som regner ut areal og omkrets på figur.
#Args, diameter på sirkel og lengste katet i trekant
import math
def arealOmkretsFigur(a,b):
    arealSirkel = math.pi*math.pow(a, 2) 
    arealTrekant = (b*a/2)
    #areal av figur
    arealFigur = (arealSirkel/2)+arealTrekant
    
    omkretsSirkel=2*math.pi*a
    hypotenusTrekant=math.sqrt(math.pow(a, 2)+math.pow(b, 2))
    #omkrets av figur
    omkretsFigur = (omkretsSirkel/2)+(b+hypotenusTrekant)

    return arealFigur,omkretsFigur


result = arealOmkretsFigur(5, 4)

print("På gitt figur med a=5 og b=4, er arealet "+str(result[0])+"og omkretsen er "+str(result[1]))



#Oppgave 6
#Plott funksjonen 𝑓(𝑥) = −𝑥2 − 5, for x på intervallet [-10,10]
