""" Este script é um exemplo do uso da biblioteca request(requisições) em um site siscomex,o arquivo requisitado
 é no formato json,um arquivo com funcionalidades parecidas com um dicionário."""

# documentos da operação

import requests

res = requests.get('https://val.portalunico.siscomex.gov.br/catp/api/ext/produto/ext/fabricante/exportar/02069421503')
print(res)
#res = res.json()
#print(res)
#rest = res['']['']
#print(rest)

