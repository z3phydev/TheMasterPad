import board
import digitalio
import usb_hid
import rotaryio
import time

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

keyboard = Keyboard(usb_hid.devices)
consumer = ConsumerControl(usb_hid.devices)
encoder = rotaryio.IncrementalEncoder(board.GP0, board.GP2)
last_position = encoder.position
encoder_button = digitalio.DigitalInOut(board.GP1)
encoder_button.direction = digitalio.Direction.INPUT
encoder_button.pull = digitalio.Pull.UP

macro_pins = [
    board.GP3, board.GP4, board.GP5, board.GP6,
    board.GP7, board.GP8, board.GP9, board.GP10
]

buttons = []

for pin in macro_pins:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    buttons.append(btn)

last_button_states = [True] * len(buttons)
last_encoder_button = True

While True:
    position = encoder.position

    if position > last_position:
        consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
    elif position < last_position:
        consumer.send(ConsumerControlCode.VOLUME_DECREMENT)

    last_position = position

    if not encoder_button.value and last_encoder_button:
        consumer.send(ConsumerControlCode.MUTE)
        time.sleep(0.2)

    last_encoder_button = encoder_button.value

    for i, button in enumerate(buttons):
        if not button.value and last_button_states[i]:
            # Example macros (edit these)
            if i == 0:
                keyboard.send(Keycode.CONTROL, Keycode.C)   # Copy
            elif i == 1:
                keyboard.send(Keycode.CONTROL, Keycode.V)   # Paste
            elif i == 2:
                keyboard.send(Keycode.CONTROL, Keycode.Z)   # Undo
            elif i == 3:
                keyboard.send(Keycode.CONTROL, Keycode.S)   # Save
            elif i == 4:
                keyboard.send(Keycode.ALT, Keycode.TAB)     # App switch
            elif i == 5:
                keyboard.send(Keycode.GUI, Keycode.D)       # Show desktop
            elif i == 6:
                keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.ESC)  # Task manager
            elif i == 7:
                keyboard.send(Keycode.F5)                   # Refresh or Run depending on the app

            time.sleep(0.2)

        last_button_states[i] = button.value

    time.sleep(0.01)
