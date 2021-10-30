""" Este script é um exemplo do uso da biblioteca request(requisições) em um site siscomex,o arquivo requisitado
 é no formato json,um arquivo com funcionalidades parecidas com um dicionário."""

# catalogo de produtos

import requests

catalogoprod = requests.get("https://val.portalunico.siscomex.gov.br/catp/api/ext/produto")
catalogoprod = catalogoprod.json()
catalogo_produto = catalogoprod['info']  # ['visao']
# print(catalogoprod)
print(catalogo_produto)
