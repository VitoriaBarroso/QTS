import requests

link = f"http://api.tempo.com/index.php?api_lang=br&localidad=12996&affiliate_id=tk99un15usak&v=3.0"

requisicao = requests.get(link)
dicRequisicao = requisicao.json()
print(dicRequisicao)
for valor in dicRequisicao['day'].values():
    print("Data:", valor['date'])
    print("Dia da semana:",valor['name'])
    print("Descrição do Tempo:",valor['symbol_description'])
    print("Temperatura Minima e Maxima:",valor['symbol_description2'])
    print("Humidades relativa do ar:",valor['humidity'])
    print("Nascer do sol:",valor['sun']['in'])
    print("Por do sol:",valor['sun']['out'])
    print("Fases da lua:",valor['moon']['desc'])
    print()

