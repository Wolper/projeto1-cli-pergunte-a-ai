import os
import glob

modelos = ["gpt-4o", "gpt-4o-mini", "gpt-4o-reasoning", "gpt-4o-mini-tts"]


def listar_modelos():
    print("\n📌 Modelos disponíveis:\n")
    for modelo in modelos:
        print(f" - {modelo}")
    print()


def mostrar_ultima_resposta():
    arquivos = glob.glob("respostas/*.md")

    if not arquivos:
        print("\n⚠️ Nenhuma resposta encontrada.\n")
        return

    arquivo_mais_recente = max(arquivos, key=os.path.getmtime)

    print(f"\n📄 Última resposta encontrada:")
    print(f"   Arquivo: {os.path.basename(arquivo_mais_recente)}\n")

    with open(arquivo_mais_recente, "r", encoding="utf-8") as f:
        print(f.read())
    print()
