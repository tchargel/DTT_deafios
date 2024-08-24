menu = '''

[D] Depositar
[S] Sacar
[E] Extrato
[X] Sair

'''

saldo =  0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        print('Deposito')
        
        valor = float(input('quanto deseja depositar?'))
        if valor > 0:
            saldo += valor
            extrato +=(f'Depostito - R${valor:.2f}\n')
            print(f'Deposito efetuado com sucesso. Seu novo saldo é de R${saldo:.2f}\n')
        else: 
            print(  'valor inválido')
        
    elif opcao == 's':
        
        print('Sacar')
        valor = float(input('quanto deseja sacar?'))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques
        
        if excedeu_saldo:
            print('saldo insuficiente')
        elif excedeu_limite:
            print('o valor do saque excedeu o limite')
        elif excedeu_saques:
            print('numero maximo de saques excedido')
        elif valor > 0 :
            saldo -= valor
            extrato += f'saque: - R$ {valor:.2f}\n'
            numero_saques += 1
            print(f'saque efetuado com sucesso, seu novo saldo é de R${saldo:.2f\n}')
        else:
            print('operacao falhou')
        
        
    elif opcao == 'e':
        print('\n===============Extrato===============')
        print('Não foram realidas movimentações' if not extrato else extrato)
        print(f'\n saldo: R${saldo:.2f}\n')
        print('\n=====================================')
')
        
    elif opcao == 'x':
        break
    else:
        print('operação inválida')
