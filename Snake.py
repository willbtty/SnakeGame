from tkinter import *
import random
import math
from Snake_Food import Food, Snake

GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 1
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class SnakeGame:
    def __init__(self):
        self.score = 0
        self.direction = DOWN
        self.snake = None
        self.food = None
        self.window = Tk()
        self.window.title("Snake")
        self.window.resizable(False, False)
        self.snake = Snake()
        self.food = Food()
        self.is_game_over = False

    def get_direction(self):
        return self.direction

    def MainGame(self):
        self.score = 0
        self.direction = DOWN

        self.label = Label(self.window, text="Score:{}".format(self.score), font=('consolas', 40))
        self.label.pack()

        self.canvas = Canvas(self.window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
        self.canvas.pack()
        self.window.update()

        self.window.bind('<Left>', lambda event: self.change_direction(LEFT))
        self.window.bind('<Right>', lambda event: self.change_direction(RIGHT))
        self.window.bind('<Up>', lambda event: self.change_direction(UP))
        self.window.bind('<Down>', lambda event: self.change_direction(DOWN))

        self.snake = Snake()
        self.food = Food()
        self.snake.draw(self.canvas)
        self.food.draw_food(self.canvas)
        self.next_turn()

        self.window.mainloop()

    def next_turn(self):
        #TODO: check if it actually retruns anything
        x, y = self.snake.coordinates[0]
        
        #varaibales used to inform agent
        reward = 0
        self.is_game_over = False

        if self.direction == UP:
            y -= SPACE_SIZE
        elif self.direction == DOWN:
            y += SPACE_SIZE
        elif self.direction == LEFT:
            x -= SPACE_SIZE
        elif self.direction == RIGHT:
            x += SPACE_SIZE

        self.snake.coordinates.insert(0, (x, y))
        square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        self.snake.squares.insert(0, square)

        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            reward = 10
            self.label.config(text="Score:{}".format(self.score))
            self.canvas.delete("food")
            self.food = Food()
            self.food.draw_food(self.canvas)
        else:
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]

        if self.check_collision():
            self.is_game_over = True
            self.game_over()
        else:
            self.window.after(SPEED, self.next_turn)

        return reward, self.is_game_over, self.score
    def change_direction(self, new_direction):
        if new_direction == LEFT and self.direction != RIGHT:
            self.direction = new_direction
        elif new_direction == RIGHT and self.direction != LEFT:
            self.direction = new_direction
        elif new_direction == UP and self.direction != DOWN:
            self.direction = new_direction
        elif new_direction == DOWN and self.direction != UP:
            self.direction = new_direction

    def check_collision(self):
        x, y = self.snake.coordinates[0]

        if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
            return True

        for body_part in self.snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True
        return False

    def game_over(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2, font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")
        self.restart_game()

    def restart_game(self):
        self.canvas.destroy()
        self.label.destroy()
        self.snake = None
        self.food = None
        self.frame_iteration = 0
        self.MainGame()

    def check_collision_specific_cords(self, cords: list):
        x = cords[0]
        y = cords[1]
        if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
            return True


if __name__ == "__main__":
    game = SnakeGame()
    game.MainGame()




