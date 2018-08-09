# _author_ = 'Batystuta Rocha'
# >>> Mestrado UFRGS/IPH 2017

def fun_curva_demanda():

    # Subrotina q gera as curvas de demanda.

    curva_demanda = [0.3, 0.4, 1.2, 1.5, 1.5, 1.3, 1.1, 0.7]

    variavel_epanet = [curva_demanda, int(24/len(curva_demanda))]

    return variavel_epanet