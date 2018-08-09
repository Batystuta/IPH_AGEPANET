# _author_ = 'Batystuta Rocha'
# >>> Mestrado UFRGS/IPH 2017

import modulo_curva_demanda

def fun_volume(volume_demanda, nb, curva_demanda = modulo_curva_demanda.fun_curva_demanda()):

    # Volume é determinado por vários métodos mas para teste inicial estou utilizando:

    k2 = 1.5

    if nb == 0:
        volume_reservatorio = (1/3)*volume_demanda*k2
        #print('OKAY >>>>> volume do Reservatorio: {:.4f} m^3'.format(volume_reservatorio))
        return volume_reservatorio
    elif nb == 24:
        volume_reservatorio = 0.0
        #print('OKAY >>>>> volume do Reservatorio: {:.4f} m^3'.format(volume_reservatorio))
        return volume_reservatorio
    else:
        # Método de determinação do volume útil baseado nos volumes diferenciais

        soma_positivo = 0.0000
        soma_negativo = 0.0000
        curva_bomba = [3, 3, 3, 3, 0, 3, 3, 3]

        #vazao_media_demanda = float(volume_demanda/(24/curva_demanda[1]))
        #intervalo = int(24/curva_demanda[1])
        #print(curva_demanda)

        for i in range(0,int(24/curva_demanda[1])):
            vazao_diferencial = float((volume_demanda/nb)*curva_bomba[i] - ((volume_demanda/(24/curva_demanda[1]))*curva_demanda[0][i]))
            #print(curva_bomba[i])
            #print(vazao_diferencial)
            if vazao_diferencial > 0:
                soma_positivo += vazao_diferencial
            else:
                soma_negativo += vazao_diferencial
        #print(vazao_media_demanda)
        #print(volume_demanda/nb)
        #print(soma_positivo)
        #print(soma_negativo)
        if int(soma_positivo) == int(-soma_negativo):
            volume_reservatorio = soma_positivo
            #print('OKAY >>>>> volume do Reservatorio: {:.4f} m^3'.format(volume_reservatorio))
        else:
            volume_reservatorio = -1.1
            #print('Não OKAY >>>>> volumes diferentes: {:.4f} m^3'.format(volume_reservatorio))
        return volume_reservatorio



#import modulo_curva_demanda

#curva_demanda = modulo_curva_demanda.fun_curva_demanda()

aux = fun_volume(1000,21)

#print(curva_demanda[0][0])

