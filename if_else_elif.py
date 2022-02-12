print('-------------SISTEMA DE CÁLCULO DE IMC--------------')
print('')

'''
O IMC É CALCULADO DIVIDINDO O PESO (EM KG) PELA ALTURA O QUADRADO (EM METROS)

- MENOR QUE 18.5 = MAGREZA
- ENTRE 18.5 E 24.9 = NORMAL
- ENTRE 25,0 E 29.9 = SOBREPESO
- ENTRE 30.0 E 39.9 = OBESIDADE
- MAIOR QUE 40.0 = OBESIDADE GRAVE
'''

altura = float(input('Digite a sua altura (Ex: 1.80):'))
print('')
peso = float(input('Digite o seu peso (Ex: 80):'))
print('')

imc = peso / (altura**2)
print('')
# ** = operador de potencia
imc = round(imc, 2)

if imc < 18.5:
    print(f'Seu IMC é {imc}, e seu peso está categorizado como MAGREZA')
    print('')
    print('Ponto de atenção: Vamos comer melhor?')
elif imc >= 18.5 and imc <= 24.9:
    print(f'Seu IMC é {imc}, e seu peso está categorizado como NORMAL')
    print('')
    print('Parabéns! Continue se cuidando!!')
elif imc >= 25.0 and imc <= 29.9:
    print(f'Seu IMC é {imc}, e seu peso está categorizado como SOBREPESO')
    print('')
    print('Ponto de atenção: Fique Ligado com o seu peso!')
elif imc >= 30.0 and imc <= 39.9:
    print(f'Seu IMC é {imc}, e seu peso está categorizado como OBESIDADE')
    print('')
    print('Ponto de atenção: É necessário fazer uma dieta seguida com uma atividade física!')
elif imc > 40.0:
    print(f'Seu IMC é {imc}, e seu peso está categorizado como OBESIDADE GRAVE')
    print('')
    print('Ponto de atenção: Procure um médico para que possa fazer um programa personalizado para você!')

print('', end='\n\n')
print('----------------CUIDE DA SUA SAÚDE-----------------')
print('')
