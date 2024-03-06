from model import Locacao_motorizado, Locacao_nmotorizado, NMotorizados, Motorizados, Total_locacao



nMotorizado1= NMotorizados(ano=2020, placa='S/N', marca='Kaloi', modelo='B150', valor_locacao='40')

motorizado1=Motorizados(ano=2017, placa='CBA321', marca='KIA', modelo='Sportage', valor_locacao='200', potencia=10, quilometragemInicial=100, quilometragemFinal=110, taxa_quilometragem=10)



locacaoMotorizado= Locacao_motorizado(1,motorizado1)

locacaoNMotorizado=Locacao_nmotorizado(10,nMotorizado1)


total_locacao1=Total_locacao()

total_locacao1.adicionar_locacao(locacaoMotorizado)
total_locacao1.adicionar_locacao(locacaoNMotorizado)


print(total_locacao1)