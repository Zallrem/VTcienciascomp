from datetime import date, datetime, timedelta

class DATAS:
    def __init__(self, dia, mes, ano):
        self._dia = dia
        self._mes = mes
        self._ano = ano

    def get_dia(self):
        return self._dia
    def set_dia(self, dia):
        self._dia = dia

    def get_mes(self):
        return self._mes
    def set_mes(self, mes):
        self._mes = mes

    def get_ano(self):
        return self._ano
    def set_ano(self, ano):
        self._ano = ano



print("1-Exibir data atual")
print("2-Avançar um dia na data atual")
print("=====================================")
OPCAO1 = input(" Digite a opcao escolhida: ")
print("=====================================")




if OPCAO1 =='1':
    data = DATAS(date.today(), date.today(), date.today())
    datastr = data._dia.strftime('%d/') + data._mes.strftime('%m/') + data._ano.strftime('%Y')
    print(datastr)

if OPCAO1 =='2':
    data = DATAS(date.today() + timedelta(days=1), date.today(), date.today())
    datastr = data._dia.strftime('%d/') + data._mes.strftime('%m/') + data._ano.strftime('%Y')
    print(datastr)

