#5.11 Números ordinais

#Armazenando números de 1 a 9

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Percorrendo a lista com um laço e tilizando cadeia if-elif-else

for numero in numeros:
    if numero == 1:
        print(str(numero) + 'st')
    elif numero == 2:
        print(str(numero) + 'nd')
    elif numero == 3:
        print(str(numero) + 'rd')
    else:
        print(str(numero) + 'th')

