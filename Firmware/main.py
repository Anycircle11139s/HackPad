import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

# Initializing the keyboard
keyboard = KMKKeyboard()
media_keys = MediaKeys()
keyboard.extensions.append(media_keys)

# 1. ENCODER SETUP 
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D26, board.D27, board.D28, False),)

# 2. KEY MATRIX SETUP (8 Keys)
keyboard.col_pins = (board.D1, board.D2, board.D4, board.D3) 
keyboard.row_pins = (board.D29, board.D0) # D0/D29 used as row strobes
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 3. KEYMAP
# Esc, Tab, Space, Backspace, F13-F16
# Encoder: Volume Up/Down, Click for Mute
keyboard.keymap = [
    [
        KC.ESC,  KC.TAB,  KC.SPC,  KC.BSPC,
        KC.F13,  KC.F14,  KC.F15,  KC.F16
    ]
]

# Encoder mapping: 
encoder_handler.map = [ ((KC.VOLU, KC.VOLD, KC.MUTE),), ]

if __name__ == '__main__':
    keyboard.go()
