'''
3. Events
    def up():
        t.forward(30)
    wn.onkey(up, "Up")      # key -> function
    wn.onclick(click)       # click -> function(x, y)

    a) Left/Right arrow turns 45 degrees.
    b) Clicking moves the turtle to the click.
    c) Why  onkey(up, "Up")  and not  onkey(up(), "Up") ?
'''
import turtle
wn = turtle.Screen()
t = turtle.Turtle()

wn.listen()
wn.mainloop()
