# custom 30 keys board
# github link
# Requires CircuitPython 7.0.0 to support the RP2040 MCU

import board

from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

keyboard = _KMKKeyboard()
keyboard.modules.append(Layers())

keyboard.col_pins = (
    board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10,
)
keyboard.row_pins = (board.GP11, board.GP12, board.GP13, board.GP14)
keyboard.diode_orientation = DiodeOrientation.COLUMNS


FN = KC.MO(1)
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
    # |______|______|______| Ctrl |Space |  Fn  |______|______|______|______|
    # '---------------------------------------------------------------------'
    [
        KC.Q,       KC.W,    KC.E,    KC.R,    KC.T,  KC.Y,    KC.U,      KC.I,    KC.O,    KC.P,
        KC.A,       KC.S,    KC.D,    KC.F,    KC.G,  KC.H,    KC.J,      KC.K,    KC.L, OOOOOOO,
        KC.Z,       KC.X,    KC.C,    KC.V,    KC.B,  KC.N,    KC.M,  KC.ENTER, OOOOOOO, OOOOOOO,
        OOOOOOO, OOOOOOO, OOOOOOO, KC.LCTL,  KC.SPC,    FN, OOOOOOO,   OOOOOOO, OOOOOOO, OOOOOOO
    ],
    # FN
    # .---------------------------------------------------------------------.
    # | ESC  |   7  |   8  |   9  |      |      |      |      |      | BSPC |
    # |------+------+------+------+------+------+------+------+------+------|
    # | TAB  |   4  |   5  |   6  |      |      |      |      |      |______|
    # |------+------+------+------+------+------+------+------+------+------|
    # |      |   1  |   2  |   3  |   0  |   ,  |   .  | Enter|______|______|
    # |------+------+------+------+------+------+------+------+------+------|
    # |______|______|______| Alt  |Space |  Fn  |______|______|______|______|
    # '---------------------------------------------------------------------'
    [  
        KC.GESC,   KC.N7,   KC.N8,   KC.N9,  XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.BSPC,
        KC.TAB,    KC.N4,   KC.N5,   KC.N6,  XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,  OOOOOOO,
        XXXXXXX,   KC.N1,   KC.N2,   KC.N3,    KC.N0, KC.COMM,  KC.DOT, KC.ENTER,  OOOOOOO,  OOOOOOO,
        OOOOOOO, OOOOOOO, OOOOOOO, KC.LALT,   KC.SPC,      FN, OOOOOOO,  OOOOOOO,  OOOOOOO,  OOOOOOO
    ],
]

if __name__ == '__main__':
    keyboard.go()

