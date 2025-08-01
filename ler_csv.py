import csv

def ler_csv():
    nome_arquivo = input("Digite o nome do arquivo CSV a ser lido: ").strip()

    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print(linha)

    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Verifique o nome e tente novamente.")
    except IOError as e:
        print(f"Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    ler_csv()
