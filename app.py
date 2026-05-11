from flask import Flask
import os

app = Flask(__name__)

contador = 0

@app.route('/')
def home():
    global contador
    contador += 1

    return f'''
    <h1>Projeto Containers 🚀</h1>
    <h2>Total de visitas: {contador}</h2>
    <p>Aplicação rodando em container com deploy na nuvem ☁️</p>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))