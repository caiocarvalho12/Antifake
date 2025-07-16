import os
from usuario import Usuario

class Professor(Usuario):
    def __init__(self):
        pass
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def adicionar_aluno(self, email, usuarios):
        self.clear()
        adicionar_email = input('digite o email do aluno: ')
        if adicionar_email not in usuarios:
            print('Esse email ainda não foi cadastrado')
        elif usuarios[adicionar_email]['tipo'] != '1':
            print('Este usuário não está cadastrado como aluno')
        else:
            if 'alunos' not in usuarios[email]:
                usuarios[email]['alunos'] = []
            if adicionar_email in usuarios[email]['alunos']:
                print('Aluno já está adicionado.')
            else:
                usuarios[email]['alunos'].append(adicionar_email)
                Usuario.salvar_usuarios(usuarios)
                print('Aluno adicionado com sucesso!')


    def menu_professor(self, usuario_logado, usuarios): #Função que mostra o menu direcionado ao professor, com as funcionalidade especificas dele
        usuario = Usuario()
        while True:
            opcao = input('\nEscolha:\n'
                        '(1) Ver dados\n'
                        '(2) Editar dados\n'
                        '(3) Deletar conta\n'
                        '(4) Adicionar alunos\n'
                        '(5) Ver desempenho dos alunos\n'
                        '(0) Sair do menu\n> ').strip()
                            
            if opcao == '1':
                usuario.ver_dados(usuario_logado, usuarios)

            elif opcao == '2':
                usuario.editar_dados(usuario_logado, usuarios)

            elif opcao == '3':
                if usuario.deletar_conta(usuario_logado, usuarios):
                    return 

            elif opcao == '4': # O docente pode adicionar o email de qualquer discente para ver o desempenho do mesmo
                self.adicionar_aluno(usuario_logado, usuarios)

            elif opcao == '0':
                print('Voltando ao menu principal...')
                return

            else:
                print('Função ainda não implementada.')