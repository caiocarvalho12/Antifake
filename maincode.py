import json
import os

ARQUIVO_USUARIOS = 'usuarios.json'

def clear(): # Limpa tudo que estava no terminal anteriormente 
    os.system('cls' if os.name == 'nt' else 'clear')  

def carregar_usuarios(): # Carrega os usuarios já logados ou cria um dicionário vazio
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return {}

def salvar_usuarios(usuarios): # Salva os dados do novo usuario adicionado ou novos dados de um usuario já existente
    with open(ARQUIVO_USUARIOS, 'w', encoding='utf-8') as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

def cadastrar_nome(): # Cadastra o nome do usuario, que estará associado ao email dele a ser adicionado depois
    while True:
        nome = input("Digite seu nome completo: ").strip()
        if all(c.isalpha() or c.isspace() for c in nome):
            if len(nome.split()) >= 2:
                return nome
            else:
                print("Nome inválido, digite seu nome completo.")
        else:
            print("Nome inválido! Use apenas letras e espaços.")

def cadastrar_data(): # Cadastra a data de nascimento do usuário (dd/mm/aaaa), está associada ao email 
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
        return data

def cadastrar_email(usuarios): # Cadastra o email do usuário, vai ser o que vai associar um usuario aos dados e a conta dele
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
            return email
        else:
            print('A confirmação falhou')

def cadastrar_senha(): # Cadastra a senha associada ao email do usuário.
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
            return senha
        else:
            print('Confirmação incorreta.')

def cadastrar_tipo(): # Há 3 tipos de usuários, aqui será especificado o tipo do usuario: estudante, professor ou amdin
    while True:
        tipo_usuario = input('Você é aluno(1) ou professor(2)? ').strip()
        if tipo_usuario not in ['1', '2', 'caio.samuel123']:
            print('usuário inválido, digite apenas "1" ou "2".')
        else:
            return tipo_usuario
        
def editar_dados(email): # No menu do Antifake está essa opção, o usuário tem o direito de fazer a modificação de seus dados se quiser
    clear()
    print('\n--- Editar dados ---')
    novo_nome = cadastrar_nome()
    nova_data = cadastrar_data()
    nova_senha = cadastrar_senha()
    usuarios[email]['nome'] = novo_nome
    usuarios[email]['data_nascimento'] = nova_data
    usuarios[email]['senha'] = nova_senha
    salvar_usuarios(usuarios)
    print('Dados atualizados!')
    input('Digite enter para continuar')

def ver_dados(email): # Opção do menu que mostra os dados do proprio usuário
    clear()
    print(json.dumps(usuarios[email], indent=4, ensure_ascii=False))
    input('Digite enter para continuar')
    
def deletar_conta(email): # No menu do antifake, também há a opção de deletar a própria conta 
    clear()
    ver_dados()
    confirmar = input('Tem certeza que deseja deletar sua conta? (s/n): ').strip().lower()
    if confirmar == 's':
        del usuarios[email]
        salvar_usuarios(usuarios)
        print('Conta deletada.')
        return True
    else:
        print('Ação cancelada.')
        return False

#Abaixo, tudo relacionado ao tutorial
def mostrar_noticia(noticia): # Função do tutorial, as partes da noticia foram devidamente separadas.
    print('\n' + '='*60)
    print(f'{noticia['manchete']}')
    print(f'Data: {noticia['data']}')
    print(f'Fonte: {noticia['fonte']}')
    print('-'*60)
    print(noticia['corpo'])
    print('-'*60)
    resposta = input("Essa notícia é verdadeira ou falsa? (v/f): ").strip().lower()
    print("\nAnálise:")
    print(noticia['criterio'])

def executar_tutorial(): #Função que mostra o corpo do tutorial
    clear()
    print('\n' + '='*30)
    print('\tTutorial Antifake')
    print('='*30)
    print('\nSeja bem vindo(a) ao tutorial do AntiFake!\n' 
        'Aqui você irá aprender os principais critérios para a identificação de Fake News!')
    input('Mas antes, vamos testar seu conhecimento atual. (Digite enter para continuar)')
            
    noticias_tutorial = [noticia1, noticia2, noticia3, noticia4, noticia5]
    for noticia in noticias_tutorial:
        mostrar_noticia(noticia)
        input('Digite enter para continuar')
        clear()
    input('Tutorial concluído! Digite enter para voltar ao menu')

