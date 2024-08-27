def on_logo_touched():
    global start
    start = input.running_time()
    basic.show_icon(IconNames.HEART)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)
 
def on_logo_released():
    global time, mittaus
    time = input.running_time() - start
    mittaus = Math.idiv(time, 1000)
    basic.show_number(Math.idiv(mittaus, 1))
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)
 
mittaus = 0
time = 0
start = 0
radio.set_group(51)
 
def on_forever():
    radio.send_value("rasti3", mittaus)
    radio.send_string("")
basic.forever(on_forever)
 