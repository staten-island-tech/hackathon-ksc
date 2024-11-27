
# ChatGPT Coding Diary

## Project Name: KSC game

### Date: _11/25/24_

---

## 1. **Task/Problem Description**

``text
I need to create an program using pygame, that allows the player to move a character to jump over obstacles.
``

---

## 2. **Initial Approach/Code**

```python
import pygame
pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Game")

running = True 
while running:
    for event in pygame.event.get():
        screen.fill((235, 192, 230))
        if event.type == pygame.QUIT:
            running = False
    
    
screen.fill((100, 0, 0))
pygame.display.update()
```

My initial approch to this project is to create an basic pygame window and a game loop. I haven’t yet added any gameplay mechanics.

---

## 3. **Interaction with ChatGPT**

### Questions/Requests to ChatGPT

```text
How can I add controls to make the dinosaur jump over obstacles?
```

---

## 4. **ChatGPT's Suggestions/Code Changes**

```python
import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dinosaur Game")

# Dinosaur setup
dino_width = 50
dino_height = 50
dino_x = 100
dino_y = screen_height - dino_height - 20
is_jumping = False
jump_velocity = 10
gravity = 0.5
y_velocity = 0

# Obstacle setup
obstacle_width = 30
obstacle_height = 30
obstacle_x = screen_width
obstacle_y = screen_height - obstacle_height - 20
obstacle_speed = 5

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls for jumping
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        y_velocity = -jump_velocity

    # Update dinosaur position
    if is_jumping:
        dino_y += y_velocity
        y_velocity += gravity
        if dino_y >= screen_height - dino_height - 20:  # Stop jump when hitting the ground
            dino_y = screen_height - dino_height - 20
            is_jumping = False

    # Update obstacle position
    obstacle_x -= obstacle_speed
    if obstacle_x < -obstacle_width:
        obstacle_x = screen_width

    # Check for collision
    if dino_x < obstacle_x + obstacle_width and dino_x + dino_width > obstacle_x and dino_y + dino_height > obstacle_y:
        running = False  # End game on collision

    # Draw background, dinosaur, and obstacle
    screen.fill((200, 200, 200))
    pygame.draw.rect(screen, (0, 150, 0), (dino_x, dino_y, dino_width, dino_height))
    pygame.draw.rect(screen, (200, 50, 50), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    pygame.display.update()
    pygame.time.Clock().tick(30)

pygame.quit()
    pass
```

- ChatGPT's solution was to add a character with variables. Also adding a moving obstacles, and if the character hits an obstacles, the game restarts. 
- In my orginal approach, I didn't know how to start, so I only created a pygame window with a game loop and background but had no gameplay mechanics or objects

---

## 5. **Reflection on Changes**

ChatGPT was helpful in setting up movement. The game loop now allows the player to press the space to make the character jump over objects. Obstacles move across the screen, and ends the game when hit. 

---

## 6. **Testing and Results**
I ran the updated code, and the character can jump over obstacles. If the character hits an obstacle, the game stops.

---

## 7. **What Did You Learn?**

I learned how to use jumping mechanics, create and move obstacles across the screen, and end the game when an object is touched.

---