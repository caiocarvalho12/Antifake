print('\t\t\t\t\t\tAntifake')

flag = True
while flag:
    cadastro = input('Já tem uma conta? (s)im (n)ão: ').strip().lower()
    
    if cadastro.startswith('s'):
        print("Login em desenvolvimento...")  # Substitua por lógica de login real depois
        flag = False
    
    elif cadastro.startswith('n'):
        print('Cadastre-se agora!')

        # Nome
        while True:
            nome = input("Digite seu nome completo: ").strip()
            if all(c.isalpha() or c.isspace() for c in nome):
                if len(nome.split()) >= 2:
                    break
                else:
                    print("Nome inválido, digite seu nome completo.")
            else:
                print("Nome inválido! Use apenas letras e espaços.")

        # Email
        while True:
            email = input('Digite seu email: ').strip()
            if ' ' in email:
                print('Email inválido, contém espaços.')
            elif '@' not in email:
                print('Email inválido, falta "@".')
            elif not ('gmail.com' in email or 'ufrpe.br' in email):
                print('Email inválido, use "gmail.com" ou "ufrpe.br".')
            elif len(email.split('@')[0]) < 3:
                print('Email inválido, parte antes do "@" muito curta.')
            else:
                break

        # Data de nascimento
        def eh_bissexto(ano):
            return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

        def dias_no_mes(mes, ano):
            if mes == 2:
                return 29 if eh_bissexto(ano) else 28
            elif mes in [4, 6, 9, 11]:
                return 30
            else:
                return 31

        while True:
            try:
                dia = int(input("Digite o dia de nascimento (1-31): "))
                mes = int(input("Digite o mês de nascimento (1-12): "))
                ano = int(input("Digite o ano de nascimento (a partir de 1900): "))

                if ano < 1900:
                    print("Ano inválido. Deve ser a partir de 1900.")
                elif mes < 1 or mes > 12:
                    print("Mês inválido.")
                elif dia < 1 or dia > dias_no_mes(mes, ano):
                    print("Dia inválido para esse mês.")
                else:
                    print(f"Data válida: {dia:02}/{mes:02}/{ano}")
                    break
            except ValueError:
                print("Digite apenas números válidos.")

        # Senha
        while True:
            senha = input('Digite sua senha (mínimo 8 caracteres): ')
            if len(senha) < 8:
                print('Senha muito curta.')
            else:
                confirmacao = input('Confirme sua senha: ')
                if confirmacao == senha:
                    break
                else:
                    print('As senhas não coincidem.')

        print("Cadastro realizado com sucesso!")
        flag = False  # encerra o loop

    else:
        print('Digite apenas "s" ou "n".')