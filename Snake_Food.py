import random
GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 1
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for _ in range(0, BODY_PARTS):
            self.coordinates.append([0,0])


    def draw(self, canvas):
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self):
        self.x = random.randint(0, (GAME_WIDTH / SPACE_SIZE - 1)) * SPACE_SIZE
        self.y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE - 1)) * SPACE_SIZE
        self.coordinates = [self.x, self.y]

    def draw_food(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + SPACE_SIZE, self.y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")