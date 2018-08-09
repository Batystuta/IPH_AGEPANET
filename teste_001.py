# import random
#
# import emoji
# print(emoji.emojize("Olá Mundo :earth_americas:", use_aliases=True))
#
#
# num = random.randint(1,10)
# print(num)

# frase = '0123456789'
# aux = frase[::2]
# # print(frase)
# print(aux)

# from funcao_beta import fun_beta
# import modulo_beta
# aux = float(modulo_beta.fun_beta(315/1000, 24190, 721.2/1000, 0.0001, 0.0, 1.1))
# aux2 = float(modulo_beta.fun_fator_dw(315/1000, 721.2/1000, 0.0001))
# print(aux2)
# print(aux)


# import modulo_fator_atualizacao
# aux = float(modulo_fator_atualizacao.fun_fa(30, 0.12, 0.06))
# print(aux)


import modulo_custo_implantacao
aux = float(modulo_custo_implantacao.fun_custo_total(1, 0.200, 500, 8))
print(aux)