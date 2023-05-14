#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
#na ordem de colocação. Depois mostre:
'''a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('São Paulo', 'Corinthias', 'Palmeiras', 'Atlético Mineiro', 'Chapecoense', 'Internacional', 'Fluminense',
'Vasco', 'Bragantino', 'Agua Santa', 'Santos', 'Bahia', 'Flamengo', 'Botafogo', 'Gremio')

print(f'Os 5 primeiros times são {times[:5]}')

print(f'Os últimos 4 times são {times[11:]}')

print(f'Em ordem alfabética: ') 
print(sorted(times))

print(f'O Chapecoense está na {times.index("Chapecoense")} posição.')


