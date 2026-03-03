from flask import Flask, render_template # Importa a ferramenta para ler HTML
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Esta linha diz ao Flask para mostrar o ficheiro index.html
    return render_template("index.html") 
@app.route("/produtos")
def produtos():
    return render_template("produtos.html")
from flask import request # Adiciona 'request' no topo onde tens o Flask

@app.route("/encomenda")
def encomenda():
    return render_template("encomenda.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    # Aqui o Python recebe o que o cliente escreveu
    nome = request.form.get("nome")
    modelo = request.form.get("modelo")
    contacto = request.form.get("contacto")
    
    # Por agora, vamos apenas mostrar uma mensagem de sucesso
    return f"<h1>Obrigado, {nome}!</h1><p>Recebemos o seu pedido para o modelo {modelo}. Entraremos em contacto para {contacto}.</p><a href='/'>Voltar ao Início</a>"
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
@app.route("/encomenda")
def encomenda():
    return render_template("encomenda.html")
