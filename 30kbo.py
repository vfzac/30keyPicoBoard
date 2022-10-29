# custom 30 keys board
# github link
# Requires CircuitPython 7.0.0 to support the RP2040 MCU

import board

from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
from kmk.modules.tapdance import TapDance
from kmk.handlers.sequences import simple_key_sequence



keyboard = _KMKKeyboard()
tapdance = TapDance()
keyboard.modules.append(Layers())
keyboard.modules.append(tapdance)

keyboard.col_pins = (
    board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10,
)
keyboard.row_pins = (board.GP11, board.GP12, board.GP13, board.GP14)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

# Additional Keys definition
FN = KC.MO(1)
FN2 = KC.MO(2)
ALEFT = KC.TD(
    KC.LCTRL,
    FN,
    FN2,
)
ARIGHT = KC.TD(
    FN,
    KC.LSHIFT,
    FN2,
)
ALTTAB = simple_key_sequence(
    (
        KC.LALT(no_release=True), 
        KC.MACRO_SLEEP_MS(30),
        KC.TAB,
        KC.MACRO_SLEEP_MS(30),
        KC.LALT(no_press=True),
    )
)
# CTLTAB = simple_key_sequence(
#     (
#         KC.LCTL(no_release=True), 
#         KC.MACRO_SLEEP_MS(30),
#         KC.TAB,
#         KC.MACRO_SLEEP_MS(30),
#         KC.LCTL(no_press=True),
#     )
# )

XXXXXXX = KC.TRNS
OOOOOOO = KC.NO

keyboard.keymap = [
    # Qwerty
    # .---------------------------------------------------------------------.
    # |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  |
    # |------+------+------+------+------+------+------+------+------+------|
    # |   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  |______|
    # |------+------+------+------+------+------+------+------+------+------|
    # |   Z  |   X  |   C  |   V  |   B  |   N  |   M  | Enter|______|______|
    # |------+------+------+------+------+------+------+------+------+------|
    # |______|______|______|ALEFT |Space |ARIGHT|______|______|______|______|
    # '---------------------------------------------------------------------'
    [
        KC.Q,       KC.W,    KC.E,    KC.R,    KC.T,  KC.Y,    KC.U,      KC.I,    KC.O,    KC.P,
        KC.A,       KC.S,    KC.D,    KC.F,    KC.G,  KC.H,    KC.J,      KC.K,    KC.L, OOOOOOO,
        KC.Z,       KC.X,    KC.C,    KC.V,    KC.B,  KC.N,    KC.M,  KC.ENTER, OOOOOOO, OOOOOOO,
        OOOOOOO, OOOOOOO, OOOOOOO,   ALEFT,  KC.SPC,  ARIGHT, OOOOOOO,   OOOOOOO, OOOOOOO, OOOOOOO
    ],
    # FN
    # .---------------------------------------------------------------------.
    # | ESC  |     |     |     |      |      |      |      |      | BSPC |
    # |------+------+------+------+------+------+------+------+------+------|
    # |ALTTAB|     |     |     |      |      |      |      |      |______|
    # |------+------+------+------+------+------+------+------+------+------|
    # |CTLTAB|     |     |     |      |   ,  |   .  | Enter|______|______|
    # |------+------+------+------+------+------+------+------+------+------|
    # |______|______|______|ALEFT |Space |ARIGHT|______|______|______|______|
    # '---------------------------------------------------------------------'
    [  
        KC.GESC,    KC.N7,     KC.N8,     KC.N9,  XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.BSPC,
        ALTTAB,   XXXXXXX,   XXXXXXX,   XXXXXXX,    XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,  OOOOOOO,
        CTLTAB,   XXXXXXX,   XXXXXXX,   XXXXXXX,    XXXXXXX, KC.COMM,  KC.DOT, KC.ENTER,  OOOOOOO,  OOOOOOO,
        OOOOOOO, OOOOOOO, OOOOOOO, XXXXXXX,   KC.SPC, XXXXXXX, OOOOOOO,  OOOOOOO,  OOOOOOO,  OOOOOOO
    ],
    # FN2
    # .---------------------------------------------------------------------.
    # |   1   |   2  |   3  |   4  |  5   |  6   |  7   |  8   |  9   |  0  |
    # |------+------+------+------+------+------+------+------+------+------|
    # |XXXXXXX|      |      |      |      |      |      |      |      |_____|
    # |------+------+------+------+------+------+------+------+------+------|
    # |XXXXXXX|      |      |      |      |   ,  |   .  | Enter|______|_____|
    # |------+------+------+------+------+------+------+------+------+------|
    # |______ |______|______|ALEFT |Space |ARIGHT|______|______|______|_____|
    # '---------------------------------------------------------------------'
    [  
        KC.N1,      KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,     KC.N8,    KC.N9,    KC.N0,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,   XXXXXXX,  XXXXXXX,  OOOOOOO,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.COMM,   KC.DOT,  KC.ENTER,  OOOOOOO,  OOOOOOO,
        OOOOOOO,  OOOOOOO,  OOOOOOO,  XXXXXXX,   KC.SPC,  XXXXXXX,  OOOOOOO,   OOOOOOO,  OOOOOOO,  OOOOOOO
    ],
]

if __name__ == '__main__':
    keyboard.go()



