#5.6 Estágios da vida

##cadeia if-elif-else que determine o estágio da vida de uma pessoa

idade = 65  #local para definir idade

if idade < 2:
    print('Você é bebê!')
elif 2 <= idade < 4:
    print('Você é uma criança.')
elif 4 <= idade < 13:
    print('Você é jovem.')
elif 20 <= idade < 65:
    print('Você é um adulto.')
elif 65 >= idade:
    print('Você é um idoso')
