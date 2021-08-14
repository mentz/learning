class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome.title()


cliente = Cliente("nico")
print(cliente.nome)
print(cliente._Cliente__nome)
cliente._Cliente__nome = "vagabundo"
print(cliente.nome)
