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
keyboard.diode_orientation = DiodeOrientation.COL2ROW

FN = KC.MO(1)
XXXXXXX = KC.TRNS

keyboard.keymap = [
    # Qwerty
    # .---------------------------------------------------------------------.
    # |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  |
    # |------+------+------+------+------+------+------+------+------+------|
    # |   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  |XXXXXX|
    # |------+------+------+------+------+------+------+------+------+------|
    # |   Z  |   X  |   C  |   V  |   B  |   N  |   M  |   ,  |XXXXXX|XXXXXX|
    # |------+------+------+------+------+------+------+------+------+------|
    # |XXXXXX|XXXXXX|XXXXXX| Alt  |Space | Alt  |XXXXXX|XXXXXX|XXXXXX|XXXXXX|
    # '---------------------------------------------------------------------'
    [
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,   KC.Y,    KC.U,    KC.I,    KC.O,       KC.P,
        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,   KC.H,    KC.J,    KC.K,    KC.L,    XXXXXXX,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,   KC.N,    KC.M,    XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, KC.LALT, KC.SPC, FN,    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX
    ],
    # Alt
    # ,-------------------------------------------------------------------------------------------------.
    # |   `  |  F1  |  F2  |  F3  |  F4  |  F5  |  F6  |  F7  |  F8  |  F9  | F10  | F11  | F12  | Del  |
    # |------+------+------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |  UP  |      |      |      |      |      | Insrt| Home | PgUp |      |      |      |
    # |------+------+------+------+------+-------------+------+------+------+------+------+------+------|
    # |      | LEFT | DOWN | RIGHT|      |      |      |      | Del  | End  | PgDn |      |      |      |
    # |------+------+------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      |      |      |      | MUTE | VOLD | VOLU |      |      |      |      |
    # |------+------+------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |      |      |      | App  | Fn   |      |      |
    # `------------------------------------------------------------------------------------------+------'
    [
        KC.GESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQUAL, KC.BSPC,
        KC.TAB,   KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,   KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC,  KC.BSLASH,
        KC.CAPS,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,   KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, XXXXXXX,  KC.ENTER,
        KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,   KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, XXXXXXX, XXXXXXX,  KC.RSFT,
        KC.LCTRL, KC.LGUI, KC.LALT, XXXXXXX, XXXXXXX, KC.SPC, XXXXXXX, XXXXXXX, XXXXXXX, KC.RALT, KC.RGUI, FN,      XXXXXXX,  KC.RCTRL
        
        KC.GRV,  KC.F1,   KC.F2,   KC.F3,    KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,   KC.F12,  KC.DEL,
        XXXXXXX, XXXXXXX, KC.UP,   XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.INS,  KC.HOME, KC.PGUP, XXXXXXX,  XXXXXXX, XXXXXXX,
        XXXXXXX, KC.LEFT, KC.DOWN, KC.RIGHT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.DEL,  KC.END,  KC.PGDN, XXXXXXX,  XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, KC.MUTE, KC.VOLD, KC.VOLU, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.APP,  XXXXXXX,  XXXXXXX, XXXXXXX,
    ],
]

if __name__ == '__main__':
    keyboard.go()