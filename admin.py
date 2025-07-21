import time
from usuario import Usuario
from noticia import Noticia

class Admin(Usuario):
    def __init__(self, email, usuarios, url, noticias):
        self.email = email
        self.usuarios = usuarios
        self.url = url
        self.noticias = noticias
    def inserir_noticias(self):
        print('Função ainda não implementada.')
    def ver_noticias(self):
        print('Função ainda não implementada.')
    def menu_admin(self, email, usuarios, url, noticias): #Função que mostra o menu direcionado ao admin, com as funcionalidade especificas dele
        usuario = Usuario()
        noticia = Noticia()
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
                noticia.inserir_noticias(url, noticias)

            elif opcao == '5':
                noticia.ver_noticias(url, noticias)
                
            elif opcao == '0':
                print('Voltando a tela de login...')
                for hora in range(1,2):
                    print('Carregando login...')
                    time.sleep(2)
                return
            else:
                return