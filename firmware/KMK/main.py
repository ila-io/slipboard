import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

# === Setup ===
keyboard = KMKKeyboard()

# Define button pins
PINS = [board.D0, board.D1, board.D2, board.D3]
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# === Macros ===
macros = Macros()
keyboard.modules.append(macros)

# === Encoder Setup ===
encoder = EncoderHandler()

# Use (A, B, Button, reverse)
encoder.pins = (
    (board.D7, board.D8, board.D9, False),
)

# Encoder actions: (CCW, CW, PRESS)
encoder.map = (
    (KC.F13, KC.PAUSE, KC.F14),
)

keyboard.modules.append(encoder)

# === Macros ===
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

# === Keymap ===
keyboard.keymap = [
    [UNDO, KC.DELETE, COPY, PASTE]
]


if __name__ == '__main__':
    keyboard.go()


