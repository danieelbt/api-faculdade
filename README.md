# 🏥 API de Profissionais de Saúde

Uma API desenvolvida com **Python 3.11** e **FastAPI**, que permite consultar um arquivo JSON com dados de profissionais da saúde. A aplicação fornece endpoints para:

- Pesquisar todos os profissionais
- Buscar por nome
- Filtrar por especialidade

---

## 🚀 Tecnologias Utilizadas

- [Python]
- [FastAPI]
- [Pydantic]
- [Uvicorn] (Opcional)

---

# ⚙️ Como Instalar e Executar o Projeto

# 1. Instação do Python

Acesse o site oficial do Python: https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe

Dê dois cliques no arquivo baixado para abrir o instalador.
MUITO IMPORTANTE: marque a opção: ✅ “Add Python 3.11 to PATH”
Clique em “Install Now”.
Aguarde a instalação ser concluída.

Abra o Prompt de Comando (CMD) ou PowerShell.
Digite o seguinte comando para verificar se o Python foi instalado corretamente: *'python --version'*
O resultado deve ser algo como: *'Python 3.11.7'*


# 1.1 Instalação das dependências
Uma vez que o projeto está baixado/clonado e o Python 3.11 (versão descrita no arquivo .python-version), você precisará instalar as dependências necessárias para execução do projeto.
Vamos começar com o FastAPI. Para instalá-lo, abra o terminal e execute o seguinte comando 'pip install "fastapi[standard]"'. Com o FastAPI instalado, nosso projeto já deve funcionar corretamente. Caso necessário, instale o Pydantic a parte com o comando 'pip install pydantic'.


# 2. Execução
Para executar o projeto, o seguinte comando deve ser executado no terminal ('fastapi dev .\projeto\endpoints\app.py' ou 'uvicorn projeto.endpoints.app:app --reload'). Esse comando aponta para o arquivo 'app.py' que está na pasta 'endpoints'. Uma vez executado, acesse o seguinte endereço para ser direcionado para a documentação interativa do Swagger UI *(http://127.0.0.1:8000/docs)*.


# Navegando pela Documentação Interativa

1. **Visualizar os Endpoints:**
   - Todos os endpoints estarão listados na interface.
   - Cada endpoint tem uma descrição, parâmetros de entrada e saída, e um botão **"Try it out"** para testar a API.

2. **Testar a API com o Swagger UI:**
   - Clique em **"Try it out"** em qualquer endpoint para ativar a funcionalidade de teste.
   - Preencha os campos necessários (como parâmetros, se houverem) e clique em **"Execute"**.
   - O Swagger irá realizar a requisição e você verá a resposta retornada pela API logo abaixo do botão **"Execute"**.

# Exemplo de Uso de Endpoints:

**Consultar todos os profissionais**:
  1. No Swagger UI, clique na opção **GET /todos-profissionais**.
  2. Clique em **"Try it out"** e depois em **"Execute"**.
  3. A resposta será uma lista de todos os profissionais cadastrados na API.
  4. Você também pode acessar o seguinte endereço: *(http://127.0.0.1:8000/todos-profissionais)*

**Buscar profissional por nome**:
  1. Clique na opção **GET /profissionais/{nome}**.
  2. Clique em **"Try it out"** e forneça o nome do profissional (Ex: 'Dra. Ana Cardio').
  3. Clique em **"Execute"** para obter os dados do profissional específico.
  4. Você também pode acessar o seguinte endereço: *(http://127.0.0.1:8000/profissionais/Dra.%20Ana%20Cardio)*
  5. Para pesquisar outro profissional pelo endereço, apenas digite o nome do mesmo após */profissionais/*

**Filtrar profissionais por especialidade**:
  1. Clique na opção **GET /profissionais**.
  2. Clique em **"Try it out"**, escolha uma especialidade e clique em **"Execute"**.
  3. A resposta mostrará os profissionais que possuem a especialidade selecionada.
  4. Você também pode acessar o seguinte endereço: *(http://127.0.0.1:8000/profissionais?especialidade=Cardiologia)*
  5. Para pesquisar outra especialidade pelo endereço, apenas digite o nome da mesma após */especialidade=/*
