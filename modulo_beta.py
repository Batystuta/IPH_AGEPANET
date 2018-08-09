# _author_ = 'Batystuta Rocha'
# >>> Mestrado UFRGS/IPH 2017

def fun_rey(vazao, diametro):

    # Função para calcular o Reynold.

    const_pi = 3.1415926              # (constante)
    const_viscosidade = 0.000001004   # m^2/s (constante)

    rey = float(4*vazao/(const_pi*const_viscosidade*diametro))
    return rey


def fun_fator_dw(vazao, diametro, rugosidade):

    # A variálvel f(Rey;E/D) é calculda pelo formulda de Colebrook-White
    # Para calcular o f, utilizou um iteração numérico.
    # Inicia com o valor inicial de Swamme e Jain (1976).
    # Rugosidade padrão de 0.00002   >>> Ferro Dúctil, Classe K7

    import math

    aux = 100.00       # Variável auxiliar para a condição do While.

    # Valor inicial de Swamme e Jain (1976).
    f = float(0.25/(math.log10(rugosidade/(3.7*diametro)+5.74/(fun_rey(vazao, diametro)**(0.9)))**2))

    # Utilizando um iteração numérico.
    while ((f - aux) > 0.001):
        aux = f
        f = float((-1/(2*math.log10((rugosidade/diametro)/3.7+2.51/(fun_rey(vazao, diametro)*math.sqrt(f)))))**2)
    return f


def fun_beta(vazao, comprimento, diametro, rugosidade = 0.00002, soma_k = 0.10, majoracao_linear = 1.0):

    # Função q calcula a variável de perdas, Beta.
    # Que é a soma das perdas de carga localizada com a distribuida e podendo assumir a seguinte expressão:
    # B = (8/(pi^2*g))*(f + K*D/L)
    # Observação: o valor padrão de z = k/L vai ser atribuido de 0.10, mas geralmente é entre 0.5 e 0.15
    # Nessa subroutine, as variaveis dependentes são o Diâmetro e o Comprimento.
    # E as demais, pi = constante, g = constante e f = função(Rey;E/D)

    const_pi = 3.1415926     # (constante)
    const_gravidade = 9.81   # (constante)

    z = float(soma_k / comprimento)         # soma_k = 10% de comprimento (5% < k < 15%)

    beta = float((8./(const_pi**2*const_gravidade))*(fun_fator_dw(vazao, diametro, rugosidade)*majoracao_linear+z*diametro))
    return beta











