# FastAPI Football Score Combinations
Esta API calcula o número de combinações possíveis para um placar de jogo de futebol americano usando pontuações válidas.

## Estrutura do Projeto
/ football-score-combination
├── app.py
├── combinations.py
├── Dockerfile
├── requirements.txt
├── test_app.py
└── docker-compose.yml

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
        3.1 construa e execute o contêiner:
            docker-compose up --build

## Testes

    1. Rodando os testes localmente:
        1.1 em seu terminal execute o comando 
            pytest

    2. Rodando os testes com o Docker:
        2.1 encontre o ID do container em um novo terminal
            docker ps
        2.2 execute os testes nesse container
            docker exec -it <container_id_or_name> pytest       
