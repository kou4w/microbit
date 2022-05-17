input.onButtonPressed(Button.A, function () {
    答えた数 += 1
})
input.onButtonPressed(Button.AB, function () {
    if (本当の数 > 答えた数) {
        pins.digitalWritePin(DigitalPin.P0, 1)
    }
    if (本当の数 < 答えた数) {
        pins.digitalWritePin(DigitalPin.P3, 1)
    }
    if (答えた数 == 本当の数) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            `)
        basic.pause(5000)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.B, function () {
    答えた数 = 答えた数 - 1
})
let 答えた数 = 0
let 本当の数 = 0
basic.showString("START!")
本当の数 = 5
答えた数 = 0
basic.forever(function () {
    basic.showNumber(答えた数)
})
