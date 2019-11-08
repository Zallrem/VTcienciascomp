# -*- coding: UTF-8 -*-
class Empregado:
    def __init__(self, nome, sobrenome, salario_mensal = 0.0):
        self._nome = nome
        self._sobrenome = sobrenome
        self._salario_mensal = salario_mensal

    def get_nome(self):
        return self._nome
    def set_nome(self, nome):
        self._nome = nome

    def get_sobrenome(self):
        return self._sobrenome
    def set_sobrenome(self, sobrenome):
        self._sobrenome = sobrenome

    def get_salario_mensal(self):
        return self._salario_mensal
    def set_salario_mensal(self, salario_mensal):
        self._salario_mensal = salario_mensal

    def salario_anual(self, salario):
        salarioano = salario * 12
        return salarioano


jose = Empregado("jose", "victor", 1000.0)
gabriely = Empregado("gabriely", "coraline", 1000.0)
aumento = 10

print ("Salario anual de Gabriely: {:.2f}" .format(jose.salario_anual(jose._salario_mensal)))
print ("Salario anual de Gabriely: {:.2f}\n" .format(gabriely.salario_anual(gabriely._salario_mensal)))

print ("Salario anual de José com reajuste: {:.2f}" .format(jose.salario_anual(jose._salario_mensal)+(jose.salario_anual(jose._salario_mensal) * aumento/100)))
print ("Salario anual de Gabriely com reajuste: {:.2f}" .format(gabriely.salario_anual(gabriely._salario_mensal)+(gabriely.salario_anual(gabriely._salario_mensal) * aumento/100)))



