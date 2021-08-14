import re


class TelefonesBr:
    def __init__(self, telefone):
        if self.valida(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto")

    @staticmethod
    def valida(telefone):
        padrao = r"\d{2,3}\d{2}\d{4,5}\d{4}"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format(self):
        padrao = r"(\d{2,3})?(\d{2})(\d{4,5})(\d{4})"
        f = re.match(padrao, self.numero)
        return f"+{f[1]} ({f[2]}) {f[3]}-{f[4]}"

    def __str__(self):
        return self.format()
