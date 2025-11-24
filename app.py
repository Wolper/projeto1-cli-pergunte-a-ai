import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")  # Não colocar no código. Usar .env.

def perguntar_ia(prompt: str) -> str:
    url = "https://api.openai.com/v1/chat/completions"
    
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]


def salvar_resposta(prompt: str, resposta: str):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"respostas/{timestamp}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Pergunta\n{prompt}\n\n# Resposta\n{resposta}")

    # Registrar pergunta no log
    with open(f"logs/log.txt", "a", encoding="utf-8") as log:
        log.write(f"{timestamp} | {prompt}\n")


def main():
    prompt = input("Qual sua pergunta para a IA?\n> ")
    resposta = perguntar_ia(prompt)
    salvar_resposta(prompt, resposta)
    print("\nResposta salva com sucesso em /respostas")


if __name__ == "__main__":
    main()
