import pandas as pd

def analisar_logs():
    nome_arquivo = input("Digite o nome do arquivo CSV (ex: logs_treinamento.csv): ").strip()

    try:
        df = pd.read_csv(nome_arquivo)

        if 'tempo_execucao' not in df.columns:
            print("Erro: A coluna 'tempo_execucao' não foi encontrada no arquivo.")
            return

        media = df['tempo_execucao'].mean()
        desvio = df['tempo_execucao'].std()

        print(f"Média do tempo de execução: {media:.2f}")
        print(f"Desvio padrão do tempo de execução: {desvio:.2f}")

    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Verifique o nome e tente novamente.")
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo está vazio.")
    except pd.errors.ParserError:
        print("Erro: Formatação incorreta no arquivo CSV.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    analisar_logs()
