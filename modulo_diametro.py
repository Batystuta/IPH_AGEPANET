# _author_ = 'Batystuta Rocha'
# >>> Mestrado UFRGS/IPH 2017

def fun_diametro(material):

    # Subrotina q gera um Diâmetro e em valor comercial
    # Diâmetro Tabelado para ferro dúctil K7 e junta JGS.

    if material == 'FERRO_K7':
        diametro = [100, 150, 200, 250, 300, 350, 400, 500, 600, 700, 800, 900, 1000]
        return diametro
    elif material == 'PVC_DE_FOFO':
        diametro = [1]
        return diametro
    return 0



