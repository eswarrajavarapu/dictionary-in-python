from tkinter import *
import random
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 200
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'
BACKGROUND_COLOR = '#000000'
window = Tk()
window.title('Snake Game')
window.resizable(False, False)
score = 0
direction = 'down'
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y,x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)
def change_direction(new_direction):
    global direction
    if new_direction=='left':
        if direction != 'right':
            direction = new_direction
    elif new_direction=='right':
        if direction != 'left':
            direction = new_direction
    elif new_direction=='up':
        if direction != 'down':
            direction = new_direction
    elif new_direction=='down':
        if direction != 'up':
            direction = new_direction
def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x<0 or x>=GAME_WIDTH:
        print('Game Over')
        return True
    if y<0 or y>=GAME_HEIGHT:
        print('Game Over')
        return True
    return False
def game_over():
    canvas.delete('all')
    canvas.create_text(GAME_WIDTH//2, GAME_HEIGHT//2, font=('Arial',20,'bold'),text ='game over' ,fill=FOOD_COLOR, tag ='gameover')
    canvas.update()







class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH//SPACE_SIZE)-1)*SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT//SPACE_SIZE)-1)*SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR, tag='food')
def next_turn(snake,food):
    x, y = snake.coordinates[0]
    if direction == 'down':
        y += SPACE_SIZE
    elif direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x,y))
    square = canvas.create_rectangle(x,y,x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    global score
    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text = 'score:{}'.format(score))
        canvas.delete('food')
        food = Food()
    else:


        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)








label = Label(window, text='Score: {}'.format(score), font=('consolas', 40))
label.pack()
canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg= BACKGROUND_COLOR)
canvas.pack()
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f'{window_width}x{window_height}+{x}+{y}')
food = Food()
snake = Snake()
next_turn(snake, food)
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))


window.mainloop()
