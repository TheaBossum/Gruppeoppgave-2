# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:17:20 2024

@author: hegee
"""

#En del av oppgave g)
import datetime
import matplotlib.pyplot as plt

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

#Oppgave e)
# Initialiser lister for hver kolonne i filene
lufttemperatur_met = []
tid_met = []
lufttrykk_met = []
lufttemperatur= []
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
    
#Øving 10 oppgave a)   
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

#Oppgave f), g), h) og i)
# Plotting
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(tider_met_dt, lufttemperatur_met, label="Meterologisk")
plt.plot(tider_dt, temperatur, label="UiS")
plt.plot(gyldige_tider, gjennomsnitt, label="Gjennomsnittstemperatur")
plt.plot(temperaturfall_tider, temperaturfall_values, label="Temperaturfall Maksimal til Minimal")

#Øving 10 oppgave a)
plt.plot(temperaturfall_tider1, temperaturfall_values1, label = 'Temperaturfall fil 2')
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

#Øving 10 oppgave b)
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.hist(lufttemperatur_met, bins=range(int(min(lufttemperatur_met)), int(max(lufttemperatur_met)) + 1), color='skyblue', edgecolor='black', alpha=0.7, label='Meteorologiske målinger')
plt.xlabel('Temperatur (°C)')
plt.ylabel('Frekvens')
plt.title('Histogram av temperaturer fil 1')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(temperatur, bins=range(int(min(temperatur)), int(max(temperatur)) + 1), color='salmon', edgecolor='black', alpha=0.3, label='UiS målinger')
plt.xlabel('Temperatur (°C)')
plt.ylabel('Frekvens')
plt.title("Histogram av temperaturer fil 2")
plt.legend()
plt.show()

#Øving 10 oppgave c)
import numpy as np

def finn_og_plott_differanse(trykk_bar, trykk_abs):
    """
    Finner og plotter differansen mellom to lister, ekskluderer tomme strenger.
    Beregner glidende gjennomsnitt for å redusere støy.

    Args:
        trykk_bar (list): Liste med barometrisk trykk.
        trykk_abs (list): Liste med absolutt trykk.
    """

    # Finn indekser med gyldige verdier
    indekser_med_verdier = [i for i in range(len(trykk_bar)) if trykk_bar[i] != "" and trykk_abs[i] != ""]

    # Beregn differansen
    differanse = [abs(float(trykk_bar[i]) - float(trykk_abs[i])) for i in indekser_med_verdier]

    # Beregn glidende gjennomsnitt (vindu på 21)
    glidende_gjennomsnitt = np.convolve(differanse, np.ones(21)/21, mode='valid')

    # Plott resultatet
    plt.plot(indekser_med_verdier[10:-10], glidende_gjennomsnitt)
    plt.xlabel("Indeks")
    plt.ylabel("Gjennomsnittlig absolutt differanse")
    plt.title("Differanse mellom trykk, glidende gjennomsnitt")
    plt.show()


# Kall funksjonen
finn_og_plott_differanse(trykk_bar, trykk_abs)

#Øving 10 oppgave d)

sirdal_data = []
sauda_data = []
                                 

with open("temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt", "r") as fil:
    for linje in fil:
        data = linje.strip().split(";")
        sted = data[0]
        tid = data[2]
        lufttemp = data[3].replace(',', '.')
        lufttrykk = data[4].replace(",", ".")
        
        try: 
            tid_obj = datetime.datetime.strptime(tid, "%d.%m.%Y %H:%M")
            ny_tid = tid_obj.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue
       
        if sted == 'Sirdal - Sinnes':
           sirdal_data.append((ny_tid, float(lufttemp), float(lufttrykk)))
        elif sted == 'Sauda':
            sauda_data.append((ny_tid, float(lufttemp), float(lufttrykk)))
# Hente ut tid, temperatur og trykk fra Sirdal
sirdal_tid = [entry[0] for entry in sirdal_data]
sirdal_temp = [entry[1] for entry in sirdal_data]
sirdal_trykk = [entry[2] for entry in sirdal_data]

# Hente ut tid, temperatur og trykk fra Sauda
sauda_tid = [entry[0] for entry in sauda_data]
sauda_temp = [entry[1] for entry in sauda_data]
sauda_trykk = [entry[2] for entry in sauda_data] 

 
        
plt.figure(figsize=(10, 6))
plt.subplot(2,2,1)
plt.plot(sirdal_tid, sirdal_temp)
plt.plot(sauda_tid, sauda_temp)
plt.plot(tid_met, lufttemperatur_met)
plt.title('Temperatur')
plt.xlabel('Tid')
plt.ylabel('Temperatur (°C)')


plt.subplot(2,2,2)
plt.plot(sirdal_tid, sirdal_trykk)
plt.plot(sauda_tid, sauda_trykk)
plt.plot(tid_met, lufttrykk_met)
plt.title('Trykk')
plt.xlabel('Tid')
plt.ylabel('Trykk (hPa)')


plt.show()   
      

"""
Oppgave e
"""
# Lag liste med like tidspunkter, og lister for temperatur og trykk for disse tidspuntene
like_tidspunkter = list()
liste_temp_met = list()
liste_temp_runtime = list()
liste_trykk_met = list()
liste_trykk_runtime = list()

for index_tid_met, tid in enumerate(tid_met):
    tid_datetime = datetime.datetime.strptime(tid, "%Y-%m-%d %H:%M:%S")
    if tid_datetime.minute == 0 and tid in tid_bar:
        index_tid_bar = tid_bar.index(tid)
        
        like_tidspunkter.append(tid)
        liste_temp_met.append(lufttemperatur_met[index_tid_met])
        liste_trykk_met.append(lufttrykk_met[index_tid_met])
        liste_temp_runtime.append(temperatur[index_tid_bar])
        liste_trykk_runtime.append(trykk_bar[index_tid_bar])
        
# Beregne forskjeller og gjennomsnittlig forskjeller i temperatur mellom tidspunktene
forskjeller_temp = [abs(t1 - t2) for t1, t2 in zip(liste_temp_met,liste_temp_runtime)]
gjennomsnitt_forskjeller_temp = sum(forskjeller_temp) / len(forskjeller_temp)
print("Gjennomsnittlig forskjell for temperatur er ", gjennomsnitt_forskjeller_temp)

# Finn tidspunkt med høyest og lavest forskjell temperatur
min_diff_temp = min(forskjeller_temp)
max_diff_temp = max(forskjeller_temp)
tid_min_diff_temp = like_tidspunkter[forskjeller_temp.index(min_diff_temp)]
tid_max_diff_temp = like_tidspunkter[forskjeller_temp.index(max_diff_temp)]
print(f"Minste temperaturforskjell er {min_diff_temp} ved tid {tid_min_diff_temp} ")
print(f"Største temperaturforskjell er {max_diff_temp} ved tid {tid_max_diff_temp} ")

# Beregne forskjeller og gjennomsnitt forskjeller i trykk
forskjeller_trykk = [abs(p1 - p2) for p1, p2 in zip(liste_trykk_met, liste_trykk_runtime)]
gjennomsnitt_forskjeller_trykk = sum(forskjeller_trykk) / len(forskjeller_trykk)
print("Gjennomsnittlig forskjell for trykk er ", gjennomsnitt_forskjeller_trykk)

# Finn tidspunkt med høyest og lavest forskjell trykk        
min_diff_trykk = min(forskjeller_trykk)
max_diff_trykk = max(forskjeller_trykk)
tid_min_diff_trykk = like_tidspunkter[forskjeller_trykk.index(min_diff_trykk)]
tid_max_diff_trykk = like_tidspunkter[forskjeller_trykk.index(max_diff_trykk)]
print(f"Minste trykkforskjell er {min_diff_trykk} ved tid {tid_min_diff_trykk} ")
print(f"Største trykkforskjell er {max_diff_trykk} ved tid {tid_max_diff_trykk} ")        
        







