import pyxel
import random

class App:
    def __init__(self):
        # Initialize the Pyxel window (width, height)
        pyxel.init(160, 120)

        pyxel.load("my_resource.pyxres")
x

        # Set the initial position of the square
        self.x = 80
        self.y = 100
        self.score = 0

        # Set the initial position and velocity of the sprite
        self.sprite_x = 80
        self.sprite_y = 30
        self.sprite_dx = 2
        self.sprite_dy = 2

        # Set the initial position and velocity of the new sprite
        self.new_sprite_x = 50
        self.new_sprite_y = 80

        # Set the initial position and velocity of the new sprite
        self.new_sprite2_x = 50
        self.new_sprite2_y = 80

        # Create a list to store new sprite positions
        self.new_sprites = []
        for _ in range(5):  # Create 5 new sprites
            self.new_sprites.append((random.randint(0, 160), random.randint(0, 120)))

        # Start the game loop
        pyxel.run(self.update, self.draw)

    def update(self):
        # Update the square's position based on arrow keys
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2

        if pyxel.btn(pyxel.KEY_W):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_S):
            self.y += 2
        if pyxel.btn(pyxel.KEY_A):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_D):
            self.x += 2

        # Wrap around
        self.x %= 160
        self.y %= 120

        # Decrease score if square touches the rotten sprites
        if abs(self.x - self.sprite_x) < 10 and abs(self.y - self.sprite_y) < 10:
            self.score -= 1  
            self.sprite_x = random.randint(0, 160)  # Generate random x-coordinate
            self.sprite_y = random.randint(0, 120)  # Generate random y-coordinate
        elif abs(self.x - self.sprite_x) < 10 and abs(self.y - self.sprite_y) < 10:
            self.score -= 1  
            self.sprite_x = -100 # Move sprite off screen
            self.sprite_y = -100

        # Increase score if square touches the good sprites
        for i, (sprite_x, sprite_y) in enumerate(self.new_sprites):
            if abs(self.x - sprite_x) < 10 and abs(self.y - sprite_y) < 10:
                self.score += 2
                self.new_sprites[i] = (random.randint(0, 160), random.randint(0, 120))  # Regenerate sprite position
                # break  # Only process one sprite collision per frame
        # Update the sprite's position
        self.sprite_y += self.sprite_dy

        # Bounce the sprite off the edges of the screen

    def draw(self):
        # Clear the screen with black (color 1)
        pyxel.cls(5)

        # Draw a square (color 9)
        pyxel.blt(self.x, self.y, 0, 0, 16, 16, 16, 0)

        # Draw the moving sprite (color 11)
        pyxel.blt(self.sprite_x, self.sprite_y, 0, 0, 0, 19, 19, 0)

        # Draw the moving sprite (color 8)
        pyxel.blt(self.sprite_x, self.sprite_y, 0, 0, 0, 16, 16, 0)

        pyxel.blt(self.new_sprite_x, self.new_sprite_y, 0, 0, 32, 16, 16, 0)

        # Draw new sprites from the list
        for sprite_x, sprite_y in self.new_sprites:
            pyxel.blt(sprite_x, sprite_y, 0, 0, 32, 16, 16, 0)

        # Draw the second new sprite
        pyxel.blt(self.new_sprite2_x, self.new_sprite2_y, 0, 16, 32, 16, 16, 0)

        # Display the score
        pyxel.text(5, 5, f"Score: {self.score}", 7)

        # Display a message when score is low
        if self.score <= -1:
            pyxel.text(35, 50, "Avoid the rotten food!", 8)
            pyxel.text(20, 30, "Collect candy and ripe foods!", 8)

# Run the game
App()
# pyxel.blt(50, 50, 2, 0, 0, 16, 16, 0)  Draws a 16x16 sprite from bank 0