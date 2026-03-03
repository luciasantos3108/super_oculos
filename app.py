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
    return f"""
    <html>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>Obrigado, {nome}!</h1>
            <p>Recebemos o seu pedido para o modelo: <strong>{modelo}</strong>.</p>
            <p>Entraremos em contacto através de: {contacto}.</p>
            <br>
            <a href="/" style="color: #6e3cbc; text-decoration: none; font-weight: bold;">Voltar ao Início</a>
        </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    