# Notícias fictícias que serão mostradas como exemplo no tutorial:
noticia1 = {
    "manchete": "Novo estudo prova que refrigerante natural cura ansiedade",
    "data": "17/03/2024",
    "fonte": "www.saudealternativa.top",
    "corpo": (
        "Um novo estudo publicado pelo portal Saúde Alternativa afirma que tomar refrigerante "
        "de hibisco com gengibre ajuda a equilibrar neurotransmissores e, por isso, seria mais "
        "efetivo que remédios tradicionais no combate à ansiedade. A publicação ainda afirma que "
        "as grandes farmacêuticas escondem esses dados para manter o mercado de ansiolíticos ativo."
    ),
    "outras_fontes": [],
    "criterio": (
        "Esta notícia é **falsa**.\n\n"
        "O principal critério violado é a **confiabilidade da fonte**.\n"
        "O site 'saudealternativa.top' não é reconhecido por especialistas nem tem vínculo com "
        "instituições científicas. Nenhuma outra fonte confiável repercutiu essa informação. "
        "Sempre verifique se a fonte é confiável e conhecida."
    )
}
noticia2 = {
    "manchete": "Prefeitura confirma: aulas serão canceladas em toda a cidade",
    "data": "10/04/2024",
    "fonte": "www.noticiaslocal24h.com",
    "corpo": (
       "A Prefeitura divulgou uma nota informando o cancelamento das aulas nesta quarta-feira "
        "em algumas escolas da rede municipal localizadas na região central, devido a um problema "
        "na rede elétrica. As demais instituições da cidade continuam funcionando normalmente. "
        "O comunicado completo está disponível no site oficial da Prefeitura."
    ),
    "outras_fontes": ["G1", "JC Online"],
    "criterio": (
        "Esta notícia é **falsa** ou **enganosa**.\n\n"
        "O critério aqui é **ler além da manchete**.\n"
        "A manchete induz ao erro ao afirmar que TODAS as aulas foram canceladas, quando o corpo da "
        "notícia mostra que a suspensão se aplica apenas a algumas escolas. Manchetes sensacionalistas "
        "são comuns em fake news. Sempre leia a matéria completa!"
    )
}
noticia3 = {
    "manchete": "Novo vírus está se espalhando e causa febre hemorrágica",
    "data": "02/08/2017",
    "fonte": "www.alertasaude.com",
    "corpo": (
        "Autoridades sanitárias da Tailândia relataram casos isolados de um vírus identificado em "
        "primatas selvagens nas florestas tropicais do país. Segundo os especialistas, o vírus pode "
        "causar sintomas como febre alta e sangramentos internos em macacos infectados. Pesquisadores "
        "alertam para a necessidade de monitoramento, embora até o momento não existam registros de "
        "transmissão para humanos. O Ministério da Saúde local afirmou que não há motivo para pânico, "
        "mas recomenda evitar contato com animais silvestres na região afetada."
    ),
    "outras_fontes": ["BBC", "Reuters"],
    "criterio": (
        "Esta notícia é **enganosa**.\n\n"
        "O critério violado é **verificar a data**.\n"
        "Apesar de a informação ter sido parcialmente verdadeira em 2017, ela está descontextualizada "
        "e sendo usada para gerar alarde atualmente. Notícias antigas que voltam a circular fora de contexto "
        "são uma forma comum de desinformação."
    )
}
noticia4 = {
    "manchete": "Ministério da Educação cancela o ENEM deste ano por falta de verba",
    "data": "20/05/2024",
    "fonte": "www.educacaolivreja.org",
    "corpo": (
        "Em publicação feita na manhã desta segunda-feira, o portal Educação Livre Já afirmou que "
        "o Ministério da Educação teria anunciado o cancelamento do ENEM 2024 devido a restrições "
        "no orçamento federal. O texto cita fontes internas do MEC, mas não apresenta nomes ou "
        "documentos oficiais. A notícia ganhou grande repercussão em grupos estudantis nas redes sociais, "
        "principalmente no WhatsApp e Telegram."
    ),
    "outras_fontes": [],  # nenhuma fonte confiável
    "criterio": (
        "Esta notícia é **falsa**.\n\n"
        "O critério é **consultar mais de uma fonte**.\n"
        "Uma notícia tão importante como o cancelamento do ENEM estaria em grandes portais e "
        "seria informada pelo próprio MEC. Se apenas um site obscuro publica algo e nenhuma outra "
        "fonte confiável confirma, é motivo para duvidar!"
    )
}
noticia5 = {
    "manchete": "Menino de 8 anos morre após tomar vacina da gripe em hospital público",
    "data": "03/04/2024",
    "fonte": "www.urgenteviral.net",
    "corpo": (
        "Um menino de apenas 8 anos faleceu nesta semana, poucas horas após ter sido vacinado contra a gripe "
        "em um hospital público da zona sul de São Paulo. De acordo com relatos que circulam nas redes sociais, "
        "a criança começou a passar mal ainda na unidade de saúde, apresentando febre alta, tremores e confusão mental. "
        "A mãe, identificada apenas como 'Dona Márcia', afirma que não recebeu orientações sobre possíveis reações e alega "
        "negligência médica. \n\n"
        "“Meu filho era saudável, e depois da vacina tudo piorou”, escreveu em uma publicação emocionada.\n\n"
        "A reportagem não apresenta documentos oficiais, exames ou confirmação de autoridades médicas sobre a causa da morte. "
        "Apesar da gravidade do caso, não há registros do incidente em canais oficiais do Ministério da Saúde ou da Secretaria Municipal."
    ),
    "outras_fontes": [],  # nenhuma fonte confiável
    "criterio": (
        "Esta notícia é possivelmente **falsa**.\n\n"
        "O critério é **cuidado com apelos emocionais**.\n"
        "O objetivo aqui é causar choque e indignação para gerar compartilhamento. Quando uma notícia "
        "usa linguagem exagerada e não apresenta provas ou fontes verificáveis, é sinal de manipulação emocional."
    )
}
#Abaixo, todas as funções relacionadas ao docente:
def adicionar_aluno():
    clear()
    adicionar_email = input('digite o email do aluno: ')
    if adicionar_email not in usuarios:
        print('Esse email ainda não foi cadastrado')
    elif 'alunos' not in usuarios[email]:
        usuarios[email]['alunos'] = []
    elif usuarios[adicionar_email]['tipo'] != '1':
        print('Este usuário não está cadastrado como aluno')
    else:
        if adicionar_email in usuarios[email]['alunos']:
            print('Aluno já está adicionado.')
        else:
            usuarios[email]['alunos'].append(adicionar_email)
            salvar_usuarios(usuarios)
            print('Aluno adicionado com sucesso!')

