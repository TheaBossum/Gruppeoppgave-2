# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:04:49 2024

@author: pegus
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:01:35 2024

@author: sara
"""

#En del av oppgave g)
import math
import datetime
import matplotlib.pyplot as plt

# Funksjoner
# Funksjon for gyldige tidspunkter og moving averages
def averages_avvik(liste_tidspunkter, liste_temperaturer, n):
    # Finn gyldige tidspunkter
    gyldige_tidspunkter = []
    moving_averages = []
    moving_std_avvik = []
    
    # Finn moving average og std_avvik
    for i in range(n, len(liste_temperaturer)-n):
        window = liste_temperaturer[i-n:i+n+1]
        # Beregn gjennomsnitt
        average = round(sum(window) / len(window),2)
        # Beregn std_avvik
        sum_avvik = 0
        for y in window:
            sum_avvik += (y-average)**2
        std_avvik = round(math.sqrt(sum_avvik/(len(window)-1)), 2)
        # Fyll listene 
        moving_averages.append(average)
        moving_std_avvik.append(std_avvik)
        gyldige_tidspunkter.append(liste_tidspunkter[i])
    return gyldige_tidspunkter, moving_averages, moving_std_avvik 
"""
#Lager et funksjon for å finne et glidende gjennomsnitt for et gitt temperatur-datasett over en spesifikk tidsperiode
def glidende_gjennomsnitt(tid, temperatur, n):
    gyldige_tider = []
    gjennomsnitt =[]

    for i in range(n, len(temperatur)-n):
        temp_slice = temperatur[i - n:i + n + 1]
        gjennomsnitt_verdi = sum(temp_slice) / len(temp_slice)

        gyldige_tider.append(tid[i])
        gjennomsnitt.append(gjennomsnitt_verdi)

    return gyldige_tider, gjennomsnitt
