# _author_ = 'Batystuta Rocha'
# >>> Mestrado UFRGS/IPH 2017

def fun_fa(ano, i = 0.12, e = 0.08):

    # Subrotina q calcula o Fator de Atualização do investimento variavel para fixo
    # O Fa vai ser aplicado no custo de Operação,  para se conhecer o valor fixo atual
    # Nessa subroutine, com o imposto, o aumento de energia e o horizonte de projeto tem o Fa
    # Obs.: O fator de atualização vai ser fixo para todos os cenarios
    # Valores padrões de crescimento: i = 12%/ano; e = 8%/ano

    fa = float((((1+e)**ano-(1+i)**ano)/((1+e)-(1+i)))*(1/((1+i)**ano)))    # e crescente com o tempo e fluxo de caixa não uniforme.
    return fa
