import epanet2.epanet2 as epa

path_Inp = r"C:\Users\batys\Dropbox\Epanet\Teste_04\Python\rede4.inp"
path_Rpt = r"C:\Users\batys\Dropbox\Epanet\Teste_04\Python\rede4.rpt"
path_Out = r"C:\Users\batys\Dropbox\Epanet\Teste_04\Python\rede4.out"

#Abrir fichero inp con la función ENopen
err = epa.ENopen(path_Inp, path_Rpt, path_Out)

(err,numNudos) = epa.ENgetcount(epa.EN_NODECOUNT)
(err,numLineas) = epa.ENgetcount(epa.EN_LINKCOUNT)
(err,valor) = epa.ENgetflowunits()

err = epa.ENclose()

print("El número total de nudos es: ", str(numNudos), "\n\El número total de líneas es: ", str(numLineas), "\n\La unidad de caudal utilizada es: ", UndCaudal)