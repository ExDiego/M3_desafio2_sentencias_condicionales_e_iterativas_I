import sys #nos permitirá ver argumentos en la linea de comando.

peso = float(sys.argv[1])
altura = float(sys.argv[2])

#altura = altura / 100 if altura > 100 else altura

if altura > 100:
    altura = altura / 100


imc = peso / (altura ** 2)

#Clasificar la condición de según el OMS de acuerdo al imc

if imc < 18.5:
    oms = "Bajo Peso"
    
elif 18.5 <= imc < 25:
    oms = "Adecuado"
    
elif 25 <= imc < 30:
    oms = "Sobrepeso"
    
elif 30 <= imc < 35:
    oms = "Obesidad Grado I"
    
elif 35 <= imc < 40:
    oms = "Obesidad Grado II"
    
else:
    oms = "Obesidad Grado III"



print(f'su IMC es {imc:.2f}.')
print(f'Su clasificación según OMS es {oms}.')