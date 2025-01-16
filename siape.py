# API em Python que consulta os órgãos cadastrados no Sistema Integrado de Administração de Pessoal (SIAPE)

import requests
import json

#Filtros mínimos: Página (padrão = 1); Período de no máximo 1 mês;
     
url = "https://api.portaldatransparencia.gov.br/api-de-dados/orgaos-siape"

headers = {
    "accept": "*/*",
    "chave-api-dados": "0507f724c486e7ba57031f090c03f3aa"
}

params = {'pagina': '3'}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    siape = response.json()
    print(siape)

    
else:
    print(f"Erro: {response.status_code} - {response.text}")