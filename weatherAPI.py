import pandas as pd
from datetime import datetime
import time
<<<<<<< Updated upstream


accidenteclima = open("ReporteClima.csv","a")
=======
import csv
import sys
import pendulum
import pymysql

#accidenteclima = open("ReporteClima.csv","a")
>>>>>>> Stashed changes
climaApodaca = open("Clima_apodaca.csv", "r")

def openClima(): 
    climaApodaca = open("Clima_apodaca.csv", "r")
    for i in range(4):
        climaApodaca.readline()
    clima = climaApodaca.readline().split(",")
    return clima

<<<<<<< Updated upstream
data = pd.read_csv('reportes.csv', encoding = "ISO-8859-1")
climaApodacas = pd.read_csv("Clima_apodaca.csv",encoding = "ISO-8859-1")
print(data.columns)
print(climaApodacas.columns)
print(climaApodacas["time"][0])
i = 0
for row in range(0,10):
  fecha = data.iloc[row,1]  
  date_object = datetime.strptime(fecha, "%m/%d/%Y").date()
  hour = datetime.strptime(data.iloc[row,3], "%H:%M:%S").time()
  fecha = str(date_object.strftime("%Y-%m-%d") + "T" + hour.strftime('%H')+":00")
=======
data = pd.read_csv('reporte.csv', encoding = "UTF-8")
climaApodacas = pd.read_csv("Clima_apodaca.csv",encoding = "ISO-8859-1")
print(data.value_counts())
print(data.columns)

print(climaApodacas["time"][0])
i = 0
for row in range(58278):

  fecha = data.iloc[row,1]  
  print(fecha)


  date_object = datetime.strptime(fecha, "%m/%d/%Y").date()
  hour = datetime.strptime(data.iloc[row,3], "%H:%M:%S").time()
  fecha = str(date_object.strftime("%Y-%m-%d") + "T" + hour.strftime('%H')+":00")
  print("--------------------------")
>>>>>>> Stashed changes
  while climaApodacas["time"][i] != fecha:
     #print(hour)
     #print(fecha)
     #print(climaApodacas["time"][i])
<<<<<<< Updated upstream
     i+=1
     time.sleep(0.1)
  f = (  
     data['2929'][row],
=======
     print(i)
     i+=1
     #time.sleep(1.1)
  fa = (  
     data['a'][row]+fecha,
>>>>>>> Stashed changes
     fecha,
     climaApodacas["temperature_2m (Â°C)"][i],
     climaApodacas["relativehumidity_2m (%)"][i],
     climaApodacas["precipitation (mm)"][i],
     climaApodacas["rain (mm)"][i],
<<<<<<< Updated upstream
     data['Thursday'][row],
     data['Alcance Con Estrellamiento'][row],
     data['25.77451'][row],
     data['-100.193782'][row] )
  
  accidenteclima.write(f)

  i-=23
=======
     data['c'][row],
     data['f'][row],
     data['g'][row],
     data['h'][row] )
  
  with open('ReporteClima.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fa)


  i-=24
>>>>>>> Stashed changes
  if (i < 0): i = 0


