class ExtratorArgumentosUrlBytebank:
    def __init__(self, url):
        if self.urlEhValida(url):
            self.__url = url.lower()
        else:
            raise LookupError("Url inválida !!!!")

    @staticmethod
    def urlEhValida(url):
        if url and url.startswith("https://bytebank.com/"):
            return True
        else:
            return False

    def extraiArgumentos(self):

        buscaMoedaOrigem = "moedaorigem=".lower()
        buscaMoedaDestino = "moedadestino=".lower()

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.__url.find("&")

        moedaOrigem = self.__url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.__url.find("&")
            moedaOrigem = self.__url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestino = self.__url.find("&valor")
        moedaDestino = self.__url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.__url.find(moedaBuscada) + len(moedaBuscada)

    def trocaMoedaOrigem(self):
        self.__url = self.__url.replace("moedadestino", "real", 1)

    def extraiValor(self):
        buscaValor = "valor="
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.__url[indiceInicialValor:]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        representacaoString = f"Valor: {self.extraiValor()}\nMoeda Origem: {self.extraiArgumentos()[0]}\nMoeda Destino: {self.extraiArgumentos()[1]}"
        return representacaoString

    def __eq__(self, outraInstancia):
        return self.url == outraInstancia.url

    @property
    def url(self):
        return self.__url

    # Isso aqui foi eu quem pensou. Nao faz parte do curso da Alura.
    """

    def extraiArgumentos(self):
        somenteArgs = self.__url.split("?")[1].split("&")
        args = ((arg.split("=")[0], arg.split("=")[1]) for arg in somenteArgs)
        return dict(args)
    """

