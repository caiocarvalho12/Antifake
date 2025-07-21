import os
import time
from usuario import Usuario
from professor import Professor
from aluno import Aluno
from admin import Admin


def clear(): # Limpa tudo que estava no terminal anteriormente 
    os.system('cls' if os.name == 'nt' else 'clear') 


#Início do programa de fato:
while True:    
    clear()
    print('\n' + '='*30)
    print('\tBem-vindo ao Antifake')
    print('='*30)

    usuarios = Usuario.carregar_usuarios()
    usuario = Usuario()
    usuario_logado = None
    aluno = Aluno()
    professor = Professor()
    admin = Admin()
    url = []
    noticias = {}


    while True: # Looping principal, se sair do menu antifake, vem pra este looping
        escolha = input('\nVocê já tem uma conta? (s)im / (n)ão / (sair): ').strip().lower()

        if escolha == 'sair':
            print('Encerrando o programa...')
            break

        elif escolha == 's':
            for hora in range(1,2):
                print('Carregando login...')
                time.sleep(2)
            clear()
            email = input('Digite seu email: ')
            senha = input('Digite sua senha: ')
            if email in usuarios and usuarios[email]['senha'] == senha:
                print(f'\nBem-vindo de volta, {usuarios[email]['nome']}!')
                usuario_logado = email
                break
            else:
                print('Email ou senha incorretos.')
                continue

        elif escolha == 'n':
            for hora in range(1,2):
                print('Carregando cadastro...')
                time.sleep(2)
            clear()
            print('\nCadastre-se agora!')
            novo_usuario = Usuario()
            tipo_usuario = novo_usuario.cadastrar_tipo()
            nome = novo_usuario.cadastrar_nome()
            data_nascimento = novo_usuario.cadastrar_data()
            email = novo_usuario.cadastrar_email(usuarios)
            senha = novo_usuario.cadastrar_senha()

            # Dentro do dicionário usuários, serão cadastrados esses dados caso o usuário seja um aluno        
            if tipo_usuario == '1':
                usuarios[email] = {
                    'nome': nome,
                    'data_nascimento': data_nascimento,
                    'senha': senha,
                    'tipo': tipo_usuario
                }

            # Dentro do dicionário usuários, serão cadastrados esses dados caso o usuário seja um professor
            elif tipo_usuario == '2':
                usuarios[email] = {
                    'nome': nome,
                    'data_nascimento': data_nascimento,
                    'senha': senha,
                    'tipo': tipo_usuario,
                    'alunos': []
                }
            
            # Dentro do dicionário usuários, serão cadastrados esses dados caso o usuário seja um admin
            elif tipo_usuario == 'caio.samuel123':
                usuarios[email] = {
                    'nome': nome,
                    'data_nascimento': data_nascimento,
                    'senha': senha,
                    'tipo': 'admin'
                }
            novo_usuario.salvar_usuarios(usuarios)
            print('Cadastro realizado com sucesso!')
            usuario_logado = email
            break

        else:
            print('Digite apenas "s", "n" ou "sair".')
            continue
        
    if usuario_logado: # O menu irá variar de acordo com o usuário
        if usuarios[usuario_logado]['tipo'] == '1':
            aluno.menu_aluno(usuario_logado, usuarios)
        elif usuarios[usuario_logado]['tipo'] == '2':
            professor.menu_professor(usuario_logado, usuarios)
        elif usuarios[usuario_logado]['tipo'] == 'admin':
            admin.menu_admin(usuario_logado, usuarios, url, noticias)
    else:
        print('Nenhum usuário logado. Encerrando programa.')
