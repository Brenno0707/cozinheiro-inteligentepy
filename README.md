# 🍳 Cozinheiro Inteligente

> Um assistente de receitas em Python que usa a API Gemini para sugerir pratos criativos com base nos ingredientes que você tem em casa.

Este projeto demonstra a integração do modelo **`gemini-2.5-flash`** da Google para tarefas de raciocínio criativo e geração de texto em Python.

## ✨ Funcionalidades

* Recebe uma lista de ingredientes fornecida pelo usuário.
* Chama a API Gemini para gerar sugestões de 3 receitas criativas.
* Limita o tamanho da resposta da IA para garantir a velocidade (otimização por `max_output_tokens`).

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.9+
* **API:** Google Gemini API
* **Biblioteca:** `google-genai` (SDK Oficial do Gemini)

## 🚀 Como Configurar e Executar

Siga estes passos para preparar seu ambiente e rodar o `main.py`.

### 1. Obtenha a Chave de API

Você precisa de uma chave de API válida para autenticar no serviço Gemini.

1.  Acesse o [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key).
2.  Crie uma nova chave e **copie-a**.

### 2. Instalação e Ambiente Virtual

1.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv venv
    # No Windows (CMD/PowerShell):
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

2.  **Instale as Dependências:**
    Use o arquivo `requirements.txt` que você baixou/criou:
    ```bash
    pip install -r requirements.txt
    ```

### 3. Configuração da Variável de Ambiente (Autenticação)

O projeto lê sua chave de API da variável de ambiente `GEMINI_API_KEY`.

#### Opção Recomendada: Configurar na IDE (IntelliJ/PyCharm)

1.  Vá em **Run** > **Edit Configurations...**.
2.  Selecione a configuração de execução do seu `main.py`.
3.  No campo **Environment variables** (Variáveis de Ambiente), clique no ícone de edição ($\fbox{\quad}$).
4.  Adicione a variável com sua chave:

| Nome | Valor |
| :--- | :--- |
| `GEMINI_API_KEY` | **COLE\_SUA\_CHAVE\_AQUI** |

### 4. Execução

Execute o arquivo principal:

```bash
python main.py
