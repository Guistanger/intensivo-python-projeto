# Cria um dicionário vazio
alien_0 = {}

# Adiciona a chave 'color' com o valor 'verde'
alien_0['color'] = 'verde'
print('O alien é ' + alien_0['color'] + '.')  # Saída: O alien é verde.

# Altera o valor da chave 'color' para 'amarelo'
alien_0['color'] = 'amarelo'
print('Agora o alien é ' + alien_0['color'] + '.')  # Saída: Agora o alien é amarelo.

# Redefine o dicionário com novas chaves e valores
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'médio'}

# Imprime a posição original no eixo x
print('Original x-position: ' + str(alien_0['x_position']))  # Saída: Original x-position: 0

# Determina o incremento da posição x com base na velocidade
if alien_0['speed'] == 'slow':
    x_increment = 1 
elif alien_0['speed'] == 'médio':
    x_increment = 2
else:
    x_increment = 3

# Atualiza a posição x com base no incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

# Adiciona a chave 'points' com o valor 5
alien_0['points'] = 5

# Imprime o dicionário final
print(alien_0)

# Removendo pares chave-valor

del alien_0['points']
print(alien_0)