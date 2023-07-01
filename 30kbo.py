# custom 30 keys board
# github link
# Requires CircuitPython 7.0.0 to support the RP2040 MCU
# rename to code.py when importing to the board
import board

from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.holdtap import HoldTap



keyboard = _KMKKeyboard()
tapdance = TapDance()
holdtap = HoldTap()
keyboard.modules.append(Layers())
keyboard.modules.append(tapdance)
keyboard.modules.append(holdtap)
tapdance.tap_time = 300 # optional: set a custom tap timeout in ms
holdtap.tap_time = 700 # optional: set a custom hold tap timeout in ms

keyboard.col_pins = (
    board.GP2, board.GP3, board.GP4, board.GP5, board.GP10,
    board.GP11, board.GP12, board.GP13, board.GP14, board.GP15,)
keyboard.row_pins = (board.GP6, board.GP7, board.GP8, board.GP9)

keyboard.diode_orientation = DiodeOrientation.COLUMNS

# Additional Keys definition
FN = KC.MO(1) #layer 2 of 3
FN2 = KC.MO(2) #layer 3 of 3
CTRLSHFT = KC.LCTL(KC.LSFT)
XXXXXXX = KC.TRNS #transparent keys / layer above will apply
OOOOOOO = KC.NO #unused keys

#tap dance defn - tapping multiple times have different keys
ARLEFT = KC.TD( 
    KC.LCTRL,
    KC.LSFT,
    KC.TAB,
    KC.LGUI,
    KC.ESC,
    CTRLSHFT,
)
ARRIGHT = KC.TD(
    KC.LSHIFT,
    FN,
    FN2,
)
ENCODERCLK = KC.TD(
    KC.ENTER,)

keyboard.keymap = [
    [
        KC.Q,    KC.W,    KC.E,     KC.R,    KC.T,    KC.Y,    KC.U,     KC.I,      KC.O,     KC.P,
        KC.A,    KC.S,    KC.D,     KC.F,    KC.G,    KC.H,    KC.J,     KC.K,      KC.L,     ENCODERCLK,
        KC.Z,    KC.X,    KC.C,     KC.V,    KC.B,    KC.N,    KC.M,     OOOOOOO,   OOOOOOO,  OOOOOOO,
        OOOOOOO, OOOOOOO, OOOOOOO,  ARLEFT,  KC.SPC,  ARRIGHT, OOOOOOO,  OOOOOOO,   OOOOOOO,  OOOOOOO
    ],
    [
        #normal keyboard keys ctrl alt shift arrow keys numbers or f keys
    ],
]

if __name__ == '__main__':
    keyboard.go()