"""

#Oppgave e)
# Initialiser lister for hver kolonne i filene

# Lister for Meteriologisk
lufttemperatur_met = []
tid_met = []
lufttrykk_met = []
lufttemperatur= []

# Lister for UIS
tid= []
temperatur = []
tid_bar = []
trykk_abs = []
trykk_bar=[]

# Fyll listene for fil1
with open("temperatur_trykk_met_samme_rune_time_datasett.csv.txt", "r") as fil: #Åpner og leser av fil
    for linje in fil:
        data = linje.strip().split(";")
        if len(data)>=5:
            tiden=data[2]  
            temperaturen= data[3].replace(',', '.')
            trykk= data[4].replace(",",".")
            try:
                if "am" in tiden or "pm" in tiden:      #Tar hensyn til pm og am
                    dato_obj = datetime.datetime.strptime(tiden, "%d/%m/%Y %I:%M:%S %p") 
                else:
                    dato_obj = datetime.datetime.strptime(tiden, "%d.%m.%Y %H:%M")
                
                tid_standard = dato_obj.strftime("%Y-%m-%d %H:%M:%S")
                lufttemperatur_float= float(temperaturen)
                lufttrykk_float= float(trykk)
                tid_met.append(tid_standard)
                lufttemperatur_met.append(lufttemperatur_float)
                lufttrykk_met.append(lufttrykk_float)
            except ValueError:
                pass

# Fyll listene for fil2
with open("trykk_og_temperaturlogg_rune_time.csv.txt", "r") as fil:
    for linje in fil:
        data = linje.strip().split(";")
        if len(data) >= 5:
            # Hent dato og tid
            tiden=data[0]
            # Hent verdier og erstatt komma med punktum
            trykk_baro= data[2].replace(",", ".")
            trykk_abso= data[3].replace(",", ".")
            temperaturen= data[4].replace(",", ".")
        
        # Sjekk om barometertrykk er en tom streng
            if trykk_baro == (''):
                try:
                   if "am" in tiden or "pm" in tiden:    #Tar hensyn til pm og am
                       if " 00:" in tiden:
                           tiden = tiden.replace("00:", "12:", 1)
                       dato_obj = datetime.datetime.strptime(tiden, "%m/%d/%Y %I:%M:%S %p")
                   else:
                       dato_obj = datetime.datetime.strptime(tiden, "%m.%d.%Y %H:%M")
                   
                   tid_standard = dato_obj.strftime("%Y-%m-%d %H:%M:%S")
                   temperatur_float = float(temperaturen)
                   trykk_abs_float = float(trykk_abso) * 10
                   
                   tid.append(tid_standard)
                   temperatur.append(temperatur_float)
                   trykk_abs.append(trykk_abs_float)
                except ValueError:
                    pass
            else:
                try:
                    if "am" in tiden or "pm" in tiden:      #Tar hensyn til pm og am
                       if " 00:" in tiden:
                           tiden = tiden.replace("00:", "12:", 1)
                       dato_obj = datetime.datetime.strptime(tiden, "%m/%d/%Y %I:%M:%S %p")
                    else:
                       dato_obj = datetime.datetime.strptime(tiden, "%m.%d.%Y %H:%M")
                   
                    tid_standard = dato_obj.strftime("%Y-%m-%d %H:%M:%S")
                    temperatur_float=float(temperaturen)
                    trykk_abs_float=float(trykk_abso)*10
                    trykk_bar_float=float(trykk_baro)*10
                   
                    trykk_bar.append(trykk_bar_float)
                    tid_bar.append(tid_standard)
                    tid.append(tid_standard)
                    temperatur.append(temperatur_float)
                    trykk_abs.append(trykk_abs_float)
                except ValueError:
                # Hopp over linjer som ikke kan konverteres til float
                    pass
tider_met_dt = [datetime.datetime.strptime(tiden, "%Y-%m-%d %H:%M:%S") for tiden in tid_met]
tider_dt = [datetime.datetime.strptime(tiden, "%Y-%m-%d %H:%M:%S") for tiden in tid]
tider_baro_dt = [datetime.datetime.strptime(tiden, "%Y-%m-%d %H:%M:%S") for tiden in tid_bar]

# Finn glidende gjennomsnitt og standardavvik for UIS-målingene
gyldige_tider_uis, gjennomsnitt_uis, std_avvik_uis = averages_avvik(tider_dt, temperatur, 10)

"""
#Bruker funksjon laget for oppgave g)
n=30
gyldige_tider, gjennomsnitt = glidende_gjennomsnitt(tider_dt, temperatur, n)


#En del av oppgave h)
start_tid = datetime.datetime(2021, 6, 11, 17, 31)
slutt_tid = datetime.datetime(2021, 6, 12, 3, 5)

temperaturer_uis_filtered = []
tider_uis_filtered = []

for tiden, temperaturen in zip(tider_dt, temperatur):
    if start_tid <= tiden <= slutt_tid:
        tider_uis_filtered.append(tiden)
        temperaturer_uis_filtered.append(temperaturen)

if temperaturer_uis_filtered:
    max_temp = max(temperaturer_uis_filtered)
    min_temp = min(temperaturer_uis_filtered)

    temperaturfall_tider = [start_tid, slutt_tid]
    temperaturfall_values = [max_temp, min_temp]
else:
    temperaturfall_tider = []
    temperaturfall_values = []
    
    
start_tid1 = datetime.datetime(2021, 6, 11, 17, 31)
slutt_tid1 = datetime.datetime(2021, 6, 12, 3, 5)

temperaturer_uis_filtered1 = []
tider_uis_filtered1 = []


for tiden, temperaturen in zip(tider_met_dt, lufttemperatur_met):
    if start_tid1 <= tiden <= slutt_tid1:
        tider_uis_filtered1.append(tiden)
        temperaturer_uis_filtered1.append(temperaturen)

if temperaturer_uis_filtered:
    max_temp1 = max(temperaturer_uis_filtered1)
    min_temp1 = min(temperaturer_uis_filtered1)

    temperaturfall_tider1 = [start_tid1, slutt_tid1]
    temperaturfall_values1 = [max_temp1, min_temp1]
    
    
