# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Add the encoder
encoder=EncoderHandler()
keyboard.modules.append(encoder)


# Define your pins here!
PINS = [board.GP26, board.GP27, board.GP28, board.GP29, board.GP4]
encoder.pins=((board.GP2, board.GP1),)

encoder=EncoderHandler()
keyboard.modules.append(encoder)

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

UNDO = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.Z),
    Release(KC.LCTL)
)

COPY = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.C),
    Release(KC.LCTL)
)

PASTE = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.V),
    Release(KC.LCTL)
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [UNDO, KC.DELETE, COPY, PASTE, KC.PAUSE]
]

encoder.map=[
    (KC.F13, KC.F14)
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()

