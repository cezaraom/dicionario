notas_estudantes = {
    "Harry": 81,
    "Ronny": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}

pontuacao_estudantes = {}

for estudante in notas_estudantes:
    notas = notas_estudantes[estudante]

    if notas > 90:
        pontuacao_estudantes[estudante] = "Excelente!"

    elif notas > 80:
        pontuacao_estudantes[estudante] = "Bom."

    elif notas > 70:
        pontuacao_estudantes[estudante] = "Razoável."
    
    else:
        pontuacao_estudantes[estudante] = "Ruim."

print(pontuacao_estudantes)