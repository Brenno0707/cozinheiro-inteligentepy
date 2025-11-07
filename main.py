# app.py
import os
from google import genai
from google.genai.errors import APIError
from google.genai import types


# Coloque sua chave de API aqui. É crucial que você NÃO envie essa chave para o GitHub!
# É melhor carregar a chave de uma variável de ambiente (como 'GEMINI_API_KEY')
# Para começar, você pode colocar a chave diretamente, mas remova antes do commit!
# Chave_de_API = "SUA_CHAVE_AQUI"

def gerar_receita(ingredientes_lista):
    # 1. Monta o prompt com os ingredientes
    prompt_usuario = (
            "Com base nos seguintes ingredientes, sugira 3 receitas criativas e detalhadas (com nome, tempo de preparo e passos): "
            + ", ".join(ingredientes_lista)
    )

    try:
        # Inicializa o cliente da API
        client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

        # 2. Chama o modelo de IA
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_usuario,
        )
        return response.text

    except APIError as e:
        return f"Erro na API: {e}. Verifique sua chave e permissões."
    except Exception as e:
        return f"Ocorreu um erro: {e}"


if __name__ == "__main__":
    print("--- Cozinheiro Inteligente ---")

    # Pede os ingredientes ao usuário
    ingredientes_raw = input("Liste 3 a 5 ingredientes que você tem (separados por vírgula): ")

    # Processa a entrada
    ingredientes_lista = [i.strip() for i in ingredientes_raw.split(',') if i.strip()]

    if ingredientes_lista:
        print("\nProcessando inteligência...")
        receitas = gerar_receita(ingredientes_lista)

        print("\n--- Receitas Sugeridas ---")
        print(receitas)
        print("--------------------------")
    else:
        print("Nenhum ingrediente fornecido. Encerrando.")