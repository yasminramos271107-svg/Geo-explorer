import random
from trilhas import carregar_trilhas

def gerar_desafio(tecnologia, nivel):
    trilhas = carregar_trilhas()

    # Encontrar a trilha certa
    trilha_encontrada = None
    for trilha in trilhas:
        if trilha["tecnologia"].lower() == tecnologia.lower() and trilha["nivel"].lower() == nivel.lower():
            trilha_encontrada = trilha
            break

    if not trilha_encontrada:
        print("Trilha não encontrada.")
        return

    # Escolher um módulo aleatório
    modulo = random.choice(trilha_encontrada["modulos"])

    # Criar um desafio baseado no módulo
    desafio = f"Desafio para {tecnologia} ({nivel}):\n" \
              f"→ Crie um mini projeto usando o módulo **{modulo}**.\n" \
              f"Explique como ele funciona e mostre um exemplo prático."

    print(desafio)
