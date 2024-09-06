# game_settings.py

class GameSettings:
    """Classe para gerenciar as configurações do jogo, incluindo dificuldade."""

    def __init__(self):
        self.difficulty = None
        self.car_speed = 5
        self.car_creation_rate = 6

    def select_difficulty(self, screen):
        """Exibe uma caixa de diálogo para o jogador selecionar a dificuldade."""
        valid_choices = ['1', '2', '3']
        while True:
            difficulty = screen.textinput("Escolher Dificuldade", "Digite 1 = fácil, 2 = médio ou 3 = difícil:").lower()
            if difficulty in valid_choices:
                self.difficulty = difficulty
                break
            else:
                screen.textinput("Entrada Inválida", "Por favor, digite '1', '2' ou '3'. Pressione Enter para tentar novamente.")

        self.set_difficulty_parameters()

    def set_difficulty_parameters(self):
        """Define os parâmetros do jogo com base na dificuldade selecionada."""
        if self.difficulty == '1':
            self.car_speed = 10
            self.car_creation_rate = 30  # Menos carros
        elif self.difficulty == '2':
            self.car_speed = 20
            self.car_creation_rate = 20  # Frequência média de carros
        elif self.difficulty == '3':
            self.car_speed = 35
            self.car_creation_rate = 10  # Mais carros

    def get_car_speed(self):
        return self.car_speed

    def get_car_creation_rate(self):
        return self.car_creation_rate

