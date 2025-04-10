def on_button_pressed_ab():
    global Level, Delay, AB
    Level = 1
    Delay = 0
    for index in range(2 * Level):
        AB = randint(0, 10)
        if AB % 2 == 0:
            pass
        else:
            pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

AB = 0
Delay = 0
Level = 0
basic.show_leds("""
    . . . . .
    . # . # .
    # # . # #
    . # . # .
    . . . . .
    """)