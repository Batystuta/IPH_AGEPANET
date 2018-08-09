# _author_ = 'Batystuta Rocha'
# >>> Mestrado UFRGS/IPH 2017

# Modulos q auxilia na programação:


import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns
import numpy as ny
import matplotlib.pyplot as plt
import sqlite3
import time
import datetime

connection = sqlite3.connect('bancoDeDados.db')
c = connection.cursor()


# Modulos criados:

import modulo_diametro
import modulo_hg
import modulo_comprimento
import modulo_beta
import modulo_custo_implantacao
import modulo_populacao
import modulo_curva_demanda

# import sys
# print(sys.path)
# sys.path.append('C:\\modulos\\diretorio')

class bd:
    def criaBD (self):
        arquivo = open('bancoDeDados.txt','w')
        arquivo.close

        #connection = sqlite3.connect('bancoDeDados.db')
        #c = connection.cursor()

def create_table():

    # Criando a Tabela de Dados

    c.execute('CREATE TABLE dados (id integer, unix real, keyword text, date )')



def IPH_AGEPANET_EXE ():

    # Parte executavel do programa
    # Essa parte é onde todas as subroutine são calling e feita o corpo do programa


    # Inicializando todas as variaveis gerais q vão receber dos seus modulos os valores

    # Número de Bombeamento = nb
    nb = [0,21,24]
    # Altura Geometrica = hg q recebe do modulo_hg e da função hg.
    hg = modulo_hg.fun_hg()
    # Comprimento = l q recebe do modulo_comprimento e da função comprimento.
    l = modulo_comprimento.fun_comprimento()
    # População = ppl q recebe do modulo_populacao e da função volume.
    volume_demanda = modulo_populacao.fun_volume()
    # Curva de Deamanda = curva_demanda q recebe do modulo_curva_demanda e da função curva demanda a curva e o intervalo dos dados.
    curva_demanda = modulo_curva_demanda.fun_curva_demanda


    # Laço de iteração da Altura Geometrica = hg[i].
    for i in range(0,4):

        # Laço de iteração de Comprimento = l[j].
        for j in range(0,5):

            # Laço de iteração de Volume de Demanda = volume_consumo[k].
            for k in range(0,7):

                # Laço de iteração do Número de Bombeamento = nb[w].
                for w in range(0,3):
                    if nb[w] == 0:
                        vazao_bombeada = 0
                    else:
                        vazao_bombeada = volume_demanda[k] / nb[w]
                    volume_reservatorio = modulo_volume_reservatorio.fun_volume(volume_demanda, nb)



                # Altura Geometrica = hg q recebe do modulo_hg e de função hg.
    hg = modulo_hg.fun_hg()









