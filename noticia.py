import json
import os

ARQUIVOS_NOTICIAS = 'noticias.json'

class Noticia:
    def __init__(self):
        pass

    def clear(self): # Limpa tudo que estava no terminal anteriormente 
        os.system('cls' if os.name == 'nt' else 'clear')

    def cadastrar_manchete(self):
        while True:
            manchete = input("Insira a manchete da notícia: ").strip()
            if manchete:
                return manchete
            else:
                print("Manchete não pode ser vazia. Tente novamente.")

    def cadastrar_data(self): # Cadastra a data da notícia (dd/mm/aaaa), está associada ao URL 
        while True:
            data = input('Digite a data da postagem da notícia (dd/mm/aaaa): ')
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
                print('Data de postagem inválida.')
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

    def cadastrar_url(self, noticias): # Cadastra a URL do notícia, vai ser o que vai associar uma notícia aos dados dela
        while True:
            url = input('Digite a URL da notícia: ').strip()
            if not url:
                print('A URL não pode estar vazia.')
                continue
            if ' ' in url:
                print('URL inválida: contém espaços.')
                continue
            if not (url.startswith('http://') or url.startswith('https://')):
                print('URL inválida: deve começar com "http://" ou "https://".')
                continue
            if not any(ext in url for ext in ['.com', '.org', '.gov']):
                print('URL inválida: domínio não reconhecido (ex: .com, .org, .gov).')
                continue
            if url in noticias:
                print('Essa notícia já está cadastrada.')
                continue
            return url
            
    def cadastrar_fonte(self):
        while True:
            fonte = input("Insira a fonte da notícia: ").strip()
            if fonte:
                return fonte
            else:
                print("A fonte não pode ser vazia. Tente novamente.")

    def cadastrar_corpo(self):
        while True:
            corpo = input("Insira o corpo da notícia: ").strip()
            if corpo:
                return corpo
            else:
                print("O corpo da notícia não pode ser vazio. Tente novamente.")

    def cadastrar_outrasFontes(self):
        while True:
            outras_fontes = input('Insira a outras fontes que compõem da notícia: ')
            return outras_fontes
    
    def cadastrar_veracidade(self):
        while True:
            veracidade = input('Insira a veracidade da notícia: ').strip().lower()
            if veracidade in ['verdadeira', 'falsa']:
                return veracidade
            else:
                print("A veracidade não pode ser vazia. Tente Novamente")


    def cadastrar_criterio(self):
        while True:
            criterio = input('Insira o critério para verificação da notícia: ').strip()
            if criterio:
                return criterio
            else:
                print("O critério de verificação de verecidade não pode ser vazio. Tente novamente.")
                    
    @staticmethod
    def carregar_noticias():
        if os.path.exists(ARQUIVOS_NOTICIAS):
            with open(ARQUIVOS_NOTICIAS, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        return {}

    def salvar_noticias(self, noticias): # Salva os dados de uma nova noticia adicionada
        with open(ARQUIVOS_NOTICIAS, 'w', encoding='utf-8') as arquivo:
            json.dump(noticias, arquivo, indent=4, ensure_ascii=False)

    def inserir_noticias(self, url, noticias):    
        while True:
            self.clear()
            print('\nInsira uma nova notícia!')
            url = self.cadastrar_url(noticias)
            fonte = self.cadastrar_fonte()
            manchete = self.cadastrar_manchete()
            data = self.cadastrar_data()
            corpo = self.cadastrar_corpo()
            while True:
                veracidade = self.cadastrar_veracidade()   
                if veracidade == 'falsa':
                    criterio = self.cadastrar_criterio()
                else:
                    criterio = None
                break

            noticias[url] = {
                    'fonte': fonte,
                    'manchete': manchete,
                    'data': data,
                    'corpo': corpo,
                    'veracidade': veracidade,
                    'criterio': criterio
                }

            self.salvar_noticias(noticias)
            print('Notícia cadastrada com sucesso!')
            break

    def ver_noticias(self):
        self.clear()
        noticias = self.carregar_noticias()
        if not noticias:
            print("Nenhuma notícia cadastrada ainda.")
        else:
            print("Todas as notícias cadastradas:\n")
            for url, dados in noticias.items():
                print(f"URL: {url}")
                for chave, valor in dados.items():
                    if valor is not None:
                        print(f"  {chave.capitalize()}: {valor}")
                print("-" * 40)
        input("\nPressione ENTER para voltar ao menu.")