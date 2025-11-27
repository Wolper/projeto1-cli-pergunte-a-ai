import os
import glob
import requests
import argparse
from datetime import datetime
from dotenv import load_dotenv
from commands import listar_modelos, mostrar_ultima_resposta
from core import perguntar_ia, salvar_resposta

load_dotenv()

modelos = ["gpt-4o", "gpt-4o-mini", "gpt-4o-reasoning", "gpt-4o-mini-tts"]

API_KEY = os.getenv("API_KEY")


def create_parser():
    parser = argparse.ArgumentParser(
        description="CLI - Pergunte à IA com Subcomandos (PT-BR)"
    )

    subparsers = parser.add_subparsers(dest="comando")

    # -----------------------------
    # Subcomando: perguntar
    # -----------------------------
    perguntar_parser = subparsers.add_parser(
        "perguntar", help="Enviar uma pergunta à IA"
    )
    perguntar_parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="Texto da pergunta",
    )
    perguntar_parser.add_argument(
        "--modelo", type=str, default="gpt-4o-mini", help="Modelo a ser usado"
    )

    # -----------------------------
    # Subcomando: historico
    # -----------------------------
    subparsers.add_parser("historico", help="Exibir o histórico de perguntas (log)")

    # -----------------------------
    # Subcomando: limpar-log
    # -----------------------------
    subparsers.add_parser("limpar-log", help="Limpar o arquivo de log")

    # -----------------------------
    # Subcomando: listar modelos
    # -----------------------------
    subparsers.add_parser("modelos", help="lista os modelos suportados")

    # -----------------------------
    # Subcomando: última-resposta
    # -----------------------------
    subparsers.add_parser(
        "ultima-resposta", help="Mostra o último arquivo de resposta gerado"
    )
    return parser


def main():
    os.system("cls" if os.name == "nt" else "clear")

    parser = create_parser()
    args = parser.parse_args()

    if args.comando == "modelos":
        listar_modelos()
    elif args.comando == "ultima-resposta":
        mostrar_ultima_resposta()
    elif args.comando == "perguntar":
        resposta = perguntar_ia(args.prompt, modelo=args.modelo)
        salvar_resposta(args.prompt, resposta)
    elif args.comando == "historico":
        try:
            with open("logs/log.txt", "r", encoding="utf-8") as f:
                conteudo = f.read()
                print("\n📜 Histórico de perguntas:\n")
                print(conteudo if conteudo else "(vazio)")
        except FileNotFoundError:
            print("\n⚠️ Nenhum histórico encontrado.\n")
    elif args.comando == "limpar-log":
        open("logs/log.txt", "w").close()
        print("\n🧹 Log limpo com sucesso!\n")


if __name__ == "__main__":
    main()
