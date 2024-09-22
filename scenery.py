import turtle

# Function to draw a rectangle
def draw_rectangle(width, height, color):
    """
    Draws a filled rectangle using the turtle.
    Arguments:
    width -- width of the rectangle
    height -- height of the rectangle
    color -- fill color of the rectangle
    """
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()

# Function to draw a circle (e.g., for decoration or candle flame)
def draw_circle(radius, color):
    """
    Draws a filled circle using the turtle.
    Arguments:
    radius -- radius of the circle
    color -- fill color of the circle
    """
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Function to draw a table with 4 legs, front legs taller than back legs
def draw_table(width, height, leg_height, leg_height_back, color):
    """
    Draws a table with 4 legs (2 front and 2 back, back legs shorter).
    Arguments:
    width -- width of the table top
    height -- height of the table top
    leg_height -- height of the front legs
    leg_height_back -- height of the back legs (for perspective)
    color -- fill color of the table
    """
    # Draw table top
    draw_rectangle(width, height, color)
    
    leg_width = 10  # Width of the legs
    
    # Front left leg
    turtle.penup()
    turtle.goto(-width / 2, -leg_height)
    turtle.pendown()
    draw_rectangle(leg_width, leg_height, color)
    
    # Front right leg
    turtle.penup()
    turtle.goto(width / 2 - leg_width, -leg_height)
    turtle.pendown()
    draw_rectangle(leg_width, leg_height, color)
    
    # Back left leg (shorter for perspective)
    turtle.penup()
    turtle.goto(-width / 3, -leg_height_back)
    turtle.pendown()
    draw_rectangle(leg_width, leg_height_back, color)
    
    # Back right leg (shorter for perspective)
    turtle.penup()
    turtle.goto(width / 3 - leg_width, -leg_height_back)
    turtle.pendown()
    draw_rectangle(leg_width, leg_height_back, color)

# Function to draw a 3-layer birthday cake with a decoration and 4 candles
def draw_cake(cake_width, cake_height, layer_colors, decoration_size, decoration_color):
    """
    Draws a 3-layer birthday cake with a decoration and 4 candles.
    Arguments:
    cake_width -- width of the cake
    cake_height -- height of each layer
    layer_colors -- list of 3 colors for the cake layers
    decoration_size -- size of the decoration
    decoration_color -- fill color of the decoration
    """
    # Draw the 3 cake layers (bottom, middle, top)
    turtle.penup()
    turtle.goto(-cake_width / 2, 20)
    turtle.pendown()
    draw_rectangle(cake_width, cake_height, layer_colors[0])  # Bottom layer

    turtle.penup()
    turtle.goto(-cake_width / 2 + 10, cake_height + 20)  # Make the middle layer slightly smaller
    turtle.pendown()
    draw_rectangle(cake_width - 20, cake_height, layer_colors[1])  # Middle layer

    turtle.penup()
    turtle.goto(-cake_width / 2 + 20, cake_height * 2 + 20)  # Make the top layer even smaller
    turtle.pendown()
    draw_rectangle(cake_width - 40, cake_height, layer_colors[2])  # Top layer

    # Draw a decoration (circle) on top of the cake
    turtle.penup()
    turtle.goto(0, cake_height * 3 + 20)  # Position the decoration on top
    turtle.pendown()
    draw_circle(decoration_size, decoration_color)

    # Draw 4 candles around the decoration
    candle_height = 20
    candle_width = 5
    # Candle 1
    turtle.penup()
    turtle.goto(-20, cake_height * 3 + 20)
    turtle.pendown()
    draw_rectangle(candle_width, candle_height, "yellow")
    
    # Candle 2
    turtle.penup()
    turtle.goto(-12, cake_height * 3 + 20)
    turtle.pendown()
    draw_rectangle(candle_width, candle_height, "yellow")
    
    # Candle 3
    turtle.penup()
    turtle.goto(15, cake_height * 3 + 20)
    turtle.pendown()
    draw_rectangle(candle_width, candle_height, "yellow")
        
    # Candle 4
    turtle.penup()
    turtle.goto(7, cake_height * 3 + 20)
    turtle.pendown()
    draw_rectangle(candle_width, candle_height, "yellow")
    
    # Draw candle flames
    turtle.penup()
    turtle.goto(-18, cake_height * 3 + candle_height + 20)
    turtle.pendown()
    draw_circle(3, "orange")  # Flame for candle 1
    
    turtle.penup()
    turtle.goto(-10, cake_height * 3 + candle_height + 20)
    turtle.pendown()
    draw_circle(3, "orange")  # Flame for candle 2
    
    turtle.penup()
    turtle.goto(9, cake_height * 3 + candle_height + 20)
    turtle.pendown()
    draw_circle(3, "orange")  # Flame for candle 3
    
    turtle.penup()
    turtle.goto(17, cake_height * 3 + candle_height + 20)
    turtle.pendown()
    draw_circle(3, "orange")  # Flame for candle 4

# Main program function
def main():
    """
    Main program to ask the user for input and draw the table, cake, and candle.
    """
    # Ask user for table properties
    table_color = input("Enter the table color: ")
    table_width = int(input("Enter the table width: "))
    table_height = int(input("Enter the table height: "))
    leg_height = int(input("Enter the table leg height (front legs): "))
    leg_height_back = int(input("Enter the table leg height (back legs): "))
    
    # Ask user for cake properties
    cake_colors = []
    cake_colors.append(input("Enter the bottom layer color of the cake: "))
    cake_colors.append(input("Enter the middle layer color of the cake: "))
    cake_colors.append(input("Enter the top layer color of the cake: "))
    cake_width = int(input("Enter the cake width: "))
    cake_height = int(input("Enter the height of each cake layer: "))
    decoration_color = input("Enter the decoration color: ")
    decoration_size = int(input("Enter the decoration size (radius): "))
    
    # Set up the canvas size based on the table and cake size
    turtle.screensize(table_width + 200, table_height + leg_height + cake_height * 3 + 200)
    turtle.speed(1)  # Set turtle drawing speed
    turtle.penup()
    turtle.goto(-table_width / 2, 0)
    turtle.pendown()

    # Draw the table and the cake
    draw_table(table_width, table_height, leg_height, leg_height_back, table_color)
    turtle.penup()
    turtle.goto(0, table_height)
    turtle.pendown()
    draw_cake(cake_width, cake_height, cake_colors, decoration_size, decoration_color)
    
    # Go back to original position
    turtle.penup()
    turtle.goto(-table_width / 2, 0)

    # Wait for user to close the window
    input("Press any key to exit")

# Run the program
if __name__ == "__main__":
    main()