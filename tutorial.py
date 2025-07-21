import os

class Tutorial:
    def __init__(self):
        pass

    def clear(self): # Limpa tudo que estava no terminal anteriormente 
        os.system('cls' if os.name == 'nt' else 'clear')
    

    def mostrar_noticia(self, noticia): # Função do tutorial, as partes da noticia foram devidamente separadas.
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

    def executar_tutorial(self): #Função que mostra o corpo do tutorial
        self.clear()
        print('\n' + '='*30)
        print('\tTutorial Antifake')
        print('='*30)
        print('\nSeja bem vindo(a) ao tutorial do AntiFake!\n' 
            'Aqui você irá aprender os principais critérios para a identificação de Fake News!')
        input('Mas antes, vamos testar seu conhecimento atual. (Digite enter para continuar)')



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

        noticias_tutorial = [noticia1, noticia2, noticia3, noticia4, noticia5]
        for noticia in noticias_tutorial:
            self.mostrar_noticia(noticia)
            input('Digite enter para continuar')
            self.clear()
        input('Tutorial concluído! Digite enter para voltar ao menu')
