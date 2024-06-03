#5.10 Verificando nomes de usuários

#Lista de usuarios atuais
current_users = ['guilherme', 'matheus', 'gabriel' , 'gustavo', 'joão']

#Lista de novos usuarios
new_users = ['manu', 'maria', 'marcos', 'gabriel', 'gustavo']

# Convertendo todos os nomes de usuários para minúsculas
current_users_lower = [user.lower() for user in current_users]

#Verificando cada usuario
for new_user in new_users:
    if new_user in current_users:
        print('Este nome ja foi utilizado, escolha outro.')
    else:
        print('Este nome está disponível.')  