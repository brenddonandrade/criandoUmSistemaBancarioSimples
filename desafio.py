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
        return saldo, saques_realizados

    valor_saque = float(input('Digite (apenas números e "." caso deseje algo na casa dos centavos) o valor desejado para realizar o saque.\
            \nExemplo de saque: digite "120.25" caso queira sacar "R$ 120.25".\nLembre-se que o limite diário de saques é de 3 operações e o limite máximo do saque é de R$ 500.00.\nQuantia: R$ '))

    if valor_saque > saldo:
        print(f'O usuário tentou sacar R$ {valor_saque:.2f}, porém só há R$ {saldo:.2f} em sua conta.')
        return saldo, saques_realizados
    else:
        saldo -= valor_saque
        saques_realizados += 1
        print(f'O usuário sacou R$ {valor_saque:.2f} e agora sua conta possui R$ {saldo:.2f}.')
        return saldo, saques_realizados


def deposito(saldo):
    quantia = float(input('Digite (apenas números e "." caso deseje algo na casa dos centavos) o valor desejado para realizar o Depósito.\
            \nExemplo de saque: digite "120.25" caso queira depositar "R$ 120.25".\nQuantia: R$ '))
    if quantia > 0:
        saldo += quantia
        print(f'Adicionando a sua conta R$ {quantia:.2f}. Agora o valor total é de R$ {saldo:.2f}.')
        return saldo
    else:
        print(f'Operação Inválida. O valor de deposito (R$ {quantia:.2f} não respeita as condições do banco.')
        return saldo


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
            '''

            Digite a operação desejada:
            [s]: Para realizar um saque;
            [d]: Para realizar um depósito;
            [e]: Para visualizar o seu extrato da sua conta bancária;
            [0 (zero)]: para sair.
            Operação: '''
        )
        if operacao == 's':
            saldo_conta, saques_realizados = saque(saldo_conta, saques_realizados)
        elif operacao == 'd':
            deposito(saldo_conta)
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
