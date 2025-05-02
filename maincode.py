print('\t\t\t\t\t\tAntifake')
while True:
    cadastro = input('Já tem uma conta? (s)im (n)ão: ').strip().lower()
    if cadastro.startswith('s') == True:
        ...
    elif cadastro.startswith('n'): # Se o usuário ainda não se cadastrou
        flag = True
        print('Cadastre-se agora!')
        while flag:
            
            email = input('digite seu email: ')
            if ' ' in email: # caso ele tenha colocado espaço no email
                print('email inválido1')
                continue
            elif '@' not in email: # caso ele não tenha colocado o @ no email
                print('email inválido2')
                continue
            elif not 'gmail.com' in email or 'ufrpe.br' in email:  # caso ele não tenha colocado nem gmail nem hotmail nem ufrpe
                print('email inválido3')
                continue
            elif 'ufrpe' in email and '.br' not in email: # Se ele usar ufrpe mas não por ".br", é inválido
                print('email inválido4')
                continue
            elif 'ufrpe' in email and len(email) < 11: # Se ele usar ufrpe e seu email tiver menos de 3 caracteres (antes do @), é inválido
                print('email inválido5')
                continue
            elif 'gmail' in email and len(email) < 13: # Se ele usar gmail ou hotmail
                print('email inválido6')
                continue     
            else:
                flag = False
    else:
        print('Digite apenas "s" ou "n"')
        continue