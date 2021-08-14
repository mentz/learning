from cpf_cnpj import Documento
from telefones_br import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

import re

# cpf_um = Cpf("15316264754")
# print(cpf_um)

# exemplo_cnpj = "35379838000112"
# documento = CpfCnpj(exemplo_cnpj, "cnpj")
# print(CpfCnpj)

# cpf = Documento.cria_documento("15316264754")
# cnpj = Documento.cria_documento("35379838000112")

# print(cpf)
# print(cnpj)

# telefone = "554734544737"
# padrao = r"(\d{2,3})(\d{2})(\d{4,5})(\d{4})"
# resposta = re.search(padrao, telefone)
# print(resposta.group(2))

# telefone = "554726481234"
# telefone_objeto = TelefonesBr(telefone)
# print(telefone_objeto)

# cadastro = DatasBr()
# print(cadastro.mes_cadastro())
# print(cadastro.dia_semana())
# print(cadastro)
# print(cadastro.idade_cadastro())

cep = 89214400
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)
bairro, cidade, uf = objeto_cep.get_endereco()
print(bairro, cidade, uf)
