import requests


codeUSD= "USD-BRL"
codeARS = "ARS"
codeETH = "ETH"

link =f"https://economia.awesomeapi.com.br/all/{codeUSD}"
requisicao = requests.get(link)
dicRequisicao = requisicao.json()

valorCode = dicRequisicao["USD"]
valorMoeda = valorCode['high']
nomeMoeda = valorCode ['name']
print(nomeMoeda,":")
print(valorMoeda)



link =f"https://economia.awesomeapi.com.br/all/{codeARS}"
requisicao = requests.get(link)
dicRequisicao = requisicao.json()
valorCode = dicRequisicao["ARS"]
valorMoeda = valorCode['high']
nomeMoeda = valorCode ['name']
print(nomeMoeda,":")
print(valorMoeda)



link =f"https://economia.awesomeapi.com.br/all/{codeETH}"
requisicao = requests.get(link)
dicRequisicao = requisicao.json()

valorCode = dicRequisicao["ETH"]
valorMoeda = valorCode['high']
nomeMoeda = valorCode ['name']
print(nomeMoeda,":")
print(valorMoeda)


