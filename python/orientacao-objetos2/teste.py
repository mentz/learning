class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print("Horas registradas")

    def mostrar_tarefas(self):
        print("Fez muita coisa...")


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print("Fez muita coisa, Caelumer")

    def busca_cursos_do_mes(self, mes=None):
        print(
            f"Mostrando cursos do mês {mes}" if mes else "Mostrando cursos do mês atual"
        )


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print("Fez muita coisa, Alurete")

    def busca_perguntas_sem_resposta(self):
        print("Mostrando perguntas não respondidas no fórum")


class Hipster:
    def __str__(self):
        return f"Hipster, {self.nome}"


class Junior(Alura):
    pass


class Pleno(Caelum, Alura, Hipster):
    pass


jose = Junior("José")
jose.busca_perguntas_sem_resposta()

luan = Pleno("Luan")
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()

print(luan)
