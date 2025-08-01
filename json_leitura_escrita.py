import json

def ler_escrever_json():
    dados_pessoa = {
        "nome": "João Silva",
        "idade": 30,
        "cidade": "Curitiba"
    }

    nome_arquivo = input("Digite o nome do arquivo JSON (ex: pessoa.json): ").strip()

    try:
        # Escrever dados no arquivo JSON
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_pessoa, arquivo, ensure_ascii=False, indent=4)
        print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'.")

        # Ler dados do arquivo JSON
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados_carregados = json.load(arquivo)
        print("Dados carregados do arquivo:")
        print(dados_carregados)

    except IOError as e:
        print(f"Erro ao acessar o arquivo: {e}")
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    ler_escrever_json()
