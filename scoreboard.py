from turtle import Turtle
import time

FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.start_time = time.time()
        self.elapsed_time = 0
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.display_score()

    def increment_score(self):
        self.score += 1
        self.start_timer()  # Reinicia o temporizador ao avançar de nível
        self.display_score()

    def decrement_life(self):
        self.lives -= 1
        self.display_score()

    def start_timer(self):
        """Reinicia o temporizador no início de cada nível."""
        self.start_time = time.time()

    def update_time(self):
        """Atualiza o tempo decorrido constantemente."""
        self.elapsed_time = time.time() - self.start_time
        self.display_score()  # Atualiza o display para mostrar o tempo atual

    def display_score(self):
        """Exibe o nível, vidas e o tempo atual na tela."""
        self.clear()
        self.write(f"Level: {self.score} | Lives: {self.lives} | Time: {self.elapsed_time:.2f}s", False, "left", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)


