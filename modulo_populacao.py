# _author_ = 'Batystuta Rocha'
# >>> Mestrado UFRGS/IPH 2017

def fun_populacao_ano_zero():

    # Função que tem as caracteristicas da população em estudo
    # Taxa de crescimento
    # E tipo de crescimento <<<<< observação com isso

    populacao_zero = 5000
    taxa_cresc = 0.02
    vetor_dados = [populacao_zero, taxa_cresc]
    return vetor_dados

def fun_crescimento():

    aux = fun_populacao_ano_zero()

    populacao_00 = aux[0]
    taxa = aux[1]

    populacao_05 = int(populacao_00*(1+taxa)**(5))
    populacao_10 = int(populacao_00*(1+taxa)**(10))
    populacao_15 = int(populacao_00*(1+taxa)**(15))
    populacao_20 = int(populacao_00*(1+taxa)**(20))
    populacao_25 = int(populacao_00*(1+taxa)**(25))
    populacao_30 = int(populacao_00*(1+taxa)**(30))

    vetor_populacao = [populacao_00, populacao_05, populacao_10, populacao_15, populacao_20, populacao_25, populacao_30]
    return vetor_populacao

def fun_volume():

    aux = fun_crescimento()
    volume = [0, 0, 0, 0, 0, 0, 0]
    consumo_per_capita = 0.2 # L/hab/dia
    k1 = 1.2
    for i in range(0,7):
        volume[i] = int(round(aux[i]*consumo_per_capita*k1))
    return volume

# print(fun_volume())