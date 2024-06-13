#6.5 Rios

#lista de rios

rios = {'nilo': 'egito', 'amazonas': 'brasil', 'yangtze': 'china'}

#Laço para exibir frase

for rio_nome, pais in rios.items():
    print(f'O {rio_nome.title()} flui pelo país {pais.title()}')

#Laço para exibir o nome de cada rio

for rio in rios.keys():
    print(rio.title())

#Laço para exibir nome de cada país

for pais in rios.values():
    print(pais.title())