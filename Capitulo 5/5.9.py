#5.9 Sem usuários

##removendo a lista de usuarios

usuarios = []  

#Acrescentando if not para garantir que a lista não esteja vazia

if not usuarios:
    print('Precisamos encontrar novos usuários!')

# lista if-else

for usuario in usuarios:
    if usuario == 'admin':
        print('Olá admin, gostaria de ver um relatório de status?')
    else:
        print('Olá ' + usuario.title() + ', Obrigado por fazer login novamente!')    



