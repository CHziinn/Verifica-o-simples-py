idade = int(input('Insira sua idade: '))
altura = int(input('Insira sua altura: '))
opcoes = ['sim', 'nao', 'não']
autorizacao = input('Seus pais autorizaram sua vinda? ').lower()

#not in sempre primeiro, pois, caso nao valide o codigo morre aq
if autorizacao not in opcoes:
    print("Acesso Negado")

#meu ultimo codigo tava poluido com coisas desnecessarias
#O elif vai validar todos em uma unica linha ao inves de validacoes separadas
elif 12 <= idade <= 17 and 140 <= altura <= 199 and autorizacao == 'sim':
    # Aqui verifica todas as condições de uma vez
    print("Acesso Cedido")

else:
    # Se qualquer uma das condições anteriores falhar, codigo morre aq
    print('Acesso Negado')