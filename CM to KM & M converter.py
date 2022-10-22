#CM to KM & M converter
CM = float(input('Enter value in CM:'))
M = CM/100
KM = M//1000
M = M-(KM*1000)
print (CM,'CM =',KM,'KM',round(M,2),'M')