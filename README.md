📌 Projeto 1 — CLI “Pergunte à IA”

Uma ferramenta simples de linha de comando que envia uma pergunta para um modelo de linguagem e salva a resposta em um arquivo .md, além de registrar logs de uso.

🧠 Objetivo

Praticar Python moderno

Integrar API de LLM

Trabalhar com arquivos, logs e estrutura de projetos

Criar a primeira aplicação real do plano de 6 meses

🚀 Como executar
1. Criar ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

2. Instalar dependências
pip install -r requirements.txt

3. Criar arquivo .env

Crie o arquivo .env na raiz contendo:

API_KEY="sua_chave_aqui"


⚠️ Nunca coloque sua API Key no código ou no GitHub.

4. Rodar o programa
python app.py

📁 Saídas geradas

/respostas/ → Respostas em .md com timestamp

/logs/log.txt → Histórico de perguntas feitas

📝 Exemplo de uso
Qual sua pergunta para a IA?
> Explique o que são embeddings.


Gera:

respostas/2024-05-10_14-30-22.md

🔒 Segurança

Chave usada via .env

Logs não armazenam respostas (boa prática inicial)