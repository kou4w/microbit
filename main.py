def on_button_pressed_a():
    global 答えた数
    答えた数 += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if 本当の数 > 答えた数:
        pins.digital_write_pin(DigitalPin.P0, 1)
    if 本当の数 < 答えた数:
        pins.digital_write_pin(DigitalPin.P3, 1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global 答えた数
    答えた数 = 答えた数 - 1
input.on_button_pressed(Button.B, on_button_pressed_b)

答えた数 = 0
本当の数 = 0
本当の数 = 5
答えた数 = 0

def on_forever():
    if 答えた数 == 本当の数:
        I2C_LCD1602.clear()
    else:
        I2C_LCD1602.show_string("answered:", 0, 0)
        I2C_LCD1602.show_number(答えた数, 10, 0)
basic.forever(on_forever)
