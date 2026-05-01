import os
from calculadora import soma

os.system('clear')

print(soma(10, 20))
print(soma(-10, 20))

# um modo de tratar excessoes de forma manual
try:
    print(soma('15', 15))
except TypeError as e:
    print('conta invalida')
    print(e)

# AssertionErro le o assert dentro da funcao original
try:
    print(soma('15', 15))
except AssertionError as e:
    print('conta invalida')
    print(e)

print('teste')
