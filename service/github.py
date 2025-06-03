import requests


def obter_dados_github(username):
    url = f"https://api.github.com/users/{username}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    return {"login": username, "name": "Desconhecido", "bio": "Não encontrado", "avatar_url": "#", "blog": ""}
