from extratorArgumentosUrlBytebank import ExtratorArgumentosUrlBytebank

url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&valor=1500"

# print(ExtratorArgumentosUrl.urlEhValida(url))

url1 = ExtratorArgumentosUrlBytebank(url)
url2 = ExtratorArgumentosUrlBytebank(url)
print(url1 == url2)
