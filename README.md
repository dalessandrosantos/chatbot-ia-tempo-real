# Chatbot IA Tempo Real

Chatbot web em Python com Flask e SocketIO para comunicação em tempo real.  
Permite conversas instantâneas por navegador (local ou online), ideal para demonstrações, estudos e portfólio.  
**Deploy fácil e gratuito no Render!**

---

## 📑 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Rodando Localmente (Passo a Passo)](#rodando-localmente-passo-a-passo)
- [Deploy Grátis no Render (Passo a Passo)](#deploy-grátis-no-render-passo-a-passo)
- [Comandos Git Básicos](#comandos-git-básicos)
- [Dicas para o Chat no Render](#dicas-para-o-chat-no-render)
- [Estrutura do Projeto](#estrutura-do-projeto)
---

## Sobre o Projeto

- **Tecnologias:** Python, Flask, Flask-SocketIO, HTML/CSS/JS (web), Render (deploy cloud)
- **Funcionalidades:**
  - Chat web em tempo real
  - Deploy em nuvem com um clique
  - Código fácil de personalizar

---

## Pré-requisitos

- [Git](https://git-scm.com/) instalado
- [Python 3.8+](https://www.python.org/)
- Conta no [GitHub](https://github.com/) (para versionar e deploy cloud)
- (Opcional) Conta no [Render](https://render.com/) para deploy online

---

## Rodando Localmente (Passo a Passo)

1. **Clone o projeto do GitHub:**
    ```bash
    git clone https://github.com/dalessandrosantos/chatbot-ia-tempo-real.git
    cd chatbot-ia-tempo-real
    ```

2. **Crie um ambiente virtual (recomendado):**
    - No Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```
    - No macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Rode o servidor local:**
    ```bash
    python app.py
    ```
5. **Acesse no navegador:**  
   [http://localhost:5000](http://localhost:5000)

---

## Deploy Grátis no Render (Passo a Passo)

1. **Crie uma conta** em [https://render.com](https://render.com) e conecte seu GitHub.

2. **No painel do Render:**
    - Clique em **"New Web Service"**
    - Selecione seu repositório `chatbot-ia-tempo-real`.

3. **Configure:**
    - **Região:** Escolha uma região próxima (Virgínia/Ohio)
    - **Build Command:**  
      `pip install -r requirements.txt`
    - **Start Command:**  
      `python app.py`
    - Tipo de instância: pode escolher a grátis (“Free”)

4. **Deploy automático:**  
   - O Render vai clonar seu repositório, instalar dependências e rodar sua aplicação.
   - Ao final, será exibida uma URL do tipo:  
     `https://chatbot-ia-tempo-real.onrender.com`
   - Clique e acesse seu chatbot online!

5. **Atualizando o deploy:**  
    Sempre que fizer mudanças no código e der `git push`, o Render atualiza sozinho.

---

## Comandos Git Básicos

Sempre que editar algo, faça assim pelo terminal:

```bash
git add .
git commit -m "sua mensagem explicando o que mudou"
git push
```
Pronto! O código vai pro GitHub e, se seu Render estiver conectado, o deploy roda automaticamente.

---

## Dicas para o Chat no Render

- Para que o chat funcione no Render **(especialmente no plano gratuito)**, garanta que no seu arquivo `index.html` está assim:

    ```js
    var socket = io({
      transports: ['polling']
    });
    ```
    Isso evita problemas de conexão devido aos proxies/filtros do Render.

- **Atenção:** Deploy em ambiente gratuito pode demorar para “acordar” se estiver inativo.

- Se der erro no Render dizendo "`Werkzeug não projetado para produção`", adicione o argumento `allow_unsafe_werkzeug=True` no `socketio.run`:
    ```python
    socketio.run(app, host='0.0.0.0', port=port, allow_unsafe_werkzeug=True)
    ```
    (Procure essa linha no `app.py`.)

---

## Estrutura do Projeto

```
├── app.py                # Backend Flask + SocketIO
├── requirements.txt      # Dependências do Python
└── templates/
    └── index.html        # Interface web do chat
```
