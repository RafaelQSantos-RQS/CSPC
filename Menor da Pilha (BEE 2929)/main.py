numero_de_operacoes = int(input())

pilha = []

for i in range(0,numero_de_operacoes):
    operacao = input()

if operacao.startswith("PUSH"):
    numero_a_ser_inserido = int(operacao.split()[1])
    pilha.append(numero_a_ser_inserido)
elif operacao.startswith("POP"):
    if len(pilha) > 0:
        pilha.pop()
    else:
        print('EMPTY')
elif operacao.startswith("MIN"):
    if len(pilha) > 0:
        valor_minimo_da_lista = min(pilha)
        print(valor_minimo_da_lista)
    else:
        print('EMPTY')
