import turtle
import random

def create_turtle(color, y):
    new_turtle = turtle.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-240, y)
    new_turtle.speed(1)  # Set movement speed
    return new_turtle

def race(turtles):
    global turtles_running
    while turtles_running:
        for t in turtles:
            t.forward(random.randint(1, 10))
            if t.xcor() >= 230:
                turtles_running = False
                return t.color()[0]  # Return the color of the winning turtle

def setup_turtles():
    colors = ["red", "blue", "green", "orange", "purple"]
    y_positions = [100, 60, 20, -20, -60]
    return [create_turtle(color, y) for color, y in zip(colors, y_positions)]

def draw_track():
    track = turtle.Turtle()
    track.speed(0)
    track.penup()
    track.goto(-250, 150)
    track.pendown()
    track.goto(250, 150)
    track.goto(250, -150)
    track.goto(-250, -150)
    track.goto(-250, 150)
    for position in [-230, 230]:  # Start and finish lines
        track.penup()
        track.goto(position, 150)
        track.pendown()
        track.goto(position, -150)
    track.hideturtle()

def draw_button(label, button_x, button_y, label_x, label_y, function):
    # Create the button shape
    button = turtle.Turtle()
    button.speed(0)
    button.penup()
    button.goto(button_x, button_y)
    button.shape("square")
    button.shapesize(2, 2)
    button.color("white")
    button.fillcolor("lightgray")
    button.onclick(function)
    button.showturtle()

    # Create the label separately
    label_turtle = turtle.Turtle()
    label_turtle.hideturtle()
    label_turtle.penup()
    label_turtle.goto(label_x, label_y)
    label_turtle.write(label, align="center", font=("Courier", 16, "normal"))

def main():
    global screen, turtles_running, turtles
    screen = turtle.Screen()
    screen.setup(width=600, height=400)
    screen.title("Turtle Racing Game")
    screen.bgcolor("lightblue")

    draw_track()
    turtles = setup_turtles()

    # Draw buttons with separate positions for the buttons and the labels
    draw_button("Start", -100, -220, -100, -200, lambda x, y: start_race())
    draw_button("Stop", 0, -220, 0, -200, lambda x, y: stop_race())
    draw_button("Replay", 100, -220, 100, -200, lambda x, y: replay_race())

def start_race():
    global turtles_running
    turtles_running = True
    winner_color = race(turtles)
    if winner_color:
        print("The winner is:", winner_color)

def stop_race():
    global turtles_running
    turtles_running = False

def replay_race():
    turtle.clearscreen()  # Clear the current screen
    main()  # Reinitialize the game setup

if __name__ == "__main__":
    main()
    turtle.mainloop()  # Keep the window open
