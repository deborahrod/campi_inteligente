# Projeto: Middleware para Integração IoT e Processamento de Dados de Consumo de Água
Este projeto visa o desenvolvimento de um middleware para facilitar a integração de sensores e dispositivos IoT e implementar funcionalidades de processamento de dados para fornecer informações detalhadas e acionáveis sobre o consumo de água.

## Objetivos Principais
Criar um middleware que facilite a integração de diversos sensores e dispositivos IoT.

Entregáveis:
Código-fonte do middleware, validado e testado.
Repositório GitHub contendo o código.
Procedimentos de instalação do software e de dependências.
Implementar funcionalidades de processamento de dados para fornecer informações detalhadas e acionáveis sobre o consumo de água.

Entregáveis:
Módulos de código para processamento de dados integrados ao middleware.
Repositório GitHub contendo o código.
Procedimentos de instalação do software e de dependências.

## Dados dos Sensores
Os dados são coletados por 4 sensores no período de 1º de dezembro de 2024 até 12 de dezembro de 2024. As informações incluem:

- Data e Hora
- Tipo de Planta
- Número do Sensor
- Temperatura do Ar (°C)
- Umidade do Ar (%)
- Umidade do Solo (%)

### Exemplo de Dados:

```bash
{
  "data": [
    {
      "Data": "2024-12-01",
      "Hora": "00:00:00",
      "Planta": "Alface Roxa",
      "Sensor": 1,
      "Temperatura_Ar (°C)": 21.12,
      "Umidade_Ar (%)": 74.97,
      "Umidade_Solo (%)": 50.32
    },
    {
      "Data": "2024-12-02",
      "Hora": "00:00:00",
      "Planta": "Alface Roxa",
      "Sensor": 2,
      "Temperatura_Ar (°C)": 22.50,
      "Umidade_Ar (%)": 72.30,
      "Umidade_Solo (%)": 48.10
    }
  ]
}
```

### Implementação e Subida dos Dados

Os dados coletados pelos sensores serão enviados para uma rota pública.
Será iniciada a análise preliminar dos dados no período especificado (1 a 12 de dezembro de 2024).


## Procedimentos de Instalação
Clonar o Repositório:

```bash
git clone https://github.com/deborahrod/campi_inteligente.git
cd campi_inteligente
```

Instalar Dependências:

```bash
pip install -r requirements.txt
```

Executar o Middleware:

```bash
python app.py
```

### Tecnologias Utilizadas

- Linguagem de Programação: Python
- Framework: Flask
- Armazenamento de Dados: JSON/CSV
- Ferramentas de Processamento: Pandas


### Estrutura do Projeto
```plaintext
campi_inteligente/
│
├── app.py                # Código principal do middleware
├── modules/              # Módulos de processamento de dados
│   ├── data_processor.py # Lógica de processamento de dados
│
├── data/                 # Dados dos sensores (JSON ou CSV)
│   ├── sensores.json
│   ├── sensores.csv
│
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
```
