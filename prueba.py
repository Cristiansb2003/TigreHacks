import requests
import csv
from datetime import datetime

# The API endpoint
municipios = ['apodaca','garcia','general-escobedo','guadalupe','juarez','monterrey','san-nicolas-de-los-garza','santa-catarina','santiago']

for m in municipios:
  url = "https://nuevoleon.opendatasoft.com/api/records/1.0/search/?dataset=indices-de-estadisticas-de-accidentes-viales-" + m + "&rows=10000"

  # A GET request to the API
  response = requests.get(url)
  # Print the response
  response_json = response.json()
  error = 0

  for i in response_json['records']:
    try:
      fecha = i['fields']['fecha']
      date_object = datetime.strptime(fecha, '%Y-%m-%d').date()
      day_object = date_object.strftime('%A')

      hora = i['fields']['hora']
      time_object = datetime.strptime(hora, '%H:%M:%S').time()

      reporte = [
        i['fields']['folio'],
        date_object,
        day_object,
        time_object,
        i['fields']['tipo_de_accidente'],
        i['fields']['georreferencia'][0],
        i['fields']['georreferencia'][1],
        m
      ]
    except:
      error = error + 1
    else:
      with open(r'reportes.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(reporte)
    
print(error)
