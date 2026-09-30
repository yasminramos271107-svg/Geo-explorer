import json

def carregar_trilhas():
    with open("data/trilhas.json", "r", encoding="utf-8") as arquivo:
        trilhas = json.load(arquivo)
    return trilhas
