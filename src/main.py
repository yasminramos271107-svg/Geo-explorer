from trilhas import mostrar_trilha
from desafio import gerar_desafio
from certificado import gerar_certificado

def main():
    print("=== Geo Explorer ===")
    print("1 - Ver trilha")
    print("2 - Gerar desafio")
    print("3 - Gerar certificado")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tecnologia = input("Tecnologia: ")
        nivel = input("Nível: ")
        mostrar_trilha(tecnologia, nivel)

    elif opcao == "2":
        tecnologia = input("Tecnologia: ")
        nivel = input("Nível: ")
        gerar_desafio(tecnologia, nivel)

    elif opcao == "3":
        tecnologia = input("Tecnologia: ")
        nivel = input("Nível: ")
        aluno = input("Nome do aluno: ")
        gerar_certificado(tecnologia, nivel, aluno)

    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()

