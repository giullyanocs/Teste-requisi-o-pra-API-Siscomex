""" Este script é um exemplo do uso da biblioteca request(requisições) em um site siscomex,o arquivo requisitado
 é no formato json,um arquivo com funcionalidades parecidas com um dicionário."""

# documentos da operação

import requests
import json

res = requests.get('https://portalunico.siscomex.gov.br/edocex/api/ext/tipos-documentos-operacao/DI')
print(res)
json = res.json()
print(json)
