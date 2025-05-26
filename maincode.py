import json
import os

ARQUIVO_USUARIOS = 'usuarios.json'

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, 'w', encoding='utf-8') as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

def cadastrar_nome():
    while True:
        nome = input("Digite seu nome completo: ").strip()
        if all(c.isalpha() or c.isspace() for c in nome):
            if len(nome.split()) >= 2:
                return nome
            else:
                print("Nome inválido, digite seu nome completo.")
        else:
            print("Nome inválido! Use apenas letras e espaços.")

def cadastrar_data():
    while True:
        data = input('Digite sua data de nascimento (dd/mm/aaaa): ')
        partes = data.split('/')
        if len(partes) != 3:
            print('Formato inválido, use dd/mm/aaaa.')
            continue
        dia, mes, ano = partes
        if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
            print('Use apenas números e "/" para dividir.')
            continue
        dia, mes, ano = int(dia), int(mes), int(ano)
        if not 1 <= mes <= 12 or not 1900 < ano <= 2025:
            print('Data de nascimento inválida.')
            continue
        if mes == 2:
            if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
                if not 1 <= dia <= 29:
                    print('Dia inválido para fevereiro em ano bissexto.')
                    continue
            else:
                if not 1 <= dia <= 28:
                    print('Dia inválido para fevereiro.')
                    continue
        elif mes in [4, 6, 9, 11] and not 1 <= dia <= 30:
            print('Esse mês tem no máximo 30 dias.')
            continue
        elif not 1 <= dia <= 31:
            print('Dia inválido.')
            continue
        return data

def cadastrar_email(usuarios):
    while True:
        email = input('Digite seu email: ').strip()
        if ' ' in email:
            print('Email inválido: contém espaços.')
            continue
        if '@' not in email:
            print('Email inválido: falta "@"')
            continue
        if not ('gmail.com' in email or 'ufrpe.br' in email):
            print('Use domínios "gmail.com" ou "ufrpe.br".')
            continue
        if len(email.split('@')[0]) < 3:
            print('Email inválido: parte antes do @ muito curta.')
            continue
        if email in usuarios:
            print('Esse email já está cadastrado.')
            continue
        return email

def cadastrar_senha():
    while True:
        senha = input('Digite sua senha (mín. 8 caracteres): ')
        if len(senha) < 8:
            print('Senha muito curta.')
            continue
        if senha.isalpha() or senha.isdigit():
            tentar = input('Senha fraca. Quer tentar outra? (s/n): ').strip().lower()
            if tentar.startswith('s'):
                continue
        confirmacao = input('Confirme sua senha: ')
        if senha == confirmacao:
            return senha
        else:
            print('Confirmação incorreta.')

print('\n' + '='*30)
print('\tBem-vindo ao Antifake')
print('='*30)

usuarios = carregar_usuarios()

while True:
    escolha = input('\nVocê já tem uma conta? (s)im / (n)ão / (sair): ').strip().lower()

    if escolha.startswith('s'):
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        if email in usuarios and usuarios[email]['senha'] == senha:
            print(f'\nBem-vindo de volta, {usuarios[email]["nome"]}!')
        else:
            print('Email ou senha incorretos.')
            continue

    elif escolha.startswith('n'):
        print('\nCadastre-se agora!')
        nome = cadastrar_nome()
        data_nascimento = cadastrar_data()
        email = cadastrar_email(usuarios)
        senha = cadastrar_senha()

        usuarios[email] = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'senha': senha
        }
        salvar_usuarios(usuarios)
        print('Cadastro realizado com sucesso!')

    elif escolha.startswith('sair'):
        print('Encerrando o programa...')
        break

    else:
        print('Digite apenas "s", "n" ou "sair".')
        continue

    while True:
        opcao = input('\nEscolha:\n'
                      '(1) Ver dados\n'
                      '(2) Editar dados\n'
                      '(3) Deletar conta\n'
                      '(4) Ir para questionário\n'
                      '(5) Ver tutorial\n'
                      '(6) Ver feedback\n'
                      '(0) Sair do menu\n> ').strip()

        if opcao == '1':
            print(json.dumps(usuarios[email], indent=4, ensure_ascii=False))

        elif opcao == '2':
            print('\n--- Editar dados ---')
            novo_nome = cadastrar_nome()
            nova_data = cadastrar_data()
            nova_senha = cadastrar_senha()
            usuarios[email]['nome'] = novo_nome
            usuarios[email]['data_nascimento'] = nova_data
            usuarios[email]['senha'] = nova_senha
            salvar_usuarios(usuarios)
            print('Dados atualizados!')

        elif opcao == '3':
            confirmar = input('Tem certeza que deseja deletar sua conta? (s/n): ').strip().lower()
            if confirmar == 's':
                del usuarios[email]
                salvar_usuarios(usuarios)
                print('Conta deletada.')
                break

        elif opcao == '0':
            print('Voltando ao menu principal...')
            break
        else:
            print('Função ainda não implementada.')