#6.3 Glossário

glossario = {'string': 'Usada para armazenar e manipular textos.',
             'indentação': 'definir blocos de código.',
             'commit': 'uma operação de Git',
             'print': 'usada para exibir mensagens na tela',
             'laço': 'usado para iterar sobre uma sequência'
             }


#print para o dicionário

for palavra, significado in glossario.items():
    print(f'{palavra}:')
    print(f'{significado}\n')