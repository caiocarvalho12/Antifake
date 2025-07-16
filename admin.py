import os
from usuario import Usuario

class Admin(Usuario):
    def __init__(self):
        pass
    def inserir_noticias(self):
        print('Função ainda não implementada.')
    def ver_noticias(self):
        print('Função ainda não implementada.')
    def menu_admin(self, email, usuarios): #Função que mostra o menu direcionado ao admin, com as funcionalidade especificas dele
        usuario = Usuario()
        while True:
            opcao = input('\nEscolha:\n'
                        '(1) Ver dados\n'
                        '(2) Editar dados\n'
                        '(3) Deletar conta\n'
                        '(4) Inserir noticias\n'
                        '(5) Ver noticias já inseridas\n'
                        '(0) Sair do menu\n> ').strip()

            if opcao == '1':
                usuario.ver_dados(email, usuarios)

            elif opcao == '2':
                usuario.editar_dados(email, usuarios)

            elif opcao == '3':
                if usuario.deletar_conta(email, usuarios):
                    return
            elif opcao == '4':
                self.inserir_noticias()

            elif opcao == '5':
                self.ver_noticias()
                
            elif opcao == '0':
                print('Voltando ao menu principal...')
                return
            else:
                print('Função ainda não implementada.')