import turtle

def koch_curve(t, length, level):
    #Draw a Koch curve with a given level of recursion.
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)
        t.right(120)
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)

def koch_snowflake(t, length, level):
    #Draw a Koch snowflake by drawing three Koch curves.
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

def main():
    # Get the level of recursion from the user
    level = int(input("Enter the level of recursion: "))

    # Set up the turtle graphics
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")
    screen.title("Koch Snowflake")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Draw the Koch snowflake
    length = 400  # Length of each side of the snowflake
    koch_snowflake(t, length, level)

    # Finish drawing
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()