#Início do programa de fato:
print('\n' + '='*30)
print('\tBem-vindo ao Antifake')
print('='*30)

usuarios = carregar_usuarios() # Já carrega todos os usuários já logados se houver algum
usuario_logado = None

while True: # Looping principal, se sair do menu antifake, vem pra este looping
    escolha = input('\nVocê já tem uma conta? (s)im / (n)ão / (sair): ').strip().lower()

    if escolha == 'sair':
        print('Encerrando o programa...')
        break

    elif escolha == 's':
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
        print('\nCadastre-se agora!')
        tipo_usuario = cadastrar_tipo()
        nome = cadastrar_nome()
        data_nascimento = cadastrar_data()
        email = cadastrar_email(usuarios)
        senha = cadastrar_senha()

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
        salvar_usuarios(usuarios)
        print('Cadastro realizado com sucesso!')
        usuario_logado = email
        break

    else:
        print('Digite apenas "s", "n" ou "sair".')
        continue
    
def menu_professor(email): #Função que mostra o menu direcionado ao professor, com as funcionalidade especificas dele
    while True:
        opcao = input('\nEscolha:\n'
                    '(1) Ver dados\n'
                    '(2) Editar dados\n'
                    '(3) Deletar conta\n'
                    '(4) adicionar alunos\n'
                    '(5) Ver desempenho dos alunos\n'
                    '(0) Sair do menu\n> ').strip()
                        
        if opcao == '1':
            ver_dados(email)

        elif opcao == '2':
            editar_dados(email)

        elif opcao == '3':
            if deletar_conta(email):
                return 

        elif opcao == '4': # O docente pode adicionar o email de qualquer discente para ver o desempenho do mesmo
            adicionar_aluno()

        elif opcao == '0':
            print('Voltando ao menu principal...')
            break

        else:
            print('Função ainda não implementada.')
    
def menu_aluno(email): #Função que mostra o menu direcionado ao aluno, com as funcionalidade especificas dele
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
            ver_dados(email)

        elif opcao == '2':
            editar_dados(email)

        elif opcao == '3':
            if deletar_conta(email):
                return
        
        elif opcao == '4':
            executar_tutorial()

        elif opcao == '0':
            print('Voltando ao menu principal...')
            break
        else:
            print('Função ainda não implementada.')

def menu_admin(email): #Função que mostra o menu direcionado ao admin, com as funcionalidade especificas dele
    while True:
        opcao = input('\nEscolha:\n'
                    '(1) Ver dados\n'
                    '(2) Editar dados\n'
                    '(3) Deletar conta\n'
                    '(4) inserir noticias\n'
                    '(5) ver noticias já inseridas\n'
                    '(0) Sair do menu\n> ').strip()

        if opcao == '1':
            ver_dados(email)

        elif opcao == '2':
            editar_dados(email)

        elif opcao == '3':
            if deletar_conta(email):
                return

        elif opcao == '0':
            print('Voltando ao menu principal...')
            break
        else:
            print('Função ainda não implementada.')

if usuario_logado: # O menu irá variar de acordo com o usuário
    if usuarios[usuario_logado]['tipo'] == '1':
        menu_aluno(usuario_logado)
    elif usuarios[usuario_logado]['tipo'] == '2':
        menu_professor(usuario_logado)
    elif usuarios[usuario_logado]['tipo'] == 'admin':
        menu_admin(usuario_logado)
else:
    print('Nenhum usuário logado. Encerrando programa.')