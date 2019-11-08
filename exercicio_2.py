# -*- coding: UTF-8 -*-

class Fatura:
    def __init__(self, num_item, descricao, qntd = 0, preco = 0.0):
        self._num_item = num_item
        self._descricao = descricao
        self._qntd = qntd
        self._preco = preco

    def get_num_item(self):
        return self._num_item
    def set_num_item(self, num_item):
        self._num_item = num_item

    def get_descricao(self):
        return self._descricao
    def set_descricao(self, descricao):
        self._descricao = descricao

    def get_qntd(self):
        return self._qntd
    def set_qntd(self, qntd):
        self._qntd = qntd

    def get_preco(self):
        return self._preco
    def set_preco(self, preco):
        self._preco = preco


    def get_valor_fatura(self, quant, valor):
        fatura = quant * valor
        print("Valor da fatura:", fatura)



Dados = Fatura(159, 'tenis', 15, 10.2)
Dados.get_valor_fatura(Dados._qntd, Dados._preco)



