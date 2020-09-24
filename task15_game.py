# Using the existing code from 'example.py' and adding the following addition
# funstionalities:
# 1. Add movement for the left and right arrow keys.
# 2. Add 2 additional enemies. Each moving in a different direction.
# 3. Add a prize, which allows the user to win when the player collides with it.

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1360
screen_height = 768
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this
# folder (similarly with the enemy and prize images).

# The same image is used for the three enemies.

player = pygame.image.load("player.jpg")
enemy1 = pygame.image.load("monster.jpg")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize1.jpg")


# Get the width and height of the images in order to do boundary detection
# (i.e. make sure the image stays within screen boundaries or know
# when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy1.get_height()
enemy_width = enemy1.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player and enemy as variables so that you
# can change them later. 

playerXPosition = 200 # Horizontal position
playerYPosition = 50 # Vertical position

# Store the position of the prize. Make it as far away as possible
# from the player position to make it more challenging.
prizeXPosition = (screen_width - prize_width)
prizeYPosition = (screen_height - prize_height)

# Make enemy1 start off screen at the right hand at a random y position.
# Make enemy2 start off screen at the left hand at a random y position.
# Make enemy3 start off screen at the bottom at a random x position. 
enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy_height)
enemy2XPosition =  (0-enemy_width)
enemy2YPosition =  random.randint(0, screen_height - enemy_height)
enemy3XPosition =  random.randint(0, screen_width - enemy_width)
enemy3YPosition =  screen_height

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test
# conditions and test states that are binary, i.e. either one way or the other.
# This is done for all four arrow keys.

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting).
    # In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false.
    # You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structures later. 

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # This event checks if the user press a key down. 
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position.
    # When the right/left arrows are pressed, the player needs to move in the x-direction.
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0: # Ensures the user does not move the player off screen to the left.
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - image_width: # Ensures that the user does not move the player off screen to the right.
            playerXPosition += 1
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Need to check for collision of the player with the prize. Need to determine
    # boundary for the prize. It is static (prize stays in one place).

    # Bounding box for the prize:
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Bounding boxes for the enemies:
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemy1Box)or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
        
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)
        
    # If the enemies are off the screen the user wins the game:
    if (enemy1XPosition < 0) and (enemy2XPosition > screen_width) and (enemy3YPosition < 0):
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
        
    # If the player collides with the prize the user wins. 
    if playerBox.colliderect(prizeBox):
        print("You win!")

        pygame.quit()

        exit(0)
    
    
    # Make enemies approach the player.To increase the speed of the eniemies,
    # increase the values below.
    
    enemy1XPosition -= 0.15
    enemy2XPosition += 0.15
    enemy3YPosition -= 0.15
    # ================The game loop logic ends here. =============
  
