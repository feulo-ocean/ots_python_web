from flask import Flask, render_template

app = Flask("Meu App")

posts = [
    {
        "titulo": "Minha primeira postagem",
        "texto": "teste"
    },
    {
        "titulo": "Segundo Post",
        'texto': "outro teste"
    }
]

@app.route('/')
def exibir_entradas():
    entradas = posts # Mock das postagens
    return render_template('exibir_entradas.html', entradas=entradas)
