renda_mensal = float(input('Qual sua renda mensal? '))
score = int(input('Possui score de crédito? Se sim digite o valor: '))
bens = (input('Possui bens com garantia? Responda com sim ou não: '))
historico = (input('Possui histórico de Inadimplência? Responda com sim ou não: '))
opcoes = ['sim', 'nao', 'não']

if historico not in opcoes:
    print ('Erro')
elif bens not in opcoes:
    print ('Erro')
elif renda_mensal >= 3000 and score >= 600 and (historico == 'nao'or historico == 'não') and bens == 'sim':
    print('Empréstimo aprovado!')
elif renda_mensal <= 2999.9 and score <= 599 and (historico == 'nao'or historico == 'não') and bens == 'sim':
    print ('Empréstimo aprovado')
else:
    print ('Empréstimo reprovado')