else:
    temperaturfall_tider1 = []
    temperaturfall_values1 = []  
"""

#Oppgave f), g), h) og i)
# Plotting
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(tider_met_dt, lufttemperatur_met, label="Meterologisk")
plt.plot(tider_dt, temperatur, label="UiS")
plt.plot(gyldige_tider_uis, gjennomsnitt_uis, label="Gjennomsnittstemperatur") # Plotter gjennomsnittsverdier
plt.plot(gyldige_tider_uis, std_avvik_uis, label="Std.avvik")
#plt.plot(temperaturfall_tider, temperaturfall_values, label="Temperaturfall Maksimal til Minimal")
#plt.plot(temperaturfall_tider1, temperaturfall_values1, label = 'Temperaturfall fil 2')
plt.xlabel("Tid")
plt.ylabel("Temperatur")
plt.legend()


plt.subplot(2, 1, 2)
plt.plot(tider_met_dt, lufttrykk_met, label = "Absoluttrykk MET")
plt.plot(tider_dt, trykk_abs, label = "Absoluttrykk")
plt.plot(tider_baro_dt, trykk_bar, label = "Barometrisk trykk")
plt.xlabel("Tid")
plt.ylabel("Trykk")
plt.legend()
plt.tight_layout()
plt.show()

"""
#sammenslåtte_temperaturer = []
#sammenslåtte_temperaturer.append(lufttemperatur_met)
#sammenslåtte_temperaturer.append(temperatur)

#plt.hist(sammenslåtte_temperaturer)

plt.subplot(1, 2, 1)
plt.hist(lufttemperatur_met, bins=range(int(min(lufttemperatur_met)), int(max(lufttemperatur_met)) + 1), color='skyblue', edgecolor='black', alpha=0.7, label='Meteorologiske målinger')
plt.subplot(1, 2, 2)
plt.hist(temperatur, bins=range(int(min(temperatur)), int(max(temperatur)) + 1), color='salmon', edgecolor='black', alpha=0.3, label='UiS målinger')


plt.xlabel('Temperatur (°C)')
plt.ylabel('Frekvens')
plt.title('Histogram av temperaturer fra begge datasett')
plt.legend()
plt.show()


#2d)

tid_sirdal = []
lufttemp_sirdal = []
lufttrykk_sirdal = []
tid_sauda = []
lufttemp_sauda = []
lufttrykk_sauda = []

with open("temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt", "r") as fil:
    for linje in fil:
        data = linje.strip().split(";")
        if "-" in data:
            sted1 = data[0]
            tid1 = data[2]
            lufttemp1 = data[3]
            lufttrykk1 = data[4]
        else:
           sted2 = data[0]
           tid2 = data[2]
           lufttemp2 = data[3]
           lufttrykk2 = data[4] 
           
           tid_sirdal.append(tid1) 
           lufttemp_sirdal.append(lufttemp1)
           lufttrykk_sirdal.append(lufttrykk1)
           tid_sauda.append(tid2) 
           lufttemp_sauda.append(lufttemp2)
           lufttrykk_sauda.append(lufttrykk2)
            
        
        
        try:
            if "am" in tiden or "pm" in tiden:      #Tar hensyn til pm og am
                dato_object = datetime.datetime.strptime(tiden, "%d/%m/%Y %I:%M:%S %p") 
            else:
                dato_object = datetime.datetime.strptime(tiden, "%d.%m.%Y %H:%M")
        except ValueError:
            pass
        
        

           
 tid_standard = dato_obj.strftime("%Y-%m-%d %H:%M:%S")
            lufttemperatur_float= float(temperaturen)
            lufttrykk_float= float(trykk)
            tid_met.append(tid_standard)
            lufttemperatur_met.append(lufttemperatur_float)
            lufttrykk_met.append(lufttrykk_float)
        

plt.plot()
"""









