import pandas as pd

def excel_to_csv(excel_file_path, csv_file_path):
    """
    Converte um arquivo Excel (.xlsx ou .xls) em CSV.

    Args:
        excel_file_path (str): Caminho do arquivo Excel de entrada.
        csv_file_path (str): Caminho onde o arquivo CSV será salvo.
    """
    try:
        df = pd.read_excel(excel_file_path)

        df.to_csv(csv_file_path, index=False)
        print(f"Arquivo convertido com sucesso! CSV salvo em: {csv_file_path}")

    except Exception as e:
        print(f"Erro durante a conversão: {e}")

if __name__ == "__main__":
    input_excel = "/home/deborah/campi_inteligente/dados/date_solo.xlsx"  
    output_csv = "/home/deborah/campi_inteligente/data_solo.csv"     

    excel_to_csv(input_excel, output_csv)
