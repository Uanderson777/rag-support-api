# 🚀 RAG Support API

**API de Base de Conhecimento para Suporte Técnico utilizando RAG (Retrieval-Augmented Generation), FastAPI e Inteligência Artificial.**

---

## 📌 Sobre o Projeto

A **RAG Support API** é uma solução backend desenvolvida em Python e FastAPI focada no atendimento de chamados e suporte técnico inteligente. A API utiliza a técnica de **RAG (Retrieval-Augmented Generation)** para consultar documentos internos de suporte (Manuais, FAQs, Procedimentos operacionais) armazenados em um Banco Vetorial e fornecer respostas precisas e contextualizadas através de um Modelo de Linguagem (LLM).

---

## ⚙️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Framework Web:** [FastAPI](https://fastapi.tiangolo.com/)
- **Servidor ASGI:** Uvicorn
- **Validação de Dados:** Pydantic
- **Gerenciamento de Variáveis:** `python-dotenv`
- **Técnica de IA:** RAG (Retrieval-Augmented Generation) com Embeddings e Vector Database (ChromaDB)

---

## 📁 Estrutura do Projeto

```text
rag-support-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # Ponto de entrada da aplicação FastAPI
│   ├── config.py            # Carregamento de configurações e variáveis de ambiente
│   ├── routers/             # Endpoints da API (Busca, Ingestão, Status)
│   ├── services/            # Serviços de RAG, Embeddings, Vector Store e LLM
│   └── models/              # Modelos e Schemas do Pydantic
├── data/                    # Documentos e arquivos de dados para ingestão
├── .env.example             # Template de variáveis de ambiente
├── .gitignore               # Arquivos e diretórios ignorados pelo Git
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação técnica do repositório
```

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/Uanderson777/rag-support-api.git
cd rag-support-api
```

### 2. Criar e ativar o ambiente virtual
- **Linux/macOS:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  \.venv\Scripts\Activate.ps1
  ```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente
Copie o arquivo `.env.example` para `.env` e preencha suas credenciais:
```bash
cp .env.example .env
```

### 5. Executar a aplicação
```bash
uvicorn app.main:app --reload
```
Acesse a documentação interativa da API em `http://127.0.0.1:8000/docs`.

---

## 👤 Autor

Desenvolvido por **Uanderson Martins** como projeto de portfólio prático em Inteligência Artificial, Engenharia de Dados e Backend Python na **DIO**.
