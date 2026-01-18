# Passo 1: Bibliotecas necessárias

# Instalação das bibliotecas
# Flask – pip install flask
# Socketio – pip install python-socketio / pip install flask-socketio
# Simple Websocket – pip install simple-websocket


# Passo 2: Código em Python
from flask import Flask, render_template # estruturas para criar o site
from flask_socketio import SocketIO, send # estruturas para criar o chat
import os # estruturas para interagir com o sistema operacional de maneira eficiente

app = Flask(__name__) # cria o site
app.config["SECRET"] = "ajudahelp123ajudahelp" # chave de segunraça, pode ser qualquer coisa, mas escolha algo difícil
app.config["DEBUG"] = False # para testar o código, no final eu tiro
socketio = SocketIO(app, cors_allowed_origins="*") # cria a conexão entre diferentes máquinas que estão no mesmo site

@socketio.on("message") # define que a função abaixo vai ser acionada quando o evento de "message" acontecer

def gerenciar_mensagens(mensagem):
    print(f"Mnesagem: {mensagem}")
    send(mensagem, broadcast=True) # envia a mensagem para todo mundo conectado no site

@app.route("/") # cria a página do site
def home():
    return render_template("index.html") # essa página vai carregar esse arquivo html que está aqui

if __name__ == "__main__":
    # render (e outros serviços) passam a porta pela variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    # 0.0.0.0 permite conexões externas
    socketio.run(app, host="0.0.0.0", port=port)

