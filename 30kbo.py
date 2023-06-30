# custom 30 keys board
# github link
# Requires CircuitPython 7.0.0 to support the RP2040 MCU
# rename to code.py when importing to the board
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
    board.GP2, board.GP3, board.GP4, board.GP5, board.GP10,
    board.GP11, board.GP12, board.GP13, board.GP14, board.GP15,
)
keyboard.row_pins = (board.GP6, board.GP7, board.GP8, board.GP9)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

# Additional Keys definition
FN = KC.MO(1)
FN2 = KC.MO(2)
ArLEFT = KC.TD(
    KC.LCTRL,
    FN,
    KC.LGUI,
)
ArRIGHT = KC.TD(
    KC.LSHIFT,
    FN,
    FN2,
)
#unused sequence, figure out next ver
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

#transparent keys / layer above will apply
XXXXXXX = KC.TRNS
#unused keys
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
        KC.Q,    KC.W,    KC.E,     KC.R,    KC.T,    KC.Y,    KC.U,     KC.I,      KC.O,     KC.P,
        KC.A,    KC.S,    KC.D,     KC.F,    KC.G,    KC.H,    KC.J,     KC.K,      KC.L,     OOOOOOO,
        KC.Z,    KC.X,    KC.C,     KC.V,    KC.B,    KC.N,    KC.M,     KC.ENTER,  OOOOOOO,  OOOOOOO,
        OOOOOOO, OOOOOOO, OOOOOOO,  ArLEFT,  KC.SPC,  ArRIGHT, OOOOOOO,  OOOOOOO,   OOOOOOO,  OOOOOOO
    ],
    # FN
    # .---------------------------------------------------------------------.
    # | ESC  |  1   |  2   |  3   |   [  |   ]  |   \  |  -   |   =  | BSPC |
    # |------+------+------+------+------+------+------+------+------+------|
    # |  TAB |  4   |  5   |  6   |      |      |   ;  |   '  | DEL  |______|
    # |------+------+------+------+------+------+------+------+------+------|
    # |  CTL |  7   |  8   |  9   |  0   |   ,  |   .  |  /   |______|______|
    # |------+------+------+------+------+------+------+------+------+------|
    # |______|______|______|ALEFT | Alt  |ARGHT |______|______|______|______|
    # '---------------------------------------------------------------------'
    [
        KC.GESC,  KC.N1,    KC.N2,     KC.N3,    KC.LBRACKET,  KC.RBRACKET,  KC.BSLASH,  KC.MINUS,  KC.EQUAL,  KC.BSPC,
        KC.TAB,   KC.N4,    KC.N5,     KC.N6,    XXXXXXX,      XXXXXXX,      KC.SCOLON,  KC.QUOTE,  KC.DEL,    OOOOOOO,
        KC.LCTRL, KC.N7,    KC.N8,     KC.N9,    KC.N0,        KC.COMM,      KC.DOT,     KC.SLASH,  OOOOOOO,   OOOOOOO,
        OOOOOOO,  OOOOOOO,  OOOOOOO,   XXXXXXX,  KC.LALT,      XXXXXXX,      OOOOOOO,    OOOOOOO,   OOOOOOO,   OOOOOOO
    ],
    # FN2
    # .---------------------------------------------------------------------.
    # |   F1 |  F2  |  F3  |  F4  |  F5  |  F6  |      |      |      |      |
    # |------+------+------+------+------+------+------+------+------+------|
    # |   F7 |  F8  |  F9  | F10  | F11  |  F12 |      |      |      |______|
    # |------+------+------+------+------+------+------+------+------+------|
    # |XXXXXXX|     |      |      |      |   ,  |  .   |Enter |______|______|
    # |------+------+------+------+------+------+------+------+------+------|
    # |______|______|______|ALEFT |      |ARIGHT|______|______|______|______|
    # '---------------------------------------------------------------------'
    [        
        KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    XXXXXXX,  KC.UP,     XXXXXXX,  XXXXXXX,
        KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,   KC.LEFT,  KC.DOWN,   KC.RGHT,  OOOOOOO,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.ENTER,  OOOOOOO,  OOOOOOO,
        OOOOOOO,  OOOOOOO,  OOOOOOO,  XXXXXXX,  XXXXXXX,  XXXXXXX,  OOOOOOO,  OOOOOOO,   OOOOOOO,  OOOOOOO
    ],
]

if __name__ == '__main__':
    keyboard.go()



