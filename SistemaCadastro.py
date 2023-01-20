# Importando o módulo Operating System, para manipulação do arquivo TXT
import os

# Gerando a matriz dos assentos.
def gerar_matriz():
    matriz = []
    for rows in range(8):
        contador = 0
        row = []
        for column in range(5):
            if column == 2:
                row.append('  ')
                contador += 1
            else:
                if rows == 0:
                    row.append('  ')
                    contador += 1
                    row[0] = 'MO'
                elif rows == 1:
                    row.append('A'+f'{contador}')
                    contador += 1
                elif rows == 2:
                    row.append('B'+f'{contador}')
                    contador += 1
                elif rows == 3:
                    row.append('C'+f'{contador}')
                    contador += 1
                elif rows == 4:
                    row.append('D'+f'{contador}')
                    contador += 1
                elif rows == 5:
                    row.append('E'+f'{contador}')
                    contador += 1
                elif rows == 6:
                    row.append('F'+f'{contador}')
                    contador += 1
                elif rows == 7:
                    row.append('G'+f'{contador}')
                    contador += 1
                elif rows == 8:
                    row.append('H'+f'{contador}')
                    contador += 1
        matriz.append(row)
    return matriz


# Atribuindo a matriz ao objeto bus
bus = gerar_matriz()

# Lista dos assentos disponíveis
disponiveis = ['A0', 'A1', 'A3', 'A4', 'B0', 'B1', 'B3', 'B4',
               'C0', 'C1', 'C3', 'C4', 'D0', 'D1', 'D3', 'D4',
               'E0', 'E1', 'E3', 'E4', 'F0', 'F1', 'F3', 'F4',
               'G0', 'G1', 'G3', 'G4']

# Lista dos assentos ocupados
ocupados = []


# Função para perguntar se o usuário deseja algo mais, ou se gostaria de sair da aplicação.
def perguntar():
    print("""
Gostaria de solicitar algo mais?
- Digite \033[32m1\033[m para sim
- Digite \033[31m2\033[m para sair da aplicação""")
    resp = input('[1 - Continuar | 2 - Sair]: ').strip().upper()
    while resp not in ['1', '2']:
        print('\033[31mATENÇÃO: Digite apenas "1" para permanecer ou "2" para sair.\033[m')
        resp = input('[1 - Continuar | 2 - Sair]: ').strip().upper()
    if resp == '1':
        print('\n'*25)
        menu()
    elif resp == '2':
        print('\n'*25, f'Volte sempre, {usuario}!')
        print('\n' * 5)
        exit()


# Função para visualizar a matriz dos assentos (apresemtação visual com quebra de linhas)
def booking():
    print('\n' * 25)
    print('\n=', 'RESERVAS DE ASSENTOS', '=')
    for row in bus:
        for num in row:
            if num == 'XX':
                print('\033[41m', '  ', '\033[m', end=' ')
            elif num == 'MO':
                print('\033[44m', num, '\033[m', end=' ')
            elif num == '  ':
                print(num, end=' ')
            else:
                print('\033[42m', num, '\033[m', end=' ')
        print()
    print('=' * 23, '\n')
    print('\033[mLegenda:\n\n', '\033[0;30;42m   ',
          '\033[m: Assentos disponíveis  ',
          '\033[0;30;41m   ', '\033[m: Assentos Indisponíveis')
    return perguntar()


