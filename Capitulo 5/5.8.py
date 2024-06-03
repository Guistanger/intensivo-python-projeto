#5.8 Olá admin

##lista de usuarios

usuarios = ['guilherme', 'user', 'matheus', 'admin', 'gui']

# lista if-else

for usuario in usuarios:
    if usuario == 'admin':
        print('Olá admin, gostaria de ver um relatório de status?')
    else:
        print('Olá ' + usuario.title() + ', Obrigado por fazer login novamente!')      

