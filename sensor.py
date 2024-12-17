from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_csv_data():
    """Rota pública que retorna o conteúdo do CSV como JSON."""
    try:
        # Caminho do arquivo CSV
        csv_path = '/home/deborah/campi_inteligente/dados/data_solo.csv'  # Substitua pelo nome do seu arquivo CSV

        # Lê o arquivo CSV usando pandas
        df = pd.read_csv(csv_path)

        # Converte o DataFrame para uma lista de dicionários
        data = df.to_dict(orient='records')

        return jsonify({'status': 'success', 'data': data}), 200

    except FileNotFoundError:
        return jsonify({'status': 'error', 'message': 'Arquivo CSV não encontrado!'}), 404

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "Bem-vindo à API! Acesse /data para obter os dados do CSV.", 200

if __name__ == '__main__':
    app.run(debug=True)
