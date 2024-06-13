#6.3 Glossário

glossario = {'variavel': 'uma referência a um valor armazenado na memória',
'lista': 'uma coleção ordenada de itens que pode ser modificada',
'dicionario': 'uma coleção de pares chave-valor',
'tupla': 'uma coleção ordenada de itens que não pode ser modificada',
'conjunto': 'uma coleção desordenada de itens únicos','string': 'Usada para armazenar e manipular textos.',
'indentação': 'definir blocos de código.',
'commit': 'uma operação de Git',
'print': 'usada para exibir mensagens na tela',
'laço': 'usado para iterar sobre uma sequência'}


#print para o dicionário

for palavra, significado in glossario.items():
    print(f'{palavra.title()}: {significado}')