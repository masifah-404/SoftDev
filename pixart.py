import turtle

'''Part 1'''

def get_color(character):
    """
    Returns the color name corresponding to the given character.
    
    If the character has no corresponding color, it returns None.
    """
    if character == '0':
        return 'black'
    elif character == '1':
        return 'white'
    elif character == '2':
        return 'red'
    elif character == '3':
        return 'yellow'
    elif character == '4':
        return 'orange'
    elif character == '5':
        return 'green'
    elif character == '6':
        return 'yellowgreen'
    elif character == '7':
        return 'sienna'
    elif character == '8':
        return 'tan'
    elif character == '9':
        return 'gray'
    elif character == 'A':
        return 'darkgray'
    else:
        return None

def draw_color_pixel(color_string, turta):
    """
    Draws a single pixel of the specified color using the turtle.
    
    This function creates a filled square in the given color.
    """
    turta.fillcolor(color_string)
    turta.begin_fill()
    for _ in range(4):
        turta.forward(20)
        turta.right(90)
    turta.end_fill()
    turta.forward(20)

def draw_pixel(character, turta):
    """
    Draws a pixel based on the character provided.
    
    It draws the color corresponding to the character. Returns False if the character is invalid.
    """
    color_string = get_color(character)
    if color_string:
        draw_color_pixel(color_string, turta)
    else:
        return False  # Invalid character
    return True  # Valid character

def draw_line_from_string(color_string, turta):
    """
    Draws a line of pixels from a string of color characters.
    
    The drawing stops if an invalid character is encountered. Returns True if all colors are valid, otherwise False.
    """
    for char in color_string:
        if draw_pixel(char, turta) == False:
            return False
    turta.setheading(180)
    turta.forward(len(color_string) * 20)
    turta.setheading(0)
    return True

def draw_shape_from_string(turta):
    """
    Prompts the user for color strings to draw lines of pixels.
    
    Continues prompting until the user enters an empty string.
    """
    while True:
        color_string = input("Enter a color string (or press Enter to stop): ")
        if color_string == "":
            break
        draw_line_from_string(color_string, turta)

        turta.penup()
        turta.right(90)
        turta.forward(20)
        turta.left(90)
        turta.pendown()

'''Part 2'''

def draw_grid(turta):
    """
    Draws a 20x20 checkerboard pattern using alternating lines of colors.
    """
    for loop in range(1, 10):
        color_string = "02020202020202020202"
        draw_line_from_string(color_string, turta)

        turta.penup()
        turta.right(90)
        turta.forward(20)
        turta.left(90)
        turta.pendown()

        color_string = "20202020202020202020"
        draw_line_from_string(color_string, turta)

        turta.penup()
        turta.right(90)
        turta.forward(20)
        turta.left(90)
        turta.pendown()

'''Part 3'''

def draw_shape_from_file(turta):
    """
    Reads a color string from a file and draws pixels accordingly.
    
    Prompts the user for the file path and draws the shapes based on its contents.
    """
    file_path = input("Enter the path of the file that you want to read its content: ")
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                draw_line_from_string(line, turta)

                turta.penup()
                turta.right(90)
                turta.forward(20)
                turta.left(90)
                turta.pendown()
    except FileNotFoundError:
        print("File not found: " + file_path)