import sys

# Calcula o nº de combinações possíveis
def combinations_calculator(points):
    combinations = [0] * (points + 1) # lista de maneiras para obter cada pontuação até o nº do placar
    combinations[0] = 1 # caso base, só há uma maneira de se obter a pontuação 0
    for i in range(3, points + 1):
        combinations[i] += combinations[i - 3]

    for i in range(6, points + 1):
        combinations[i] += combinations[i - 6]

    for i in range(7, points + 1):
        combinations[i] += combinations[i - 7]

    for i in range(8, points + 1):
        combinations[i] += combinations[i - 8]

    return combinations[points]

# Retorna o nº de combinações possíveis
def get_combinations_for_score(score: str) -> int:
    points1, points2 = map(int, score.split('x'))
    return combinations_calculator(points1) * combinations_calculator(points2)