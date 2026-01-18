import pygame




pygame.init()


screen_width, screen_height = 700,700
# Screen Size 
screen = pygame.display.set_mode((screen_width, screen_height))


# Box size
box_width , box_height = 500,500
box_x = (screen_width - box_width) // 2 
box_y = (screen_height - box_height) // 2

# Wall thickness
wall_thickness = 5


# walls
top_wall = pygame.Rect(box_x, box_y, box_width, wall_thickness)
bottom_wall = pygame.Rect(box_x, box_y + box_height - wall_thickness , box_width, wall_thickness)
left_wall = pygame.Rect(box_x, box_y, wall_thickness, box_height)
right_wall = pygame.Rect(box_x + box_width - wall_thickness, box_y, wall_thickness, box_height)


# the inside the box to seprate and work inside the box 
inside_box = pygame.Rect(box_x + wall_thickness, box_y + wall_thickness, box_width - 2 * wall_thickness, box_height - 2 * wall_thickness )

# Ball 
ball_radius = 15 
ball_x = box_x = box_width // 2
ball_y = box_y + box_height // 2  
ball_speed_y = 5 
ball_speed_x = 3 
ball_color = (255,50,50)


running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    # Move the ball 
    ball_x += ball_speed_x
    ball_y += ball_speed_y



    #  Bounce off bottom wall 
    if ball_y + ball_radius >= bottom_wall.top:
        ball_y = bottom_wall.top - ball_radius
        ball_speed_y = -ball_speed_y


    # Bounce off top wall 
    if ball_y - ball_radius <= top_wall.bottom:
        ball_y = top_wall.bottom + ball_radius
        ball_speed_y = -ball_speed_y

    # Left wall
    if ball_x - ball_radius <= left_wall.right:
        ball_x = left_wall.right + ball_radius
        ball_speed_x = -ball_speed_x

    # right wall 
    if ball_x + ball_radius >= right_wall.left:
        ball_x = right_wall.left - ball_radius
        ball_speed_x = -ball_speed_x

    
        


    # Fill the Backgorund color
    screen.fill("black")


    # Draw Walls 
    pygame.draw.rect(screen,(200,200,200), top_wall)
    pygame.draw.rect(screen,(200,200,200), bottom_wall)
    pygame.draw.rect(screen,(200,200,200), left_wall)
    pygame.draw.rect(screen,(200,200,200), right_wall)

    # inside the box 
    pygame.draw.rect(screen, ("blue"), inside_box)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x,ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(60) #fps

pygame.quit()


print (top_wall)
print(bottom_wall)
print(left_wall)

print(right_wall)

print (left_wall.right)
print (ball_x)
print(bottom_wall.top)