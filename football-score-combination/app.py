from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from combinations import get_combinations_for_score

app = FastAPI()

# Decorador
@strawberry.type
class Query:
    @strawberry.field
    def name(self) -> str:
        return "Strawberry"
    
# Definindo o tipo de resposta 
@strawberry.type
class Result:
    combinations: int

# Definindo o tipo de mutation
@strawberry.type
class Verify:

    @strawberry.field
    def verify(self, score: str) -> Result:
        return Result(combinations = get_combinations_for_score(score))

# Criando o schema com a mutation
schema = strawberry.Schema(query=Query, mutation=Verify)

# Configurando a aplicação FastAPI e a rota GraphQL
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)