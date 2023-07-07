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
from kmk.modules.encoder import EncoderHandler



encoder_handler = EncoderHandler()
keyboard = _KMKKeyboard()
tapdance = TapDance()
holdtap = HoldTap()
layers = Layers()
keyboard.modules = [layers, tapdance, holdtap, encoder_handler]
# tapdance.tap_time = 300 # optional: set a custom tap timeout in ms :: default 300ms
# holdtap.tap_time = 700 # optional: set a custom hold tap timeout in ms 

keyboard.col_pins = (
    board.GP2, board.GP3, board.GP4, board.GP5, board.GP10,
    board.GP11, board.GP12, board.GP13, board.GP14, board.GP15,)
keyboard.row_pins = (board.GP6, board.GP7, board.GP8, board.GP9)

keyboard.diode_orientation = DiodeOrientation.COLUMNS

encoder_handler.pins = (
    # regular direction encoder and a button
    (board.GP17, board.GP15, None,), # encoder #1 
    #(board.GP17, board.GP15, None,), # encoder #2 template
    )

# Additional Keys definition
# FN = KC.MO(1) #layer 2 of 3
# FN2 = KC.MO(2) #layer 3 of 3
CTRLSHFT = KC.LCTL(KC.LSHIFT)
CTRLALT = KC.LCTL(KC.LALT)
XXXXXXX = KC.TRNS #transparent keys / layer above will apply
OOOOOOO = KC.NO #unused keys


encoder_handler.map = [ 
    (( KC.VOLD, KC.VOLU, KC.MUTE),), # Layer 1
    #(( KC.VOLD, KC.VOLU, KC.MUTE),( KC.VOLD, KC.VOLU, KC.MUTE),), # Layer with 2 encoder template
]   #inner parenthesis is for encoder(s), outer is for layers(same with normal keys)

#tap dance defn - tapping multiple times have different keys
FNLEFT = KC.TD( 
    KC.LCTRL,
    KC.LGUI, 
    CTRLSHFT,
    CTRLALT,
)
FNRIGHT = KC.TD(
    KC.RSHIFT,
    KC.MO(1), #second layer
    KC.MO(2), #third layer
)
FNEX = KC.TD(
    KC.RSHIFT,
    KC.MO(2), #third layer
)
ENCODERCLK = KC.TD(
    KC.ENTER,)

keyboard.keymap = [
    [
        KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,
        KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,     KC.L,     ENCODERCLK,
        KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     FNEX,                                           OOOOOOO,  OOOOOOO,
        OOOOOOO,  OOOOOOO,  OOOOOOO,  FNLEFT,   KC.SPC,   OOOOOOO,  FNRIGHT,                                        OOOOOOO,  OOOOOOO,  OOOOOOO
    ],                      #the space key physically occupies 2U slots but is connected to the T key column
    [
        #normal keyboard keys ctrl alt shift arrow keys numbers or f keys
        KC.N7,    KC.N8,    KC.N9,    KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    KC.BSPC,
        KC.N4,    KC.N5,    KC.N6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,   XXXXXXX,
        KC.N1,    KC.N2,    KC.N3,    KC.N0,    XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                        OOOOOOO,  OOOOOOO,
        OOOOOOO,  OOOOOOO,  OOOOOOO,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                        OOOOOOO,  OOOOOOO,  OOOOOOO,  OOOOOOO
    ],
    [
        #etc symbols
        KC.ESC,   XXXXXXX,  KC.UP,    XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.BSLS,  KC.MINS,  KC.EQL,   XXXXXXX,
        KC.TAB,   KC.LEFT,  KC.DOWN,  KC.RGHT,  KC.SCLN,  KC.QUOT,  KC.LBRC,  KC.RBRC,  KC.BSLS,  XXXXXXX,
        KC.LCTRL, KC.LGUI,  KC.LALT,  XXXXXXX,  KC.COMM,  KC.DOT,   KC.SLSH,  XXXXXXX,                                        OOOOOOO,  OOOOOOO, # spaced out for better(?) readability
        OOOOOOO,  OOOOOOO,  OOOOOOO,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                        OOOOOOO,  OOOOOOO,  OOOOOOO,  OOOOOOO, # no key switch are connected here (yet)
    ]
]

if __name__ == '__main__':
    keyboard.go()