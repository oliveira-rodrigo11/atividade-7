import csv

def escrever_csv():
    # Dados fictícios de pessoas
    pessoas = [
        ["Ana Silva", 28, "São Paulo"],
        ["Carlos Pereira", 35, "Rio de Janeiro"],
        ["Mariana Costa", 22, "Belo Horizonte"]
    ]

    nome_arquivo = input("Digite o nome do arquivo CSV para salvar os dados (ex: pessoas.csv): ").strip()

    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            # Escreve o cabeçalho
            escritor.writerow(["Nome", "Idade", "Cidade"])
            # Escreve as linhas com dados
            escritor.writerows(pessoas)

        print(f"Dados gravados com sucesso no arquivo '{nome_arquivo}'.")

    except IOError as e:
        print(f"Erro ao escrever no arquivo: {e}")

if __name__ == "__main__":
    escrever_csv()
