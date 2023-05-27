import requests

# The API endpoint
municipios = ['apodaca','garcia','general-escobedo','guadalupe','juarez','monterrey','san-nicolas-de-los-garza','santa-catarina','santiago']
reportes = []

for m in municipios:
  url = "https://nuevoleon.opendatasoft.com/api/records/1.0/search/?dataset=indices-de-estadisticas-de-accidentes-viales-" + m + "&rows=1"

  # A GET request to the API
  response = requests.get(url)
  # Print the response
  response_json = response.json()

  for i in response_json['records']:
    reportes.append({
        "folio": (i['fields']['folio']),
        "fecha": (i['fields']['fecha']),
        "dia": (i['fields']['dia']),
        "hora": (i['fields']['hora']),
        "tipo_de_accidente": (i['fields']['tipo_de_accidente']),
        "latitud": (i['fields']['georreferencia'][0]),
        "longitud": (i['fields']['georreferencia'][1]),
        "municipio": m
    })