import math
from turtle import *

def heart_x(k):
    return 16 * math.sin(k) ** 3

def heart_y(k):
    return 13 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

def draw_creative_heart():
    speed(0)
    bgcolor("black")
    colors = ["red", "hot pink"]
    for offset in range(2):
        penup()
        goto(0, 0)
        pendown()
        color(colors[offset])
        pensize(2)
        for i in range(0, 6000, 10):
            k = i * 0.001
            x = heart_x(k) * (20 + offset * 2)
            y = heart_y(k) * (20 + offset * 2)
            goto(x, y)
            if i % 200 == 0:
                for j in range(10):
                    forward(offset + 2)
                    right(30)

def draw_arrow_and_text():
    penup()
    goto(-420, 130)  # Start point of the arrow
    pendown()
    color("white")
    pensize(4)
    setheading(-15)  # Set the angle to match the original image
    forward(850)  # Length of the arrow
    # Adding arrowhead
    setheading(-15)  # Continue the same angle for the arrowhead
    forward(20)  # Length of the arrowhead
    backward(20)  # Move back to the end of the arrow line
    left(150)  # Create the left side of the arrowhead
    forward(20)
    backward(20)  # Reset position for the next movement
    right(300)  # Create the right side of the arrowhead
    forward(20)
    penup()

    goto(-480, 160)  # Position for 'K' (lowered slightly)
    pencolor("white")
    style = ('Comic Sans MS', 64, 'italic')  # Hand-drawn style font
    write("K", align="center", font=style)

    goto(470, 0)  # Position for 'A' (lowered slightly)
    write("A", align="center", font=style)

def add_copyright():
    penup()
    goto(350, -350)
    color("gray")
    write("© KA cc", align="right", font=("Arial", 12, "normal"))

if __name__ == "__main__":
    setup(800, 800)
    title("Heart with Diagonal Arrow and Text")
    showturtle()
    draw_creative_heart()
    draw_arrow_and_text()
    add_copyright()
    done()
