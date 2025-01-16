## API em Python que consulta todos os servidores do Poder Executivo Federal


import requests
import json

#Filtros mínimos: Página (padrão = 1); Código Órgão Lotação (SIAPE) OU Código Órgão Exercício (SIAPE) OU CPF;

# URL da API
url = "https://api.portaldatransparencia.gov.br/api-de-dados/servidores"

# Cabeçalhos da requisição, incluindo a chave da API
headers = {
    "accept": "*/*",
    "chave-api-dados": "0507f724c486e7ba57031f090c03f3aa"
}

params = {'orgaoServidorExercicio': '13000', 'pagina': '1'}

# Fazendo a requisição GET com os cabeçalhos
response = requests.get(url, headers=headers, params=params)

# Verificando o status da resposta
if response.status_code == 200:
    servidores = response.json()  #Traz as informações em json para o python
    print(servidores)
else:
    print(f"Erro: {response.status_code} - {response.text}")