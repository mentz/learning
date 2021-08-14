class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def dar_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    def __str__(self):
        return f"{self._nome}, {self.ano}, {self._likes} likes"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome}, {self.ano}, {self.duracao} min, {self._likes} likes"

    def __repr__(self):
        return f'Filme(nome="{self._nome}", ano={self.ano}, duracao={self.duracao})'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome}, {self.ano}, {self.temporadas} temporadas, {self._likes} likes"

    def __repr__(self):
        return (
            f'Serie(nome="{self._nome}", ano={self.ano}, temporadas={self.temporadas})'
        )


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __len__(self):
        return len(self._programas)

    def __getitem__(self, item):
        return self._programas[item]


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("todo mundo em panico", 1999, 100)
demolidor = Serie("demolidor", 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

listinha = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist("fim de semana", listinha)

for programa in minha_playlist:
    print(programa)

print(f"Tamanho: {len(minha_playlist)}")
print(vingadores in minha_playlist)
