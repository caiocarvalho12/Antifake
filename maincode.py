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
            nome = input('Digite seu nome completo: ').strip()
            if len(nome.split()) < 2:
                print('Digite seu nome completo')
                continue
            else:
                break
        
        while True:
            email = input('digite seu email: ').strip()
            if ' ' in email: # caso ele tenha colocado espaço no email
                print('email inválido, seu email tem espaços')
                continue
            if '@' not in email: # caso ele não tenha colocado o @ no email
                print('email inválido, seu email não tem "@"')
                continue
            if not ('gmail.com' in email or 'ufrpe.br' in email):  # caso ele não tenha colocado nem gmail.com nem ufrpe.br
                print('email inválido falta o domínio gmail.com ou ufrpe.br')
                continue
            if len(email.split('@')[0]) < 3: # Se seu email tiver menos de 3 caracteres (antes do @), é inválido
                print('email inválido5')
                continue     
            else:
                break
        
        while True:
            data_de_nascimento = input('Digite a sua data de nascimento:(dd/mm/aaaa) ').strip()
            if '/' not in data_de_nascimento:
                print('formato inválido, use dd/mm/aaaa')
                continue

            partes = data_de_nascimento.split('/')
            if len(partes) != 3:
                print('formato inválido, use dd/mm/aaaa')
                continue

            dia, mes, ano = partes
            if not (dia.isdigit and mes.isdigit and ano.isdigit):
                print('A data de nascimento deve conter apenas numeros e "/" para divisão')
                continue
            if len(dia) != 2 or len(mes) != 2 or len(ano) != 4:
                print('É necessário 2 caracteres no dia, 2 no mês e 4 no ano')
                continue
            else:
                break

        while True:
            senha = input('Digite sua senha (min 8 caracteres): ')
            if len(senha) < 8:
                print('caracteres insuficientes, minimo 8')
                continue
            confirmação_senha = input('confirme sua senha: ')
            if confirmação_senha == senha:
                break
            else:
                print('A confirmação falhou, suas senhas foram diferentes')

    else:
        print('Digite apenas "s" ou "n"')
        continue