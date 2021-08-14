from datetime import datetime


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.now()

    def mes_cadastro(self):
        meses = [
            "janeiro",
            "fevereiro",
            "março",
            "abril",
            "maio",
            "junho",
            "julho",
            "agosto",
            "setembro",
            "outubro",
            "novembro",
            "dezembro",
        ]
        return meses[self.momento_cadastro.month - 1]

    def dia_semana(self):
        dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
        return dias[self.momento_cadastro.weekday()]

    def format_br(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")

    def idade_cadastro(self):
        return datetime.now() - self.momento_cadastro

    def __str__(self):
        return self.format_br()

