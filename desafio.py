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
    extrato += ('\n' + mensagem)
    return extrato


def saque(saldo, saques_realizados, extrato):
    if saques_realizados > 2:
        print('O usuário já ultrapassou o limite diário de saques. Tente novamente amanha.')
        return saldo, saques_realizados, extrato

    valor_saque = float(input('Digite (apenas números e "." caso deseje algo na casa dos centavos) o valor desejado para realizar o saque.\
            \nExemplo de saque: digite "120.25" caso queira sacar "R$ 120.25".\nLembre-se que o limite diário de saques é de 3 operações e o limite máximo do saque é de R$ 500.00.\nQuantia: R$ '))

    if valor_saque > saldo:
        print(f'O usuário tentou sacar R$ {
              valor_saque:.2f}, porém só há R$ {saldo:.2f} em sua conta.')
        return saldo, saques_realizados, extrato

    elif valor_saque > 500:
        print(f'O usuário tentou sacar R$ {
              valor_saque:.2f}, porém o limite de saque é R$ 500.00 .')
        return saldo, saques_realizados, extrato

    else:
        saldo -= valor_saque
        saques_realizados += 1
        print(f'O usuário sacou R$ {
              valor_saque:.2f} e agora sua conta possui R$ {saldo:.2f}.')
        extrato = escrever_extrato(extrato,
                                   f'\t- R$ {valor_saque:.2f}\t {get_day()}')
        return saldo, saques_realizados, extrato


def deposito(saldo, extrato):
    valor_deposito = float(input('Digite (apenas números e "." caso deseje algo na casa dos centavos) o valor desejado para realizar o Depósito.\
            \nExemplo de saque: digite "120.25" caso queira depositar "R$ 120.25".\nvalor_deposito: R$ '))
    if valor_deposito > 0:
        saldo += valor_deposito
        print(f'Adicionando a sua conta R$ {
              valor_deposito:.2f}. Agora o valor total é de R$ {saldo:.2f}.')
        extrato = escrever_extrato(
            extrato, f'\t+ R$ {valor_deposito:.2f}\t {get_day()}')
        return saldo, extrato
    else:
        print(f'Operação Inválida. O valor de deposito (R$ {
              valor_deposito:.2f} não respeita as condições do banco.')
        return saldo, extrato


def menu():
    print('\nVocê, o usuário, irá começar em um mundo ideal no qual todos gostaríamos de habitar. Será um milionário =D.')
    saldo_conta = 1e7
    extrato = f'\nExtrato iniciado.\nO saldo inicial da conta é R$ {
        saldo_conta:.2f}\n'
    limite_diario = 3
    saques_realizados = 0

    while True:
        operacao = input('\n\nDigite a operação desejada:\n[s]: Para realizar um saque;\n[d]: Para realizar um depósito;\n[e]: Para visualizar o seu extrato da sua conta bancária;\n[0 (zero)]: para sair.\nOperação: '
                         )
        print('\n')
        if operacao == 's':
            saldo_conta, saques_realizados, extrato = saque(
                saldo_conta, saques_realizados, extrato)
        elif operacao == 'd':
            saldo_conta, extrato = deposito(saldo_conta, extrato)
        elif operacao == 'e':
            visualizar_extrato(extrato)
        elif operacao == '0':
            print(f'\nFechando menu no dia {
                  get_day()}.\nFoi um prazer te servir.\nAdeus!\n\n')
            break
        else:
            print('A operação desejada não está disponível.')

    return


menu()
