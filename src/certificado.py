from trilhas import carregar_trilhas

def gerar_certificado(tecnologia, nivel, aluno):
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

    # Criar certificado
    certificado = f"""
===========================================
        CERTIFICADO DE CONCLUSÃO
===========================================

Aluno: {aluno}
Trilha: {tecnologia} - {nivel}

Módulos concluídos:
"""

    for modulo in trilha_encontrada["modulos"]:
        certificado += f"- {modulo}\n"

    certificado += """
-------------------------------------------
Parabéns pela sua conquista!
Digital Innovation One - Geo Explorer
===========================================
"""

    print(certificado)
