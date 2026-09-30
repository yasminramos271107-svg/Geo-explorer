from trilhas import carregar_trilhas

trilhas = carregar_trilhas()

print("Trilhas carregadas:")
for trilha in trilhas:
    print(trilha["tecnologia"], "-", trilha["nivel"])
