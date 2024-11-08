# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:16:37 2024

@author: Petter Nygård
@mail pettnyg@gmail.com

"""

kjoreLengde = 20000 # km pr aar
Trafikkforsikringsavgift = 8.38 # kr pr dag
dagerPrAar = 365

forsikringElbil = 5000 # kroner pr aar
forsikringBensinbil = 7500 # kroner pr aar

forbrukElbil = 0.2 # kwh/km
stromPris = 2.0 # kr pr kwh
forbrukBensinbil = 1.0 # kr pr km

bomavgiftElbil = 0.1 # kr pr km
bomavgiftBensinbil = 0.3 # kr pr km

# Felles utgifter
# Trafikkforikringsavgift
utgiftTrafikkforikringsavgift = Trafikkforsikringsavgift*dagerPrAar

# Elbil
#BompengeUtgifter
bompengeUtgifterElbil = bomavgiftElbil*kjoreLengde
#DrivstoffKostnad
drivstoffElbil = forbrukElbil*stromPris*kjoreLengde

#Bensinbil
#BompengeUtgifter
bompengeUtgifterBensinbil = bomavgiftBensinbil*kjoreLengde
#DrivstoffKostnad
drivstoffBensinbil = forbrukBensinbil*kjoreLengde

# Samlede utgifter ELBIL
totElbil =  utgiftTrafikkforikringsavgift + forsikringElbil + drivstoffElbil + bompengeUtgifterElbil

# Samlede utgifter BENSINBIL
totBensinbil = utgiftTrafikkforikringsavgift + forsikringBensinbil + drivstoffBensinbil + bompengeUtgifterBensinbil

# Output
#Kost elbil
print("Den årlige kostnaden for en elbil med årlig kjørelengde på", kjoreLengde,"km, er", round(totElbil,1), "kroner")
print("")
#Kost bensinbil
print("Den årlige kostnaden for en bensinbil med årlig kjørelengde på", kjoreLengde,"km, er", round(totBensinbil,1), "kroner")
print("")
#Sammenligning
if totElbil < totBensinbil:
    print("Elbil er rimeligst,", round(totBensinbil-totElbil,1), "kroner rimeligere.")
else:
    print("Bensinbil er rimeligst,", round(totElbil-totBensinbil,1), "kroner rimeligere.")





