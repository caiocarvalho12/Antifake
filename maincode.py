print('\t\t\t\t\t\tAntifake')
flag = True
while flag:
    cadastro = input('Já tem uma conta? (s)im (n)ão: ').strip().lower()
    if cadastro.startswith('s'):
        ...
    elif cadastro.startswith('n'): # Se o usuário ainda não se cadastrou
        flag = True
        print('Cadastre-se agora!')
        
        def cadastrar_nome():
            while True:
                nome = input("Digite seu nome completo: ").strip()
                # Verifica se o nome contém apenas letras e espaços
                if all(c.isalpha() or c.isspace() for c in nome):
                    if len(nome.split()) >= 2:  # Verifica se tem pelo menos nome e sobrenome
                        return nome    
                    else:
                        print("Nome inválido, digite seu nome completo.")
                else:
                    print("Nome inválido! Use apenas letras e espaços.")
        
        def cadastrar_email(): 
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
                    print('email inválido, seu email deve haver mais caracteres!')
                    continue
                if 'gmail.com' in email and len(email.split('@')[1]) != 9: #Se o email tiver mais ou menos que 9 caracteres depois do '@' e for gmail.com, é inválido.   
                    print('email inválido, domínio está incorreto')
                    continue
                if 'ufrpe.br' in email and len(email.split('@')[1]) != 8: #Se o email tiver mais ou menos que 8 caracteres depois do '@' e for ufrpe.br, é inválido.   
                    print('email inválido, domínio está incorreto')
                    continue
                else:
                    return email
                
        def cadastrar_data():
            while True:
                data_de_nascimento = input('Digite sua data de nascimento: (dd/mm/aaaa): ')
                partes = data_de_nascimento.split('/')
                if len(partes) != 3:
                    print('formato inválido, use dd/mm/aaaa.')
                    continue
                dia, mes, ano = partes
                if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
                    print('A data de nascimento deve conter apenas numeros e "/" para divisão.')
                    continue
                if len(dia) != 2 or len(mes) != 2 or len(ano) != 4:
                    print('É necessário dois caracteres no dia, dois caracteres no mês e quatro no ano')
                    continue
                
                dia_int = int(dia)
                mes_int = int(mes)
                ano_int = int(ano)

                if not 1 <= mes_int <= 12:
                    print('(erro 0) data de nascimento inválida')
                    continue
                if mes_int % 2 == 1 and not 1 <= dia_int <= 31: # mês ímpar, dia até 31 
                    print('(erro 1) data de nascimento inválida')
                    continue
                if mes_int == 2:
                    if (ano_int % 4 == 0 and (ano_int % 100 != 0 or ano_int % 400 == 0)):
                        if not 0 < dia_int <= 29:
                            print('(erro2.1) data de nascimento inválida')
                            continue
                    else:
                        if not 0 < dia_int <= 28:
                            print('(erro2.2) data de nascimento inválida')
                            continue
                if mes_int % 2 == 0 and mes_int != 2 and not 1 <= dia_int <= 30:
                    print('(erro 3) data de nascimento inválida')
                    continue
                if not 1900 < ano_int <= 2025:
                    print('(erro 4) data de nascimento inválida')
                    continue
                else:
                    return data_de_nascimento

        def cadastrar_senha():
            while True:
                senha = input('Digite sua senha (min 8 caracteres): ')
                if len(senha) < 8:
                    print('caracteres insuficientes, deve ter no mínimo 8.')
                    continue
                if senha.isalpha() or senha.isdigit():
                    senha_fraca = input('senha fraca, gostaria de tentar de novo para deixá-la mais forte?' \
                                        '(s)im ou (n)ão): ').lower().strip()
                    if senha_fraca.startswith('s'):
                        continue
                confirmação_senha = input('confirme sua senha: ')
                if confirmação_senha == senha:
                    return senha
                else:
                    print('A confirmação falhou, suas senhas foram diferentes!')

    else:
        print('Digite apenas "s" ou "n"')
        continue