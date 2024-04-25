from model import Locacao_motorizado, Locacao_nmotorizado, NMotorizados, Motorizados, Total_locacao



nMotorizado1= NMotorizados(ano=2020, placa='S/N', marca='Kaloi', modelo='B150', valor_locacao=40)

motorizado1=Motorizados(ano=2017, placa='CBA321', marca='KIA', modelo='Sportage', valor_locacao=200, potencia=10, quilometragemInicial=100, quilometragemFinal=110, taxa_quilometragem=10)
motorizado2=Motorizados(ano=2010, placa='ABC123', marca='FIAT', modelo='UNO', valor_locacao=100, potencia=5, quilometragemInicial=100, quilometragemFinal=150, taxa_quilometragem=8)




locacaoMotorizado= Locacao_motorizado(1,motorizado1)

locacaoNMotorizado=Locacao_nmotorizado(10,nMotorizado1)

locacaoMotorizado2=Locacao_motorizado(10, motorizado2)

total_locacao1=Total_locacao()

total_locacao1.adicionar_locacao(locacaoMotorizado)
total_locacao1.adicionar_locacao(locacaoNMotorizado)
total_locacao1.adicionar_locacao(locacaoMotorizado2)



print(total_locacao1.__str__())