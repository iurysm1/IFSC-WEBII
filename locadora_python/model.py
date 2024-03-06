class NMotorizados:
    
    def __init__(self, placa, marca, modelo, ano, valor_locacao):
        self.placa=placa
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.valor_locacao=valor_locacao
    

    def __str__(self):
        return f"""
                ===Informações gerais===
                Placa: {self.placa}
                marca: {self.marca}
                modelo: {self.modelo}
                ano: {self.ano}
                valor locação: {self.valor_locacao}
                """


class Motorizados(NMotorizados):
    def __init__(self, placa, marca, modelo, ano, valor_locacao, quilometragemInicial, quilometragemFinal, potencia, taxa_quilometragem):
        super().__init__(self, placa, marca, modelo, ano, valor_locacao)
        self.quilometragemInicial=quilometragemInicial
        self.quilometragemFinal=quilometragemFinal
        self.potencia=potencia
        self.taxa_quilometragem=taxa_quilometragem

    

    def calcular_quilometragem(self):
        return self.quilometragemFinal-self.quilometragemInicial
    
    def __str__(self):
        return super().__str__()+\
            f"""
            ===Informaçoes específicas===
            Potencia: {self.potencia}
            Taxa de quilometragem: {self.taxa_quilometragem}
            Quilometragem percorrida: {self.calcular_quilometragem()}        
            """
        

class Locacao_nmotorizado:

    def __init__(self, dias_locado, veiculo):
        self.dias_locado=dias_locado
        self.veiculo=veiculo

    def total(self):
        return self.veiculo.valor_locacao*self.dias_locado
    
    def __str__(self):
        return f"""
                ===Locaçao não motorizada===
                Veiculo: {self.veiculo.modelo}
                Dias locado: {self.dias_locado}
                Total: {Total_locacao}
                """

class Locacao_motorizado:

    def __init__(self, dias_locado, veiculo):
        self.dias_locado=dias_locado
        self.veiculo=veiculo

    def total(self):
        return (self.veiculo.valor_locacao*self.dias_locado)+(self.veiculo.calcular_quilometragem()*self.veiculo.taxa_quilometragem)

    def __str__(self):
        return f"""
                ===Locaçao motorizada===
                Veiculo: {self.veiculo.modelo}
                Dias locado: {self.dias_locado}
                Total: {Total_locacao}
                """

class Total_locacao:

    def __init__(self):
        self.itens=[]

    def adicionar_locacao(self,locacao):
        self.itens.append(locacao)

    def __str__(self):
        resumo="===Resumo==="
        maiorLocacao=0
        maiorLocacaoStr=""
        valorTotalLocacao=0
        for locacao in self.itens:
            resumo+=locacao.__str__()
            valorTotalLocacao+=locacao.total()
            if locacao.total()>maiorLocacao:
                maiorLocacao=locacao.total()
                maiorLocacaoStr=locacao.veiculo.modelo
        resumo+=f"a maior locação foi a: {maiorLocacaoStr}"



    

