# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:21:20 2025
@author: Petter Nygård
@mail pettnyg@gmail.com
"""

import pandas as pd
import datetime
import matplotlib.pyplot as plt
#%%
#DEL A
#Lese inn kolonner til variabler
#Leser inn data fra fil
excelData = pd.read_excel("support_uke_24.xlsx")

#Henter data fra kolonne A-Ukedag
u_dag = excelData.loc[:,"Ukedag"]

#Henter data fra kolonne B-Klokkeslett
kl_slett = excelData.loc[:,"Klokkeslett"]

#Henter data fra kolonne C-Varighet
varighet = excelData.loc[:,"Varighet"]

#Henter data fra kolonne D-Tilfredshet
score = excelData.loc[:,"Tilfredshet"]

'''
print(u_dag)
print(kl_slett)
print(varighet)
print(score)
'''

#%%
#DEL B
#Finne antall henvendelser for ukedager. Visualiser med stolpediagram
#import numpy as np

mandager=0
tirsdager=0
onsdager=0
torsdager=0
fredager=0

#Løpe gjennom ukedager-kolonnen og sammenlikner verdi
for dag in u_dag:
    if dag.lower() =="mandag":
        mandager +=1
    if dag.lower() =="tirsdag":
        tirsdager +=1        
    if dag.lower() =="onsdag":
         onsdager+=1
    if dag.lower() =="torsdag":
        torsdager +=1        
    if dag.lower() =="fredag":
        fredager +=1

#arrays for plot
henvendelserelser =[mandager,tirsdager,onsdager,torsdager,fredager]
ukedager =['mandag','tirsdag','onsdag','torsdag','fredag']

#Generere plot og vise
plt.bar(ukedager,henvendelserelser)
plt.show()
#%%
#DEL C

#Finn og skriv ut lengste og korteste samtale
print("Lengste samtale varte: " ,varighet.max())
print("Korteste samtale varte:", varighet.min())

#%%
#DEL D
#regner ut gjennomsnittlig samtaletid basert på alle henvendelser i uke 24.

#Finne total samtalelengde
totalTid = datetime.timedelta()
for i in varighet:
    (h,m,s)= i.split(':')
    d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    totalTid+= d
    
#Finne antall samtaler
antallSamtaler = excelData["Varighet"].count()
gjSnittSamtale = totalTid/antallSamtaler
    
print("Gjennomsnittlig samtalelengde er:" ,gjSnittSamtale)

#%%
#DEL E
skift1=0 #08-10
skift2=0 #10-12
skift3=0 #12-14
skift4=0 #14-16

#Sjekk om aktuell tid er mellom to klokkeslett
def sjekkKlokkeslett(tid, start, slutt):
    if tid >start and tid < slutt:
        return True
    else:
        return False
        
#Løper gjennom kl_slett og finner tidspunkter og legger antall til hvert skift    
for k in kl_slett:
    if sjekkKlokkeslett(k, '08:00','10:00'):
        skift1 +=1
    if sjekkKlokkeslett(k, '10:00','12:00'):    
        skift2 +=1
    if sjekkKlokkeslett(k, '12:00','14:00'):
        skift3 +=1
    if sjekkKlokkeslett(k, '14:00','16:00'):
        skift4 +=1
        
        
        
        
print("Skift 1:",skift1)
print("Skift 2:",skift2)
print("Skift 3:",skift3)
print("Skift 4:",skift4)

print("TOT: ", (skift1+skift2+skift3+skift4))
    
    
    
#arrays for plot
skift=[skift1,skift2,skift3,skift4]
labels=['08-10','10-12','12-14','14-16']

#Generere plot og vise
colors = ['blue','red','green','yellow']
plt.pie(skift,colors=colors, labels=labels, startangle=60, autopct='%1.1f%%')
plt.show()

#%%
#DEL F
scoreNegativ=0 #1-6
scoreNoytral=0 #7-8
scorePositiv=0 #9-10
def tilfreds(verdi,lav,hoy):
    if verdi>=lav and verdi<=hoy:
        return True
    else:
        return False
    
for t in score:
    if tilfreds(t, 1, 6):
        scoreNegativ +=1
    if tilfreds(t, 7, 8):
        scoreNoytral +=1
    if tilfreds(t, 9, 10):
        scorePositiv +=1


antallTilbakemeldinger = scoreNegativ+scoreNoytral+scorePositiv
print("Negative:",scoreNegativ)
print("Nøytrale:",scoreNoytral)
print("Positive:",scorePositiv)

print("Antall Tilbakemeldinger:", antallTilbakemeldinger)


NPS = (scorePositiv/antallTilbakemeldinger*100)-(scoreNegativ/antallTilbakemeldinger*100)

print("MORSE sin NPS er:", round(NPS,2))
antInnst=[scorePositiv,scoreNoytral,scoreNegativ]
innst=["positiv","nøytral","negativ"]



#Generere plot og viser resultat
colors2 = ['blue','red','green','yellow']
plt.pie(antInnst,colors=colors2, labels=innst, startangle=0, autopct='%1.1f%%')
plt.show()
