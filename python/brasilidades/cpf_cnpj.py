from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCPF(documento)
        elif len(documento) == 14:
            return DocCNPJ(documento)
        else:
            raise ValueError(
                "Quantidade de dígitos incorreta. 11 para CPF, 14 para CNPJ."
            )


class DocCPF:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido.")

    @staticmethod
    def valida(cpf):
        return CPF().validate(cpf)

    @staticmethod
    def format(cpf):
        return CPF().mask(cpf)

    def __str__(self):
        return self.format(self.cpf)


class DocCNPJ:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido.")

    @staticmethod
    def valida(cnpj):
        return CNPJ().validate(cnpj)

    @staticmethod
    def format(cnpj):
        return CNPJ().mask(cnpj)

    def __str__(self):
        return self.format(self.cnpj)
