from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    r.incr('visitas')
    visitas = r.get('visitas').decode('utf-8')

    return f'''
    <h1>Projeto Containers 🚀</h1>
    <h2>Total de visitas: {visitas}</h2>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)