# sistema bancario com as operacao de sacar, depositar  e visualizar extrato
import time


# obtendo o dia
def get_day():
    timestamp_atual = time.time()
    tempo_local = time.localtime(timestamp_atual)
    data_compelta = time.strftime('%d/%m/%Y', tempo_local)
    return data_compelta


def visualizar_extrato(extrato):
    print(extrato)


def escrever_extrato(extrato, mensagem):
    extrato += mensagem
    return extrato


def saque(saldo, saques_realizados):
    if saques_realizados > 2:
        print('O usuário já ultrapassou o limite diário de saques. Tente novamente amanha.')
        return False

    valor_saque = float(input('Digite (apenas números e "." caso deseje algo na casa dos centavos) o valor desejado para realizar o saque.\
                                      \nExemplo de saque: digite "120.25" caso queira sacar "R$ 120.25".\n Lembre-se que o limite diário de saques é de 3 operações e o limite máximo do saque é de R$ 500.00.'))

    if saques_realizados > 2:
        print('O usuário já ultrapassou o limite diário de saques. Tente novamente amanha.')
        return False
    elif valor_saque > saldo:
        print(f'O usuário tentou sacar R$ {
              valor_saque:.2f}, porém só há R$ {saldo:.2f} em sua conta.')
        return False
    else:
        saldo -= valor_saque
        return saldo
        # mensagem_extrato = f''
        # escrever_extrato()


def menu():
    print('\nVocê, o usuário, irá começar em um mundo ideal no qual todos gostaríamos de habitar. Será um milionário =D.')
    saldo_conta = 1e7
    info_extrato = f'\nExtrato iniciado.\nO saldo inicial da conta é R$ {
        saldo_conta:.2f}\n'
    print(info_extrato)

    limite_diario = 3
    saques_realizados = 0

    while True:
        operacao = input(
            '''Digite a operação desejada:
            [s]: Para realizar um saque em sua conta bancária.
            [e]: Para visualizar o seu extrato
            [0 (zero)]: para sair
            Operação: '''
        )
        if operacao == 's':
            saldo_conta = saque(saldo_conta, saques_realizados)

        elif operacao == 'e':
            print('\nVou fazer a visualizacao')
        elif operacao == '0':
            print(f'\nFechando menu no dia {
                  get_day()}.\nFoi um prazer te servir.\nAdeus!\n\n')
            break
        else:
            print('A operação desejada não está disponível.')

    return


menu()
