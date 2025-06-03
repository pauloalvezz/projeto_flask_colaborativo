from flask import Flask, render_template, render_template_string
from jinja2 import TemplateNotFound
from service.github import obter_dados_github 

app = Flask(__name__)

usuarios = ["lucianolpsf", "fernandallobao", "jesieldossantos", "Victorrezende19", "calebegomes740", "CaioHarrys", "aucelio0", "brunofluna", "Rafael-ai13", "Xandy77", "pauloalvezz" ] 

usuarios = ["lucianolpsf", "fernandallobao", "jesieldossantos", "Victorrezende19", "calebegomes740", "CaioHarrys", "aucelio0", "brunofluna", "Rafael-ai13", "Xandy77", "pauloalvezz"] 

@app.route("/")
def home():
    membros = [obter_dados_github(usuario) for usuario in usuarios]
    return render_template("home.html", membros=membros)


@app.route("/<usuario>")
def rota_usuario(usuario):
    try:
        return render_template(f"{usuario}.html")
    except TemplateNotFound:
        return render_template_string(f"<h1>Rota personalizada de {usuario}</h1>") 



if __name__ == '__main__':
    app.run(debug=True)