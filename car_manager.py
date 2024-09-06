#car_manager.py

import time
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager:
    def __init__(self, speed, creation_rate):
        self.cars = []
        self.car_speed = speed
        self.car_creation_rate = 0.35  # Frequência de criação de carros em segundos
        self.last_creation_time = time.time()  # Registrar o tempo da última criação de carro

    def create_cars(self):
        """Cria um novo carro e o posiciona na tela."""
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()

        # Variar o tamanho dos carros
        car_length = random.randint(1, 3)  # Comprimento aleatório entre 1 e 3
        car_width = random.randint(1, 2)  # Largura aleatória entre 1 e 2
        new_car.shapesize(stretch_wid=car_width, stretch_len=car_length)

        new_car.color(random.choice(COLORS))

        # Escolher aleatoriamente a direção do carro
        if random.choice([True, False]):
            new_car.setheading(180)  # Da direita para a esquerda
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
        else:
            new_car.setheading(0)  # Da esquerda para a direita
            random_y = random.randint(-250, 250)
            new_car.goto(-300, random_y)

        # Definir o comportamento de movimento especial
        if random.choice([True, False]):
            new_car.move_type = "zigzag"  # Carro que faz zig-zag
        else:
            new_car.move_type = "variable_speed"  # Carro que acelera e desacelera

        self.cars.append(new_car)

    def move_car(self):
        """Move os carros na tela, aplicando movimentos especiais."""
        for car in self.cars:
            if car.move_type == "zigzag":
                # Zigzag: movimenta-se horizontalmente e levemente para cima ou para baixo
                car.forward(self.car_speed)
                car.sety(car.ycor() + random.choice([-5, 5]))  # Move um pouco em Y para zig-zag
            elif car.move_type == "variable_speed":
                # Velocidade variável: acelera ou desacelera
                speed_variation = random.uniform(-1, 1)  # Pequena variação de velocidade
                car.forward(self.car_speed + speed_variation)
            else:
                car.forward(self.car_speed)  # Movimento normal

        # Remover os carros que saíram da tela
        self.cars = [car for car in self.cars if -320 < car.xcor() < 320]

    def game_loop(self):
        """Loop principal do gerenciamento de carros."""
        current_time = time.time()
        # Criar um carro novo baseado no tempo decorrido desde a última criação
        if current_time - self.last_creation_time >= self.car_creation_rate:
            self.create_cars()
            self.last_creation_time = current_time  # Atualizar o tempo da última criação

        self.move_car()

    def level_up(self):
        """Aumentar a velocidade dos carros e reduzir o tempo entre a criação de novos carros a cada nível."""
        self.car_speed += 2  # Aumenta a velocidade dos carros
        self.car_creation_rate -= 0.1

        # Reduzir o tempo entre criações, mas limitar para evitar criação muito rápida
        if self.car_creation_rate > 0.35:
            self.car_creation_rate -= 0.05
        print(f"Velocidade do carro: {self.car_speed}, Taxa de criação: {self.car_creation_rate:.2f} segundos")

