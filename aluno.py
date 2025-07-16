import os
from usuario import Usuario
from noticia import Noticia

class Aluno(Usuario):
    def __init__(self):
        pass
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def menu_aluno(self, email, usuarios): #Função que mostra o menu direcionado ao aluno, com as funcionalidade especificas dele
        usuario = Usuario()
        noticia = Noticia()
        while True:
            opcao = input('\nEscolha:\n'
                        '(1) Ver dados\n'
                        '(2) Editar dados\n'
                        '(3) Deletar conta\n'
                        '(4) Ver tutorial\n'
                        '(5) Ir para questionário\n'
                        '(6) Ver feedback\n'
                        '(0) Sair do menu\n> ').strip()

            if opcao == '1':
                usuario.ver_dados(email, usuarios)

            elif opcao == '2':
                usuario.editar_dados(email, usuarios)

            elif opcao == '3':
                if usuario.deletar_conta(email, usuarios):
                    return
            
            elif opcao == '4':
                noticia.executar_tutorial()

            elif opcao == '0':
                print('Voltando ao menu principal...')
                return
            else:
                print('Função ainda não implementada.')