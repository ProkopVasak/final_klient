pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
radio.setGroup(69)
radio.setTransmitSerialNumber(true)
radio.setTransmitPower(7)
let enabled = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (enabled == 1) {
        radio.sendValue("vote", 1)
        basic.showString("A")
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (enabled == 1) {
        radio.sendValue("vote", 2)
        basic.showString("B")
    }
    
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
    if (enabled == 1) {
        radio.sendValue("vote", 3)
        basic.showString("C")
    }
    
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    if (enabled == 1) {
        radio.sendValue("vote", 4)
        basic.showString("D")
    }
    
})
radio.onReceivedValue(function on_received_value(name: string, value: number) {
    
    if (name == "enabled" && value == 1) {
        enabled = 1
    }
    
    if (name == "enabled" && value == 0) {
        enabled = 0
        basic.clearScreen()
    }
    
    if (name == "ack" && value == control.deviceSerialNumber()) {
        basic.showIcon(IconNames.Heart)
        basic.pause(300)
        basic.clearScreen()
    }
    
})
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    basic.showIcon(IconNames.Heart)
    basic.pause(3000)
    basic.clearScreen()
})
console.log(control.deviceSerialNumber())
