pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)
radio.set_group(69)
radio.set_transmit_serial_number(True)
radio.set_transmit_power(7)
enabled = 0

def on_button_pressed_a():
    global enabled
    if enabled == 1:
        radio.send_value("vote", 1)
        basic.show_string("A")
        
    
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    global enabled
    if enabled == 1:
        radio.send_value("vote", 2)
        basic.show_string("B")
        
    
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_pin_pressed_p1():
    global enabled
    if enabled == 1:
        radio.send_value("vote", 3)
        basic.show_string("C")
        
    
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
def on_pin_pressed_p2():
    global enabled
    if enabled == 1:
        radio.send_value("vote", 4)
        basic.show_string("D")
        
    
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_received_value(name, value):
    global enabled
    if name == "enabled" and value == 1:
        enabled = 1
        
    if name == "enabled" and value == 0:
        enabled = 0
        basic.clear_screen()
        
    if name == "ack" and value == control.device_serial_number():
        
        basic.show_icon(IconNames.HEART)
        basic.pause(300)
        basic.clear_screen()
radio.on_received_value(on_received_value)

def on_received_number(receivedNumber):
    basic.show_icon(IconNames.HEART)
    basic.pause(3000)
    basic.clear_screen()
radio.on_received_number(on_received_number)
print(control.device_serial_number())
