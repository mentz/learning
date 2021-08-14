from collections.abc import MutableSequence


class MinhaListinhaMutavel(MutableSequence):
    pass


objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)

# Pode ver que a execucao do codigo acima vai gerar um erro
# que informa que os metodos abstratos nao foram implementados.
