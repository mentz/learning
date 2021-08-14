from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

gui = Usuario("Gui")
yuri = Usuario("Yuri")

lance_do_gui = Lance(gui, 150.0)
lance_do_yuri = Lance(yuri, 100.0)

leilao = Leilao("Celular")

leilao.lances.append(lance_do_yuri)
leilao.lances.append(lance_do_gui)

for lance in leilao.lances:
    print(f"O usuario {lance.usuario.nome} deu um lance de {lance.valor}")

avaliador = Avaliador()
avaliador.avalia(leilao)

print(
    "O menor lance foi de {} e o maior lance foi de {}".format(
        avaliador.menor_lance, avaliador.maior_lance
    )
)