# Função para comprar passagens
def comprar():
    print('\n' * 25)
    print(f"""\033[32mLista de assentos disponíveis:\033[m  
{disponiveis[0:10]}
{disponiveis[10:20]} 
{disponiveis[20:30]},
            """)
    num = str(input('Digite a numeração do assento desejado: ')).upper().strip()
    while num not in disponiveis:
        print('\033[31mAssento não disponível.\033[m\n')
        print(f"""\033[32mLista de assentos disponíveis:\033[m 
{disponiveis[0:10]}
{disponiveis[10:20]} 
{disponiveis[20:30]}
            """)
        num = str(input('Digite a numeração de um assento disponível: ')).upper().strip()
    if num in disponiveis:
        ocupados.append(num)
        disponiveis.remove(num)
        ind = num[0]
        coluna = int(num[1])
        linha = 0
        if ind == 'A':
            linha = 1
        elif ind == 'B':
            linha = 2
        elif ind == 'C':
            linha = 3
        elif ind == 'D':
            linha = 4
        elif ind == 'E':
            linha = 5
        elif ind == 'F':
            linha = 6
        elif ind == 'G':
            linha = 7
        bus[linha][coluna] = 'XX'
    print('\n' * 25)
    print(f'\n{usuario}, sua reserva foi efetuada com sucesso!\n'
          f'A numeração do seu assento é: \033[2;32m{num}.\033[m\n')
    return perguntar()


# Função para trocar os assentos que foram escolhidos
def trocar():
    print('\n' * 25)
    if not ocupados:
        print('Nenhum assento ainda foi comprado.')
        perguntar()
    num = str(input('Digite a numeração do assento que deseja trocar: ')).upper().strip()
    while num not in ocupados:
        print('\033[31mO assento informado não existe ou não foi comprado.\033[m\n')
        print(f"""\033[32mLista de assentos já comprados:\033[m 
{ocupados[0:30]}
                """)
        num = str(input('Digite a numeração do assento que deseja trocar: ')).upper().strip()
    if num in ocupados:
        disponiveis.append(num)
        ocupados.remove(num)
        ind = num[0]
        ind2 = num[1]
        coluna = int(num[1])
        linha = 0
        if ind == 'A':
            linha = 1
        elif ind == 'B':
            linha = 2
        elif ind == 'C':
            linha = 3
        elif ind == 'D':
            linha = 4
        elif ind == 'E':
            linha = 5
        elif ind == 'F':
            linha = 6
        elif ind == 'G':
            linha = 7
        bus[linha][coluna] = f'{ind + ind2}'
    print('\n' * 25)
    print('Acento devolvido com sucesso! Agora, escolha o seu novo assento.\n')
    comprar()
    return perguntar()


# Função para imprimir a relação de assentos Vendidos x Disponíveis
def imprimir():
    print('\n' * 25)
    relacao = open(os.path.join('RelacaoAssentos.txt'), 'w')
    relacao.write('Relação dos assentos Disponíveis x Ocupados:')
    relacao.write('\n\n\n')
    relacao.write('Assentos disponíveis: ')
    for item in disponiveis:
        relacao.write(item + ' | ')
    relacao.write('\n\n')
    relacao.write('Assentos ocupados: ')
    for item in ocupados:
        relacao.write(item + ' | ')
    relacao.close()
    print('\n' * 25)
    print('Relação no formato .TXT gerada com sucesso!')
    return perguntar()


# Função para aresentar ao usuário o menu de opções
def menu():
    while True:
        print(f"""
Olá, {usuario}! Em que posso te ajudar?

[1] Comprar passagem individual
[2] Trocar assento já escolhido
[3] Verificar assentos vendidos e disponíveis
[4] Imprimir relação Vendidos x Disponíveis
[5] Sair do programa
""")

        esc = input('Digite a opção desejada: ')
        while esc not in ['1', '2', '3', '4', '5']:
            esc = input('\033[31mATENÇÃO: Escolha apenas um número entre 1 e 5: \033[m')
            print('')

        if esc == '1':
            comprar()
        elif esc == '2':
            trocar()
        elif esc == '3':
            booking()
        elif esc == '4':
            imprimir()
        elif esc == '5':
            print('\n' * 25)
            print(f'\nVolte sempre, {usuario}!')
            print('\n' * 5)
            exit()


# Programa principal
print('-=' * 20)
print(f'\033[34m{"Bem vindo(a)!":^40}\033[m')
print('-=' * 20)
usuario = str(input('Qual o seu nome? ')).strip().upper()

menu()
