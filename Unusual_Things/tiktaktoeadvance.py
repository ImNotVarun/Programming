import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set block size
block_size = 20

# Create font object
font = pygame.font.Font(None, 36)

def generate_maze(width, height):
    maze = [['#' for x in range(width)] for y in range(height)]
    start_x = random.randint(0, width - 1)
    start_y = 0
    end_x = random.randint(0, width - 1)
    end_y = height - 1
    maze[start_y][start_x] = 'S'
    maze[end_y][end_x] = 'E'
    carve_path(maze, start_x, start_y)
    return maze

def carve_path(maze, x, y):
    directions = ['N', 'S', 'E', 'W']
    random.shuffle(directions)
    for direction in directions:
        if direction == 'N':
            if y - 2 <= 0:
                continue
            if maze[y - 2][x] == '#':
                maze[y - 1][x] = ' '
                maze[y - 2][x] = ' '
                carve_path(maze, x, y - 2)
        elif direction == 'S':
            if y + 2 >= len(maze) - 1:
                continue
            if maze[y + 2][x] == '#':
                maze[y + 1][x] = ' '
                maze[y + 2][x] = ' '
                carve_path(maze, x, y + 2)
        elif direction == 'E':
            if x + 2 >= len(maze[0]) - 1:
                continue
            if maze[y][x + 2] == '#':
                maze[y][x + 1] = ' '
                maze[y][x + 2] = ' '
                carve_path(maze, x + 2, y)
        else:
            if x - 2 <= 0:
                continue
            if maze[y][x - 2] == '#':
                maze[y][x - 1] = ' '
                maze[y][x - 2] = ' '
                carve_path(maze, x - 2, y)

def draw_maze(maze):
    for y,row in enumerate(maze):
        for x,char in enumerate(row):
            rect = pygame.Rect(x*block_size,y*block_size,block_size,block_size)
            if char == '#':
                pygame.draw.rect(screen,black,rect)
            elif char == 'S':
                pygame.draw.rect(screen,green,rect)
            elif char == 'E':
                pygame.draw.rect(screen,red,rect)

width = screen_width // block_size
height = screen_height // block_size

maze = generate_maze(width,height)

start_x = [row.index('S') for row in maze if 'S' in row][0]
start_y = [i for i,row in enumerate(maze) if 'S' in row][0]
end_x = [row.index('E') for row in maze if 'E' in row][0]
end_y = [i for i,row in enumerate(maze) if 'E' in row][0]

player_x = start_x
player_y = start_y

clock = pygame.time.Clock()

done = False

while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_y > 0 and maze[player_y-1][player_x] != '#':
                player_y -=1
            elif event.key == pygame.K_DOWN and player_y < height-1 and maze[player_y+1][player_x] != '#':
                player_y +=1
            elif event.key == pygame.K_LEFT and player_x >0 and maze[player_y][player_x-1] != '#':
                player_x -=1
            elif event.key == pygame.K_RIGHT and player_x < width-1 and maze[player_y][player_x+1] != '#':
                player_x +=1

    # Draw screen
    screen.fill(white)
    draw_maze(maze)
    rect=pygame.Rect(player_x*block_size+5 ,player_y*block_size+5 ,block_size-10 ,block_size-10 )
    pygame.draw.ellipse(screen ,green ,rect )
    
    # Check if player has reached the end of the maze
    if player_x == end_x and player_y == end_y:
        text = font.render("Congratulations! You've reached the end of the maze!", True, red)
        text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
        screen.blit(text, text_rect)
        done = True
    
    # Update screen
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(60)

# Wait for user to close window
while True:
    event=pygame.event.wait()
    if event.type==pygame.QUIT:
        break

# Quit Pygame
pygame.quit()
