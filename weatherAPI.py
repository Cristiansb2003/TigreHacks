import pandas as pd
from datetime import datetime
import time


accidenteclima = open("ReporteClima.csv","a")
climaApodaca = open("Clima_apodaca.csv", "r")

def openClima(): 
    climaApodaca = open("Clima_apodaca.csv", "r")
    for i in range(4):
        climaApodaca.readline()
    clima = climaApodaca.readline().split(",")
    return clima

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
  while climaApodacas["time"][i] != fecha:
     #print(hour)
     #print(fecha)
     #print(climaApodacas["time"][i])
     i+=1
     time.sleep(0.1)
  f = (  
     data['2929'][row],
     fecha,
     climaApodacas["temperature_2m (Â°C)"][i],
     climaApodacas["relativehumidity_2m (%)"][i],
     climaApodacas["precipitation (mm)"][i],
     climaApodacas["rain (mm)"][i],
     data['Thursday'][row],
     data['Alcance Con Estrellamiento'][row],
     data['25.77451'][row],
     data['-100.193782'][row] )
  
  accidenteclima.write(f)

  i-=23
  if (i < 0): i = 0


