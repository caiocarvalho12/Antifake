# AntiFake: Plataforma Educacional para o Combate à Desinformação

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange?style=flat)
![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-green?style=flat) ## 📚 Descrição do Projeto

O AntiFake é uma plataforma educacional desenvolvida para capacitar indivíduos de todas as idades a identificar e combater a crescente disseminação de desinformação online. Reconhecendo que a proliferação de "Fake News" é um problema social significativo e em constante evolução, nosso projeto visa fornecer ferramentas interativas e metodologias de treinamento para fomentar o pensamento crítico e transformar usuários em avaliadores conscientes da informação digital.

## ✨ Funcionalidades

O projeto AntiFake inclui as seguintes funcionalidades principais (algumas em desenvolvimento, mas projetadas para serem integradas na versão final):

* **Gerenciamento de Usuários:** Cadastro, login, edição de perfil e exclusão de conta para diferentes tipos de usuários (Alunos, Professores, Administradores).
* **Perfis de Usuário:** Experiências personalizadas para Alunos, Professores e Administradores, com menus e opções específicas para cada tipo.
* **Módulo de Tutorial Interativo:** Apresenta exemplos de notícias (verificadas como "Fato" ou "Fake" de fontes como o G1) e explica os critérios essenciais para identificar desinformação (ex: confiabilidade da fonte, leitura além da manchete, verificação da data, apelo emocional).
* **Módulo de Questionário (Projetado):** Avaliação compreensiva do entendimento dos usuários sobre os critérios de identificação de Fake News, reforçando o aprendizado.
* **Funcionalidades para Professores (Projetado):** Adição e gerenciamento de alunos, e (futuramente) visualização do desempenho dos alunos nos questionários.
* **Funcionalidades para Administradores (Projetado):** Inserção e gerenciamento de notícias para o tutorial e questionários.

## 🚀 Como Executar o Projeto

Para executar o AntiFake em sua máquina local, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado em seu sistema.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```
    (Substitua `seu-usuario/seu-repositorio` pelo caminho real do seu repositório no GitHub)

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd nome-do-repositorio-antifake
    ```

### Execução

1.  **Execute o script principal:**
    ```bash
    python main.py
    ```
    O programa iniciará no terminal, onde você poderá criar uma conta, fazer login e explorar as funcionalidades.

## 🏗️ Estrutura do Projeto (Em Desenvolvimento)

* `main.py`: O script principal que contém a lógica de execução do programa e as funções de gerenciamento de usuários, tutorial, etc.
* `usuarios.json`: Arquivo JSON para persistência dos dados de usuário (nomes, emails, senhas, tipo de usuário).
* `noticias.json` (A ser implementado): Arquivo JSON para armazenamento das notícias usadas no tutorial/questionário.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Bibliotecas Padrão do Python:** `json` (para manipulação de dados), `os` (para comandos de sistema, como `clear`).

## 🔮 Próximas Etapas e Propostas Futuras

Este projeto está em desenvolvimento contínuo. As futuras funcionalidades e expansões planejadas incluem:

* **Modularização do Código:** Reestruturação para um design mais modular e escalável.
* **Implementação Completa do Módulo de Questionário:** Desenvolvimento de um sistema robusto de questionários para avaliação do aprendizado.
* **Feedback Personalizado:** Geração de feedback individualizado com base no desempenho do usuário no questionário.
* **Sistema de Pontuação e Níveis:** Introdução de elementos de gamificação para aumentar o engajamento e a progressão do usuário como "investigador".
* **Expansão da Base de Dados de Notícias:** Inclusão de mais exemplos de notícias e critérios de diferentes fontes.
* **Integração com Conteúdo em Tempo Real:** Potencialmente, analisar e permitir a avaliação de notícias recentes.
* **Ampliação do Público-Alvo:** Adaptações para atender a necessidades específicas de diferentes grupos etários ou educacionais.

## 👥 Contribuintes

* [Caio Cordeiro Gomes Carvalho] - [@caiocarvalho12](https://github.com/SeuUsuarioGitHub)
* [Nome Completo do seu Amigo] - [@UsuarioGitHubDoAmigo](https://github.com/UsuarioGitHubDoAmigo)

---

Lembre-se de substituir os placeholders como `seu-usuario/seu-repositorio`, `nome-do-repositorio-antifake`, `SeuUsuarioGitHub`, `UsuarioGitHubDoAmigo` pelos valores corretos do seu projeto e perfil no GitHub.

Este `README` deve dar uma excelente primeira impressão e fornecer todas as informações necessárias para quem quiser entender e executar seu projeto!
