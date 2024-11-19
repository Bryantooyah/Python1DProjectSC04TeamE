import turtle as tur

# Set up the screen
tur.setup(800, 600)

# Create the player turtle
player = tur.Turtle()

# Set the player's color
player.color("blue")

# Draw Square 
def draw_square():
  for i in range(4):
    player.forward(100)
    player.right(90)