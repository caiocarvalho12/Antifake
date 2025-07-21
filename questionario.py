import json
import os
import random
from noticia import Noticia

ARQUIVO_USUARIOS = 'usuarios.json'
ARQUIVO_NOTICIAS = 'noticias.json'
ARQUIVO_RESULTADOS = 'resultados.json'

class Questionario(Noticia):
    def __init__(self):
        self.pontuacao = 0

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def executar_questionario(self):
        noticia = Noticia()
        self.clear()
        print("=== QUESTIONÁRIO ANTIFAKE ===\n")

        noticias = noticia.carregar_noticias()

        if len(noticias) < 10:
            print(f"Ainda não há 10 notícias cadastradas. Atualmente há {len(noticias)}.")
            input("Digite Enter para voltar...")
            return

        urls_sorteadas = random.sample(list(noticias.keys()), 10)

        for i, url in enumerate(urls_sorteadas, 1):
            noticia = noticias[url]
            print(f"Questão {i}:")
            print(f"Manchete: {noticia['manchete']}")
            print(f"Fonte: {noticia['fonte']}")
            print(f"Data: {noticia['data']}")
            print(f"Corpo: {noticia['corpo']}\n")

            while True:
                resposta = input("Essa notícia é verdadeira ou falsa? ").strip().lower()
                if resposta not in ['verdadeira', 'falsa']:
                    print("Digite apenas 'verdadeira' ou 'falsa'.")
                    continue
                break

            if resposta == noticia['veracidade'].strip().lower():
                print("Resposta correta!\n")
                self.pontuacao += 1
            else:
                print("Resposta incorreta.")
                print(f"A veracidade correta é: {noticia['veracidade']}")
                if noticia['veracidade'].strip().lower() == 'falsa' and noticia.get('criterio'):
                    print(f"Critério de verificação: {noticia['criterio']}")
                print()

            input("Pressione Enter para continuar...\n")
            self.clear()

        print(f"\n--- Fim do questionário ---")
        print(f"Sua pontuação: {self.pontuacao} de 10")
        if self.pontuacao <= 6:
            print('Sua pontuação foi baixa, continue treinando para evoluir ;)')
        elif self.pontuacao == 10:
            print('Você obteve a pontuação máxima, parabéns por isso!!!')
        else:
            print('Sua pontuação está acima da média, continue treinando para obter a pontuação máxima :)')
        input("\nDigite Enter para voltar ao menu.")

    def salvar_resultado(self, email, pontuacao, total=10):
        resultados = {}
        if os.path.exists(ARQUIVO_RESULTADOS):
            with open(ARQUIVO_RESULTADOS, 'r', encoding='utf-8') as arq:
                try:
                    resultados = json.load(arq)
                except json.JSONDecodeError:
                    resultados = {} 
        resultados[email] = {
            "pontuacao": pontuacao,
            "total": total
        }
        with open(ARQUIVO_RESULTADOS, 'w', encoding='utf-8') as arq:
            json.dump(resultados, arq, indent=4, ensure_ascii=False)

    def ver_feedbacks(self):
        with open('resultados.json', 'r', encoding='utf-8') as arq:
            resultados = json.load(arq)

        print("=== RESULTADOS DE TODOS OS ALUNOS ===\n")
        for email, dados in resultados.items():
            print(f"{email}: {dados['pontuacao']}/{dados['total']}")