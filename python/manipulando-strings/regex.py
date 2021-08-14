import re

msg1 = "Meu numero e 1234-5678"
msg2 = "O numero do meu celular e 1234-5678"
msg3 = "1234-5678 e meu numero"


padrao = "[0-9]{4,5}-?[0-9]{4}"

retorno = re.search(padrao, msg1)
print(retorno.group())
retorno = re.search(padrao, msg2)
print(retorno.group())
retorno = re.search(padrao, msg3)
print(retorno.group())
