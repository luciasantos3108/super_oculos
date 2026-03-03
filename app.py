from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

@app.route("/encomenda")
def encomenda():
    return render_template("encomenda.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form.get("nome")
    modelo = request.form.get("modelo")
    contacto = request.form.get("contacto")
    return f"<h1>Obrigado, {nome}!</h1><p>Pedido recebido para: {modelo}. Contactaremos para {contacto}.</p><a href='/'>Voltar</a>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)