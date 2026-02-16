import time
import os
import platform
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def voltar_menu():
    while True:
        volt = input('Deseja retornar ao menu? s/n: ').lower()
        if volt == 's':
            return True
        elif volt == 'n':
            return False
        else:
            input('Por favor responda somente com s ou n, tecle Enter para tentar novamente: ')
                    
def escolher_opcoes():
    while True:
        print(' 1- Adicionar item\n 2- Remover item\n 3- Mostrar itens\n 4- Sair')
        try:
            op = int(input('Opção escolhida: '))
            return op
        except ValueError:
            input('Opção inválida, tecle enter para tentar novamente: ')
            time.sleep(1.3)
            limpar_tela()
            continue


def adicionar(dicionario):
        while True:
            chave = input('Digite uma chave: ').strip()
            if not chave:
                input('A chave não pode ser vazia, tecle Enter para tentar novamente: ')
                time.sleep(1.2)
                continue
            if chave in dicionario:
                confirm = input('Essa chave já existe, gostaria de substituir? s/n: ').lower()
                if confirm == 's':
                    time.sleep(0.5)
                    print('Chave atualizada com sucesso!')
                elif confirm == 'n':
                    continue
                else:
                    input('Por favor responda somente com s ou n, tecle enter para tentar novamente: ')
                    continue

            valor = input('Digite um valor: ').strip()
            dicionario[chave] = valor
            print(f'A chave {chave} foi adicionada com sucesso!')
            time.sleep(1.2)
            limpar_tela()
            if voltar_menu(): 
                break
            else:
                limpar_tela
                continue
            
                
                
def finalizar_programa():
    print('Finalizando programa...')
    time.sleep(2)
    limpar_tela()
    exit()
    

def deletar_itens(dicionario):
    if not dicionario:
        print('O dicionário está vazio, não há nada à ser removido. ')
        time.sleep(1.2)
        limpar_tela()
        return
            
    while True:
        try:
            print('Menu de remoções:')
            opcao_limpar = int(input('1- Remover item completo\n2-Limpar valor da chave\n3-Voltar ao menu principal\n Opção escolhida: '))
        except ValueError: 
            print('Opção inválida, tente novamente')
            time.sleep(1.2)
            continue
        
        if opcao_limpar == 3:
            break

        if opcao_limpar not in [1,2]:
            print('Opção inválida, tente novamente..')
            time.sleep(1.2)
            continue
        chave = input('Digite o nome de chave: ') 
        if chave not in dicionario:
            print(f'A chave {chave} não existe, tente novamente..')
            time.sleep(1.2)
            continue

        if opcao_limpar == 1:
            del dicionario[chave]
            print(f'O item {chave} foi removido completamente.')
            limpar_tela()

        elif opcao_limpar == 2:
            dicionario[chave] = 'none'
            print(f'O valor da chave {chave} foi apagado')
            limpar_tela()

        time.sleep(1.2)
        if voltar_menu():
            break
        limpar_tela()

def mostrar_itens(dicionario):
    limpar_tela()
    if not dicionario:
        print('A lista está vazia...')
        input('Pressione Enter para retornar: ')
    else:
        print('-'*50)
        print('Lista de itens adicionados:')

        for k, v in dicionario.items():
            print(f'Item: {k}  |  Valor: {v}')
        
        input('Pressione Enter para retornar ao menu: ')
    limpar_tela()




dicionario = {}
print('*'*50)
print('Bem vindo ao dicionário interativo!\nPor favor escolha uma das opções abaixo:')
while True:
    op = escolher_opcoes()
    match op:
        case 1:
            adicionar(dicionario)

        case 2:
            deletar_itens(dicionario)
        
        case 3:
            mostrar_itens(dicionario)
        case 4:
            finalizar_programa()
            
        case _:
            print('Opção inválida! Tente novamente')
            time.sleep(1.45)
            limpar_tela()
            continue   
