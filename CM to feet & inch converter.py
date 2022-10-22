#CM to feet & inch converter
CM = float(input('Enter value in CM:'))
inch = CM/2.54
feet = inch//12
inch = inch-(feet*12)
print (CM,'CM =',round(feet,0),'feet',round(inch,2),'inch')