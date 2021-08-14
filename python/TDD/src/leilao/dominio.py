from src.leilao.excecoes import LanceInvalido


class Usuario:
    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self._pode_propor(valor):
            raise LanceInvalido(
                "Não pode propor um lance com valor maior que o valor da carteira."
            )

        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def _pode_propor(self, valor):
        return valor <= self.__carteira


class Lance:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

    def propoe(self, lance: Lance):
        if self._lance_valido(lance):
            self.__lances.append(lance)

    @property
    def lances(self):
        return self.__lances.copy()
        # return self.__lances[:] # também é cópia

    @property
    def menor_lance(self):
        return self.__lances[0].valor or 0

    @property
    def maior_lance(self):
        return self.__lances[-1].valor or 0

    def _tem_lances(self):
        return len(self.__lances) > 0

    def _usuarios_diferentes(self, lance):
        if lance.usuario != self.__lances[-1].usuario:
            return True
        raise LanceInvalido("O mesmo usuário não pode propor dois lances seguidos.")

    def _valor_de_lance_crescente(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido("Um novo lance deve ter valor maior que o último lance.")

    def _lance_valido(self, lance):
        return not self._tem_lances() or (
            self._usuarios_diferentes(lance) and self._valor_de_lance_crescente(lance)
        )
