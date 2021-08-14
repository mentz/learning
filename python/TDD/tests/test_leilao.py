from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):
    def setUp(self):
        self.gui = Usuario("Gui", 500.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao("Celular")

    def test_avalia_maior_e_menor_em_ordem_ordem_crescente(self):
        yuri = Usuario("Yuri", 500.0)
        lance_do_yuri = Lance(yuri, 100.0)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_avalia_retorna_igual_para_somente_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 150.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_avalia_maior_e_menor_com_tres_lances(self):
        yuri = Usuario("Yuri", 500.0)
        vini = Usuario("Vini", 500.0)

        lance_do_yuri = Lance(yuri, 170.0)
        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 150.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # Se o leilão não tiver lances, deve permitir propor lance
    def test_deve_permitir_propor_um_lance_caso_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)

        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances)

    # Se o último usuário for diferente, deve permitir propor o lance
    def test_deve_permitir_propor_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario("Yuri", 500.0)
        lance_do_yuri = Lance(yuri, 160.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances)

    # Se o último usuário for o mesmo, não deve permitir propor o lance
    def test_nao_deve_permitir_propor_lance_caso_o_ultimo_usuario_seja_igual(self):
        lance_do_gui200 = Lance(self.gui, 200.0)

        # try:
        #     self.leilao.propoe(self.lance_do_gui)
        #     self.leilao.propoe(lance_do_gui200)
        #     self.fail(msg="Não lançou exceção.")
        # except ValueError:
        #     quantidade_de_lances = len(self.leilao.lances)
        #     self.assertEqual(1, quantidade_de_lances)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)

    # Não deve permitir um lance de valor igual ou menor do que o do último lance
    def test_nao_deve_permitir_propor_lance_caso_valor_seja_menor_ou_igual_ao_anterior(
        self,
    ):
        yuri = Usuario("Yuri", 500.0)
        vini = Usuario("Vini", 500.0)

        lance_do_yuri = Lance(yuri, 150.0)
        lance_do_vini = Lance(vini, 100.0)

        self.leilao.propoe(self.lance_do_gui)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(lance_do_yuri)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(lance_do_vini)

    # Deve permitir um lance de valor maior do que o do último lance
    def test_deve_permitir_propor_um_lance_com_valor_maior_ao_anterior(self):
        yuri = Usuario("Yuri", 500.0)

        lance_do_yuri = Lance(yuri, 170.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        quantidade_de_lances = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances)
