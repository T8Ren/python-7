'''
4. Timers
    wn.ontimer(func, 500)   # run func once, in 500 ms

    a) Every 200 ms: forward 20, left 15.
       (Hint: the function calls ontimer on itself.)
    b) Stop after 24 steps. Where does it end up, and why?
'''
import turtle
wn = turtle.Screen()
t = turtle.Turtle()

wn.mainloop()