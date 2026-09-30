import json

def carregar_trilhas():
    with open("data/trilhas.json", "r", encoding="utf-8") as arquivo:
        trilhas = json.load(arquivo)
    return trilhas


def buscar_trilha(tecnologia, nivel):
    trilhas = carregar_trilhas()
    for trilha in trilhas:
        if trilha["tecnologia"].lower() == tecnologia.lower() and trilha["nivel"].lower() == nivel.lower():
            return trilha
    return None


def mostrar_trilha(tecnologia, nivel):
    trilha = buscar_trilha(tecnologia, nivel)
    if trilha:
        print(f"Trilha encontrada: {tecnologia} - {nivel}")
        print("Módulos:")
        for modulo in trilha["modulos"]:
            print(f"- {modulo}")
    else:
        print("Trilha não encontrada.")
