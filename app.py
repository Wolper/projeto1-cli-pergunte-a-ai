import os
import requests
import argparse
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def perguntar_ia(prompt: str, modelo: str = "gpt-4o-mini") -> str:
    """
    Envia uma pergunta ao modelo de IA usando a OpenAI API.
    Sempre força a resposta em português do Brasil.
    """
    
    url = "https://api.openai.com/v1/chat/completions"

    payload = {
        "model": modelo,
        "messages": [
            {
                "role": "system",
                "content": "Você é um assistente que responde sempre em português do Brasil, "
                           "de forma clara, objetiva e educada. Nunca responda em outro idioma."
            },
            {"role": "user", "content": prompt}
        ]
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    try:
        response.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Erro ao chamar a API: {e}")

    return response.json()["choices"][0]["message"]["content"]


def salvar_resposta(prompt: str, resposta: str):
    """
    Salva a pergunta e a resposta em um arquivo Markdown;
    e registra a pergunta no log.txt.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"respostas/{timestamp}.md"

    # Salvar resposta
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Pergunta\n{prompt}\n\n# Resposta\n{resposta}")

    # Registrar log
    with open("logs/log.txt", "a", encoding="utf-8") as log:
        log.write(f"{timestamp} | {prompt}\n")


def main():
    parser = argparse.ArgumentParser(description="CLI - Pergunte à IA (PT-BR)")

    parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="Texto da pergunta para enviar à IA"
    )

    parser.add_argument(
        "--modelo",
        type=str,
        default="gpt-4o-mini",
        help="Modelo a ser utilizado (padrão: gpt-4o-mini)"
    )

    args = parser.parse_args()

    resposta = perguntar_ia(args.prompt, modelo=args.modelo)
    salvar_resposta(args.prompt, resposta)

    print("\n📁 Resposta salva com sucesso em /respostas\n")


if __name__ == "__main__":
    main()
