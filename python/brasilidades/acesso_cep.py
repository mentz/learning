import requests


class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def get_endereco(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        req = requests.get(url)
        dados = req.json()
        return (dados["bairro"], dados["localidade"], dados["uf"])

    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def __str__(self):
        return self.format_cep()
