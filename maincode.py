print('\t\t\t\t\t\tAntifake')
while True:
    cadastro = input('Já tem uma conta? (s)im (n)ão: ').strip().lower()
    if cadastro.startswith('s'):
        ...
    elif cadastro.startswith('n'): # Se o usuário ainda não se cadastrou
        flag = True
        print('Cadastre-se agora!')
        while flag:
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
                flag = False
    else:
        print('Digite apenas "s" ou "n"')
        continue