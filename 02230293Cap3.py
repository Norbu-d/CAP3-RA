import pygame
import sys
import time
import random

class Snake:
    def __init__(self):
        # Initialize snake position and body
        self.pos = [100, 50]
        self.body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def move(self):
        # Change direction if the new direction isn't the opposite of current direction
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        # Move snake according to its direction
        if self.direction == 'UP':
            self.pos[1] -= 10
        if self.direction == 'DOWN':
            self.pos[1] += 10
        if self.direction == 'LEFT':
            self.pos[0] -= 10
        if self.direction == 'RIGHT':
            self.pos[0] += 10

        # Add current position to the beginning of the body
        self.body.insert(0, list(self.pos))

class Food:
    def __init__(self, frame_size_x, frame_size_y):
        # Initialize food position randomly within the frame
        self.pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]

# Define window size
frame_size_x = 720
frame_size_y = 480

# Initialize pygame and font module
pygame.init()
pygame.font.init()

# Set up the game window
pygame.display.set_caption('SNAKE GAME')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Set up FPS controller
fps_controller = pygame.time.Clock()

# Initialize game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0
difficulty = 8  # Decreased difficulty level

# Load the music file
pygame.mixer.music.load('Passenger - Let Her Go (Feat. Ed Sheeran - Anniversary Edition) [Official Video].mp3')  # Update 'your_music_file.mp3' with your actual music file path

# Set the music volume (optional)
pygame.mixer.music.set_volume(0.5)  # Adjust the volume as needed (0.0 to 1.0)

# Start playing the music in an infinite loop (-1 indicates loop indefinitely)
pygame.mixer.music.play(-1)

# Function to display game over message

def game_over():
    pygame.mixer.music.stop()  # Stop the music when the game ends
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    
    # Display total score
    total_score_font = pygame.font.SysFont('times new roman', 40)
    total_score_surface = total_score_font.render('Total Score: ' + str(score), True, white)
    total_score_rect = total_score_surface.get_rect()
    total_score_rect.midtop = (frame_size_x/2, frame_size_y/2)
    game_window.blit(total_score_surface, total_score_rect)
    
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Function to display score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)

# Function to display game menu
def game_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        game_window.fill(black)
        my_font = pygame.font.SysFont('times new roman', 60)
        menu_surface = my_font.render('Press ENTER to start', True, white)
        menu_rect = menu_surface.get_rect()
        menu_rect.midtop = (frame_size_x / 2, frame_size_y / 2)
        game_window.blit(menu_surface, menu_rect)
        pygame.display.flip()

# Main game loop
game_menu()  # Show the game menu before starting the game

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Change direction based on key pressed
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            # Prevent snake from moving in opposite direction instantly
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 2
        food_spawn = False
        # Increase difficulty as the snake eats an apple
        difficulty += 1
    else:
        snake_body.pop()

    # Spawning food on the screen
    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True

    # GFX
    game_window.fill(black)
    for pos in snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Snake food
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    # Getting out of bounds
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, white, 'consolas', 20)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(difficulty)
