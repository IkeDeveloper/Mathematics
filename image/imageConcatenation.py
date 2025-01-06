import pygame
from PIL import Image

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
done = False
# Load the images
image1 = Image.open("2dRoad.jpg").resize((screen_width+100,screen_height))
image2 = Image.open("road.png").resize((screen_width+100,screen_height))
image3 = Image.open("road2.png").resize((screen_width+100,screen_height))

# Get the dimensions of the images
width1, height1 = image1.size
width2, height2 = image2.size
width3, height3 = image3.size

# Create a new image with the combined width and the height of the tallest image
new_width = max(width1, width2,width3)
new_height = height1 + height2 + height3
new_image = Image.new("RGB", (new_width, new_height))

# Paste the two images onto the new image
new_image.paste(image1, (0, 0))
new_image.paste(image2, (0, height1))
new_image.paste(image3, (0, height1*2))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.display.update()

    new_image.save("concatenated_image.png")
pygame.quit()
