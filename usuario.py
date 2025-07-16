import json
import os

ARQUIVO_USUARIOS = 'usuarios.json'

class Usuario:
    def __init__(self):
        self.nome = None
        self.data = None
        self.email = None
        self.senha = None
        self.tipo_usuario = None    
        
    def clear(self): # Limpa tudo que estava no terminal anteriormente 
        os.system('cls' if os.name == 'nt' else 'clear')  
    
    @staticmethod
    def carregar_usuarios(): # Carrega os usuarios já logados ou cria um dicionário vazio
        if os.path.exists(ARQUIVO_USUARIOS):
            with open(ARQUIVO_USUARIOS, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        return {}

    def salvar_usuarios(self, usuarios): # Salva os dados do novo usuario adicionado ou novos dados de um usuario já existente
        with open(ARQUIVO_USUARIOS, 'w', encoding='utf-8') as arquivo:
            json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

    def cadastrar_nome(self): # Cadastra o nome do usuario, que estará associado ao email dele a ser adicionado depois
        while True:
            nome = input("Digite seu nome completo: ").strip()
            if all(c.isalpha() or c.isspace() for c in nome):
                if len(nome.split()) >= 2:
                    self.nome = nome
                    return nome
                else:
                    print("Nome inválido, digite seu nome completo.")
            else:
                print("Nome inválido! Use apenas letras e espaços.")

    def cadastrar_data(self): # Cadastra a data de nascimento do usuário (dd/mm/aaaa), está associada ao email 
        while True:
            data = input('Digite sua data de nascimento (dd/mm/aaaa): ')
            partes = data.split('/')
            if len(partes) != 3:
                print('Formato inválido, use dd/mm/aaaa.')
                continue
            dia, mes, ano = partes
            if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
                print('Use apenas números e "/" para dividir.')
                continue
            dia, mes, ano = int(dia), int(mes), int(ano)
            if not 1 <= mes <= 12 or not 1900 < ano <= 2025:
                print('Data de nascimento inválida.')
                continue
            if mes == 2:
                if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)): # Condição de ano bissexto o ano 
                    if not 1 <= dia <= 29:
                        print('Dia inválido para fevereiro em ano bissexto.')
                        continue
                else:
                    if not 1 <= dia <= 28:
                        print('Dia inválido para fevereiro.')
                        continue
            elif mes in [4, 6, 9, 11] and not 1 <= dia <= 30:
                print('Esse mês tem no máximo 30 dias.')
                continue
            elif not 1 <= dia <= 31:
                print('Dia inválido.')
                continue
            self.data = data
            return data

    def cadastrar_email(self, usuarios): # Cadastra o email do usuário, vai ser o que vai associar um usuario aos dados e a conta dele
        while True:
            email = input('Digite seu email: ').strip()
            if ' ' in email:
                print('Email inválido: contém espaços.')
                continue
            if '@' not in email:
                print('Email inválido: falta "@"')
                continue
            if not ('gmail.com' in email or 'ufrpe.br' in email):
                print('Use domínios "gmail.com" ou "ufrpe.br".')
                continue
            if len(email.split('@')[0]) < 3: # Antes do caractere "@" deve haver pelo menos 3 caracteres
                print('Email inválido: parte antes do @ muito curta.')
                continue
            if email in usuarios:
                print('Esse email já está cadastrado.')
                continue
            confirmação_email = input('Confirme o email: ')
            if confirmação_email == email:
                self.email = email
                return email
            else:
                print('A confirmação falhou')

    def cadastrar_senha(self): # Cadastra a senha associada ao email do usuário.
        while True:
            senha = input('Digite sua senha (mín. 8 caracteres): ')
            if len(senha) < 8:
                print('Senha muito curta.')
                continue
            if senha.isalpha() or senha.isdigit():
                tentar = input('Senha fraca. Quer tentar outra? (s/n): ').strip().lower()
                if tentar.startswith('s'):
                    continue
            confirmacao = input('Confirme sua senha: ')
            if senha == confirmacao:
                self.senha = senha
                return senha
            else:
                print('Confirmação incorreta.')

    def cadastrar_tipo(self): # Há 3 tipos de usuários, aqui será especificado o tipo do usuario: estudante, professor ou amdin
        while True:
            tipo_usuario = input('Você é aluno(1) ou professor(2)? ').strip()
            if tipo_usuario not in ['1', '2', 'caio.samuel123']:
                print('usuário inválido, digite apenas "1" ou "2".')
            else:
                self.tipo_usuario = tipo_usuario
                return tipo_usuario
            
    def editar_dados(self, email, usuarios): # No menu do Antifake está essa opção, o usuário tem o direito de fazer a modificação de seus dados se quiser
        self.clear()
        print('\n--- Editar dados ---')
        novo_nome = self.cadastrar_nome()
        nova_data = self.cadastrar_data()
        nova_senha = self.cadastrar_senha()
        usuarios[email]['nome'] = novo_nome
        usuarios[email]['data_nascimento'] = nova_data
        usuarios[email]['senha'] = nova_senha
        self.salvar_usuarios(usuarios)
        print('Dados atualizados!')
        input('Digite enter para continuar')

    def ver_dados(self, email, usuarios): # Opção do menu que mostra os dados do proprio usuário
        self.clear()
        print(json.dumps(usuarios[email], indent=4, ensure_ascii=False))
        input('Digite enter para continuar')
        
    def deletar_conta(self, email, usuarios): # No menu do antifake, também há a opção de deletar a própria conta 
        self.clear()
        self.ver_dados(email, usuarios)
        confirmar = input('Tem certeza que deseja deletar sua conta? (s/n): ').strip().lower()
        if confirmar == 's':
            del usuarios[email]
            self.salvar_usuarios(usuarios)
            print('Conta deletada.')
            return True
        else:
            print('Ação cancelada.')
            return False
    