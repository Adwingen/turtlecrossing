import os
import json
from turtle import Turtle
import time

RANKING_FILE = r"C:\Users\carlo\PycharmProjects\pythonProjectTurtleCrossing\ranking.json"


# Função para ler as pontuações do arquivo
def load_ranking():
    print(f"Lendo ranking de {RANKING_FILE}...")
    if os.path.exists(RANKING_FILE):
        with open(RANKING_FILE, "r") as file:
            scores = json.load(file)  # Carregar as pontuações como JSON
            print(f"Pontuações lidas: {scores}")
            return scores
    print("Arquivo de ranking não encontrado.")
    return []


# Função para salvar uma nova pontuação no arquivo
def save_new_score(name, level, laps, avg_time):
    print(f"Salvando nova pontuação: Jogador={name}, Nível={level}, Voltas={laps}, Média de tempo={avg_time:.2f}")
    scores = load_ranking()

    # Adicionar a nova entrada de ranking
    new_entry = {"name": name, "level": level, "laps": laps, "avg_time": avg_time}
    scores.append(new_entry)

    # Ordenar primeiro pelo nível, depois pela média de tempo
    scores = sorted(scores, key=lambda x: (x["level"], -x["avg_time"]), reverse=True)[:5]  # Mantém os 5 melhores

    # Criar o arquivo se ele não existir e salvar as pontuações
    with open(RANKING_FILE, "w") as file:
        json.dump(scores, file, indent=4)
    print(f"Pontuações salvas em {RANKING_FILE}")


# Função para exibir o ranking
def display_ranking(screen):
    scores = load_ranking()

    # Limpa a tela para exibir o ranking
    screen.clear()

    # Desabilita a atualização automática da tela para evitar flicker
    screen.tracer(0)

    # Mostrar ranking no topo da tela
    if scores:
        ranking_message = "Ranking:\n" + "\n".join(
            [f"{idx + 1}. {entry['name']} - Nível: {entry['level']}, Voltas: {entry['laps']}, Média: {entry['avg_time']:.2f}s"
             for idx, entry in enumerate(scores)])
    else:
        ranking_message = "Nenhuma pontuação registrada ainda."

    # Exibir o ranking no centro da tela
    turtle_writer = Turtle()
    turtle_writer.hideturtle()
    turtle_writer.penup()
    turtle_writer.goto(0, 0)  # Posição no topo
    turtle_writer.write(ranking_message, align="center", font=("Courier", 12, "normal"))

    screen.update()  # Atualizar a tela com o ranking

    return turtle_writer  # Retorna o Turtle responsável pelo texto para que possamos apagá-lo depois





