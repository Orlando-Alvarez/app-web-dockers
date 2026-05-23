from flask import Flask
import redis
import os

app = Flask(__name__)

r = redis.from_url(os.getenv('REDIS_URL'))

@app.route('/')
def inicio():
    visits = r.incr('visits')
    return f'''
    <html>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>🐳 My First Web App with Dockers!!</h1>
            <h2>This Website has been visited <span style="color: blue;">{visits}</span> times</h2>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
