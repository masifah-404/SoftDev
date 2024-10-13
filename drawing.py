'''Part 4'''

import turtle
from pixart import draw_shape_from_string, draw_grid, draw_shape_from_file

def main():
    """
    Main function that initializes the turtle and prompts the user for input.

    Based on the user's choice, it either draws a shape from input, 
    creates a grid, or draws from a specified file. 
    """
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 200)
    t.pendown()

    choice = input("Enter 'S' to draw a shape from input, 'G' to draw a grid, 'F' to draw from file: ")

    if choice == 'S':
        draw_shape_from_string(t)
    elif choice == 'G':
        draw_grid(t)
    elif choice == 'F':
        draw_shape_from_file(t)
    else:
        print("Invalid choice")

    turtle.done()

if __name__ == "__main__":
    main()