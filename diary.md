
# ChatGPT Coding Diary

## Project Name: _[KSC]_

### Date: _[11/25]_

---

## 1. **Task/Problem Description**

I need to create a program that has a loop that makes the player go up and down to avoid obstacles


---

## 2. **Initial Approach/Code**

Describe the initial approach you took to solving the problem. If you started writing code, include it here.


import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Background Example')

background = pygame.image.load('background.jpg')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()


- What was your plan for solving the problem?
My initial plan for solving the problem was to create a background with a player that can move up and down by creating a loop
- Did you have any initial thoughts or strategies before using ChatGPT?
No
---

## 3. **Interaction with ChatGPT**

### Questions/Requests to ChatGPT
Write down the questions or requests you made to ChatGPT. 

"Why is my background not appearing on the screen?"
"How to change the initial position of my shape?"

- Why did ChatGPT opt for create element when my teacher suggested insertAdjacentHTML?

```text
# Example prompt to ChatGPT:
How can I optimize this sorting function for large datasets?
```

---

## 4. **ChatGPT's Suggestions/Code Changes**

Record the code or suggestions ChatGPT provided. Include any changes or improvements ChatGPT suggested and how it influenced your approach.

```python
# ChatGPT suggested using a custom sorting algorithm to improve efficiency
def optimized_sort(numbers):
    # Implementation of a more efficient sorting algorithm
    pass
```

Chat GPT taught us how to correctly create a object controlled by the player and have obstacles coming at the player. We also learned how change the player's appearance and color.

- What was ChatGPT's solution or suggestion?
- How did it differ from your original approach?

---

## 5. **Reflection on Changes**

Reflect on the changes made to your code after ChatGPT's suggestions. Answer the following questions:

- Why do you think ChatGPT's suggestions are helpful or relevant?
- Did the suggestions improve your code? How?
- Did you understand why the changes were made, or are you still uncertain about some parts?

Example:
> ChatGPT recommended using a more efficient sorting algorithm like quicksort. I think this will improve the runtime for large inputs, but I need to review the algorithm's complexity to fully understand its advantages.

---

## 6. **Testing and Results**

After making the changes, did you test your code? What were the results?

- Did you run any tests (e.g., unit tests, edge cases)?
- Did the code work as expected after incorporating ChatGPT's changes?

```python
# Example: Testing the updated sorting function
numbers = [5, 2, 9, 1]
print(optimized_sort(numbers))  # Expected output: [1, 2, 5, 9]
```

- Did you encounter any bugs or issues during testing?

---

## 7. **What Did You Learn?**

In this section, reflect on what you learned from this coding session. Did you gain any new insights, or were there areas you still struggled with? 

Example:
> I learned how to implement an efficient sorting algorithm, and I now understand the time complexity differences between various sorting methods.

---
