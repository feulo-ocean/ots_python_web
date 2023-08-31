from flask import Flask

app = Flask("meu app")
# Comentario
@app.route('/')
def hello():
    return "Hello World"

@app.route('/novo')
def novo():
    return "<h1> NOva pagina</h1>"