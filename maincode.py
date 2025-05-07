print('\t\t\t\t\t\tAntifake')
flag = True
while flag:
    cadastro = input('Já tem uma conta? (s)im (n)ão: ').strip().lower()
    if cadastro.startswith('s'):
        ...
    elif cadastro.startswith('n'): # Se o usuário ainda não se cadastrou
        flag = True
        print('Cadastre-se agora!')
        
        while True:
            nome = input("Digite seu nome completo: ").strip()

            # Verifica se o nome contém apenas letras e espaços
            if all(c.isalpha() or c.isspace() for c in nome):
                if len(nome.split()) >= 2:  # Verifica se tem pelo menos nome e sobrenome
                    break
                else:
                    print("Nome inválido, digite seu nome completo.")
            else:
                print("Nome inválido! Use apenas letras e espaços.")
        
        while True:
            email = input('digite seu email: ').strip()
            if ' ' in email: # caso ele tenha colocado espaço no email
                print('email inválido, seu email tem espaços.')
                continue
            if '@' not in email: # caso ele não tenha colocado o @ no email
                print('email inválido, seu email não tem "@".')
                continue
            if not ('gmail.com' in email or 'ufrpe.br' in email):  # caso ele não tenha colocado nem gmail.com nem ufrpe.br
                print('email inválido, use os domínios "gmail.com" ou "ufrpe.br".')
                continue
            if len(email.split('@')[0]) < 3: # Se seu email tiver menos de 3 caracteres (antes do @), é inválido
                print('email inválido, tente novamente!')
                continue     
            else:
                break
        
        while True:
            try:
                dia = int(input("Digite o dia de nascimento (1-31): "))
                mes = int(input("Digite o mês de nascimento (1-12): "))
                ano = int(input("Digite o ano de nascimento (a partir de 1900): "))

                if ano < 1900:
                    print("Ano inválido. Digite um ano a partir de 1900.")
                    continue
                if mes < 1 or mes > 12:
                    print("Mês inválido. Digite um número de 1 a 12.")
                    continue

                # Verifica os dias válidos do mês considerando ano bissexto
                if mes == 2:
                    if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
                        dias_do_mes = 29
                    else:
                        dias_do_mes = 28
                elif mes in [4, 6, 9, 11]:
                    dias_do_mes = 30
                else:
                    dias_do_mes = 31

                if dia < 1 or dia > dias_do_mes:
                    print(f"Dia inválido para o mês {mes}.")
                    continue

                print(f"Data válida: {dia:02}/{mes:02}/{ano}")
                break

            except ValueError:
                print("Digite apenas números válidos para dia, mês e ano.")

        while True:
            senha = input('Digite sua senha (min 8 caracteres): ')
            if len(senha) < 8:
                print('caracteres insuficientes, deve ter no mínimo 8.')
                continue
            confirmação_senha = input('confirme sua senha: ')
            if confirmação_senha == senha:
                break
            else:
                print('A confirmação falhou, suas senhas foram diferentes!')

    else:
        print('Digite apenas "s" ou "n"')
        continue