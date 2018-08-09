# _author_ = 'Batystuta Rocha'
# >>> Mestrado UFRGS/IPH 2017

def fun_adutora(diametro):

    # IMPLANTACAO da ADUTORA = f(Diametro)
    # f é o custo de implantação da tubulação e variavel como o Diâmetro por metro de comprimento.

    # Equação obtida da tabela de preço para ferro dúctil K7 e junta JGS.
    # FONTE: Maquimotor (2016) e DMAE (2016) apud Joice (2017).                     <<<<<cuidado
    custo_adutora = float(0.0023*(diametro*1000)**2 + 0.5306*(diametro*1000) + 94.999)    # R$/m.
    return custo_adutora

def fun_reservatorio(volume):

    # IMPLANTACAO do RESERVATORIO = f(Volume)
    # f é o custo de implantação do reservatorio e variavel como o Volume.

    # Equação obtida da tabela de preço para @@@@@@@@@@@@@@@@@@@@@@.
    # FONTE: Gomes (2016) apud Joice (2017).                                           <<<<<cuidado
    custo_reservatorio = float(-0.1202*volume**2 + 345.94*volume + 63443)   # R$.
    return custo_reservatorio

def fun_motobomba(potencia):

    # IMPLANTACAO do MOTOBOMBA = f(Potencia)
    # f é o custo de implantação do motobomba e variavel como a Potencia.

    # Equação obtida da tabela de preço para @@@@@@@@@@@@@@@@@@@@@@.
    # FONTE: Maquimotor (2016) apud Joice (2017).                                           <<<<<cuidado
    custo_motobomba = float(3.1688*potencia**2 + 388.55*potencia + 9022.1)  # R$.
    return custo_motobomba

def fun_custo_total(comprimento, diametro, volume, potencia):

    # Subrotina q calcula o Custo de Implanatação.
    # Custo Total = Custo da Adutora + Custo do Reservatorio + Custo Motobomba

    custo_total = float(fun_adutora(diametro)*comprimento + fun_reservatorio(volume) + fun_motobomba(potencia))
    return custo_total



