#5.5 Cores alienígenas #3


#Definindo a cor do alienígena

alien_colors = ['rosa'] # Altere para 'verde', 'amarelo' ou 'vermelho' para testar diferentes condições

#Cadeia if-elif-else correspondente
for alien_color in alien_colors:
    if alien_color == 'verde':
        print('Você acaba de ganhar 5 pontos por ser verde!')
    elif alien_color == 'amarelo':
         print('Você acaba de ganhar 10 pontos por ser amarelo!')
    elif alien_color == 'vermelho':
          print('Você acaba de ganhar 15 pontos por ser vermelho')
    else: 
        print('Cor errada!')