# Chatbot IA Tempo Real

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
![Deploy on Render](https://img.shields.io/badge/Render-Deployed-green?logo=render)

Chatbot em Flask + SocketIO para comunicação web em tempo real, **pronto para rodar localmente ou ser hospedado gratuitamente no Render**.

---

## 🔖 Sumário

- [Funcionalidades](#funcionalidades)
- [Rodando Localmente](#rodando-localmente)
- [Deploy na Nuvem (Render)](#deploy-na-nuvem-render)
- [Dicas para Funcionamento no Render](#dicas-para-funcionamento-no-render)
- [Soluções de Problemas Comuns](#soluções-de-problemas-comuns)
- [Sobre Licença](#sobre-licença)

---

## ✨ Funcionalidades

- Chat em tempo real (SocketIO)
- Interface web simples (`templates/index.html`)
- Deploy fácil (Render: escolha "Virgínia" para menor latência BR)
- Repositório didático para projetos de estudo e portfólio

---

## 🚀 Rodando Localmente

Clone e rode:

```bash
git clone https://github.com/dalessandrosantos/chatbot-ia-tempo-real.git
cd chatbot-ia-tempo-real

python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

Acesse [http://localhost:5000](http://localhost:5000) no navegador.

---

## ☁️ Deploy na Nuvem (Render)

1. Crie uma conta em [render.com](https://render.com)
2. Clique em "New Web Service" e vincule seu repositório.
3. Preencha:
    - **Região:** Virgínia ou Ohio
    - **Build command:**  
      ```bash
      pip install -r requirements.txt
      ```
    - **Start command:**  
      ```bash
      python app.py
      ```
    - **Tipo de instância:** “Livre” (plano gratuito)
4. Aguarde o deploy. Acesse a URL gerada ao final!
5. Todo push no GitHub faz deploy automático.

---

## ❓ Soluções de problemas comuns

- **O chat fica em branco:** Verifique a conexão do SocketIO (verifique o console do navegador) e se o `transports: ['polling']` está correto.
- **Deploy demora/“dorme”:** Instâncias gratuitas no Render “hibernam” sem uso e levam até 1min para reativar.
- **Erros estranhos:** Veja os logs em “Registros” no Render.

---

## 📁 Estrutura do projeto

```
├── app.py                # código principal Flask/SocketIO
├── requirements.txt      # dependências do Python
└── templates/
    └── index.html        # interface do chatbot
```

---

## 📋 Comandos Git

```bash
git add .
git commit -m "sua mensagem"
git push
# O Render faz deploy automático!
```

---

## 🔗 Links úteis

- [Render](https://render.com)
- [Documentação Flask](https://flask.palletsprojects.com/)
- [Documentação Flask-SocketIO](https://flask-socketio.readthedocs.io/)
- [Socket.IO JS](https://socket.io/docs/v4/)

---

## 📝 Sobre Licença

Este projeto está sob a [licença MIT](LICENSE).  
Você pode usar, modificar e compartilhar – só mantenha este aviso no projeto!

---
