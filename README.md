# football-score-combination
Esta API calcula o número de combinações possíveis para um placar de jogo de futebol americano usando pontuações válidas.

## Requisitos

- Python 3.9
- Docker (opcional)

## Instalação

    1. Clone este repositório:
        ```sh
        git clone https://github.com/004-4/football-score-combination.git
        cd football-score-combination

    2. Para executar localmente:
        2.1 crie um ambiente virtual 
            python -m venv venv
            source venv/bin/activate  # Linux/Mac
            venv\Scripts\activate  # Windows
        2.2 instale as dependências
            pip install -r requirements.txt
        2.3 execute a aplicação
            uvicorn app:app --host 0.0.0.0 --port 8080

    3. Para executar usando o Docker:
        3.1 construa a imagem Docker:
            docker build -t football-api .
        3.2 execute o contêiner:
            docker run -p 8080:8080 football-api

    observação: foi escolhido a api FastAPI de padrão GraphQL
