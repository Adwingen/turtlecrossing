import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from game_settings import GameSettings
import pygame
import ranking  # Importa o módulo ranking

# Iniciar o mixer do Pygame para tocar os sons
pygame.mixer.init()

# Carregar os arquivos de som
collision_sound = pygame.mixer.Sound(
    r"C:\Users\carlo\PycharmProjects\pythonProjectTurtleCrossing\.sounds\415079__harrietniamh__video-game-death-sound-effect.wav")
goal_sound = pygame.mixer.Sound(
    r"C:\Users\carlo\PycharmProjects\pythonProjectTurtleCrossing\.sounds\438993__javapimp__lexie-good-job.ogg")
game_sound = pygame.mixer.music.load(
    r"C:\Users\carlo\PycharmProjects\pythonProjectTurtleCrossing\.sounds\647908__sonically_sound__short-loop-made-in-a-few-minutes-with-qws-and-goldwave.flac")  # Som de fundo

game_over = pygame.mixer.Sound(
    r"C:\Users\carlo\PycharmProjects\pythonProjectTurtleCrossing\.sounds\182286__qubodup__game-over.flac")

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Tocar música de fundo
def play_background_music(loop=True):
    pygame.mixer.music.play(-1 if loop else 0)

def adjust_background_music_speed(level):
    if level == 1:
        pygame.mixer.music.set_volume(0.5)
    elif level > 1:
        new_volume = min(1.0, 0.5 + (level * 0.1))
        pygame.mixer.music.set_volume(new_volume)

def clear_screen():
    screen.clearscreen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

def start_new_game(game_settings):
    player = Player()
    car = CarManager(game_settings.get_car_speed(), game_settings.get_car_creation_rate())
    scoreboard = Scoreboard()
    scoreboard.start_timer()
    screen.onkeypress(player.go_up, "Up")
    screen.onkeypress(player.go_down, "Down")
    screen.listen()

    play_background_music()

    return player, car, scoreboard


def play_game(player, car, scoreboard):
    game_is_on = True
    invincible = False
    invincibility_duration = 1.0
    last_collision_time = 0
    total_time = 0
    laps = 0  # Número de voltas

    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car.game_loop()

        scoreboard.update_time()

        if invincible and time.time() - last_collision_time > invincibility_duration:
            invincible = False

        for car_move in car.cars:
            if car_move.distance(player) < 20 and not invincible:
                collision_sound.play()
                scoreboard.decrement_life()
                if scoreboard.lives > 0:
                    player.go_to_start()
                    invincible = True
                    last_collision_time = time.time()
                else:
                    scoreboard.game_over()
                    game_is_on = False

        if player.is_at_finnish_line():
            goal_sound.play()
            player.go_to_start()
            car.level_up()
            scoreboard.increment_score()
            laps += 1
            total_time += scoreboard.elapsed_time  # Acumula o tempo total
            adjust_background_music_speed(scoreboard.score)

            # Alterar o tema do jogo se o nível for ímpar
            if scoreboard.score % 2 == 1:
                # Nível ímpar: fundo preto, tartaruga branca
                screen.bgcolor("black")
                player.color("white")
                scoreboard.color("white")
            else:
                # Nível par: fundo branco, tartaruga preta
                screen.bgcolor("white")
                player.color("black")
                scoreboard.color("black")

    pygame.mixer.music.stop()
    game_over.play()

    if laps > 0:
        avg_time = total_time / laps  # Calcula a média de tempo por volta
    else:
        avg_time = 0

    name = screen.textinput("Game Over", "Digite seu nome:").strip()

    # Salva a pontuação com nome, nível, voltas e tempo médio
    ranking.save_new_score(name, scoreboard.score, laps, avg_time)

    response = screen.textinput("Game Over", "Quer jogar novamente? (sim/não)").strip().lower()
    return response in ("sim", "s", "yes", "y", "1")


# Main game loop
while True:
    clear_screen()

    # Exibe o ranking no início do jogo e mantém o objeto Turtle para limpar o ranking depois
    turtle_writer = ranking.display_ranking(screen)

    # Aguarda um tempo para exibir o ranking, mas sem travar o jogo
    screen.update()
    time.sleep(5)  # Exibir o ranking por 3 segundos

    # Limpa o ranking da tela
    turtle_writer.clear()

    game_settings = GameSettings()
    game_settings.select_difficulty(screen)
    player, car, scoreboard = start_new_game(game_settings)
    if not play_game(player, car, scoreboard):
        screen.bye()
        break















