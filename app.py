from flask import Flask
import redis
import os

app = Flask(__name__)

r = redis.from_url(os.getenv('REDIS_URL'))

@app.route('/')
def inicio():
    visitas = r.incr('visitas')
    return f'''
    <html>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>🐳 Mi primera app web con Docker</h1>
            <h2>Esta página ha sido visitada <span style="color: blue;">{visitas}</span> veces</h2>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)