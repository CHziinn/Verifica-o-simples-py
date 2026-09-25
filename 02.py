estudante = input('Voce e estudante? (responda com sim ou nao): ')
dia_semana = input('Que dia da semana é hoje? ')
sala = input('Tipo de sala: ')

opcoes1 = ['sim', 'nao', 'não']
opcoes2 = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo', 'sábado', 'terça']
opcoes3 = ['comum', 'vip']

# IF inicia a sequência de verificações
if estudante not in opcoes1:
    print('Diga sim ou não')

# Cada ELIF continua a mesma sequência de verificações
elif dia_semana not in opcoes2:
    print('Diga o dia da semana')

elif sala not in opcoes3:
    print('Diga a sala')

# Verifica as variaveis anteriores
elif estudante == 'sim' and (dia_semana == 'terca' or dia_semana == 'terça') and sala == 'comum':
    # Os parenteses agrupam as duas possibilidades de dia
    # Assim, o Python verifica se é 'terca' OU 'terça'
    # E com isso ele verifica com os and anteriores
    print('desconto aplicado')

else:
    print('sem desconto bobao')