"""
KMK firmware for XIAO-based macropad (4 keys arranged in a WASD layout,
freely programmable -- see the EDIT THIS SECTION block below)
- 4 keys on D0-D3, direct wired to GND
- Rotary encoder (A=D4, B=D5, push=D6)
- SSD1306 0.91" OLED on software I2C (SDA=D8, SCL=D9)
- 6x SK6812MINI RGB LEDs on D10
"""

import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.rgb import RGB, AnimationModes

keyboard = KMKKeyboard()

# ---------------------------------------------------------------------------
# KEYS (direct pins, no matrix/diodes needed)
# 4 face buttons + the encoder's push-button, all wired to GND.
# ---------------------------------------------------------------------------
keyboard.row_pins = None
keyboard.col_pins = None
keyboard.direct_pins = (
    (board.D0, board.D1, board.D2, board.D3, board.D6),
)

# ---------------------------------------------------------------------------
# EDIT THIS SECTION to program each key.
# Physical order below matches the wiring order: SW1, SW2, SW3, SW4, then
# the encoder push-button.
#
# Every key can be:
#   - a normal keystroke, e.g. KC.A, KC.F5, KC.ESC
#   - a shortcut combo, e.g. KC.LCTRL(KC.C) for Ctrl+C
#   - a layer key, e.g. KC.MO(1) to hold for layer 1
#   - a macro (see the Macro example further down, commented out)
#
# Full list of available keycodes:
# https://kmkfw.io/docs/keycodes
# ---------------------------------------------------------------------------
SW1 = KC.LCTRL(KC.C)   # example: Copy
SW2 = KC.LCTRL(KC.V)   # example: Paste
SW3 = KC.LCTRL(KC.Z)   # example: Undo
SW4 = KC.LCTRL(KC.S)   # example: Save
ENCODER_PUSH = KC.MUTE

keyboard.keymap = [
    [SW1, SW2, SW3, SW4, ENCODER_PUSH]
]

# --- Optional: multi-step macros -------------------------------------------
# Uncomment and adapt to send a sequence of keys/text from one button:
#
# from kmk.modules.macros import Press, Release, Tap
# from kmk.macros import KMKMacro
# my_macro = KMKMacro([Tap(KC.H), Tap(KC.I)])   # types "hi"
# SW1 = my_macro
# (also add: from kmk.modules.macros import Macros; keyboard.modules.append(Macros()))

# ---------------------------------------------------------------------------
# ROTARY ENCODER (rotation only -- the push-button is handled above)
# ---------------------------------------------------------------------------
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.D4, board.D5, None, False),  # (pin_a, pin_b, button_pin, is_inverted)
)
# Per-layer encoder actions: (turn CCW, turn CW)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),
]
keyboard.modules.append(encoder_handler)

# ---------------------------------------------------------------------------
# RGB (6x SK6812MINI on D10)
# ---------------------------------------------------------------------------
rgb = RGB(
    pixel_pin=board.D10,
    num_pixels=6,
    val_limit=100,
    hue_default=0,
    sat_default=255,
    rgb_order=(1, 0, 2),  # GRB order -- change to (0,1,2) if colors look wrong
    animation_mode=AnimationModes.STATIC,
)
keyboard.modules.append(rgb)

# ---------------------------------------------------------------------------
# OLED DISPLAY (SSD1306 0.91" 128x32, software I2C on D8/D9)
# ---------------------------------------------------------------------------
try:
    import displayio
    import adafruit_displayio_ssd1306
    from kmk.modules.display import Display, TextEntry
    from kmk.modules.display.ssd1306 import SSD1306  # noqa: F401

    displayio.release_displays()
    i2c = busio.I2C(scl=board.D9, sda=board.D8)  # SCL, SDA per schematic
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
    display_driver = adafruit_displayio_ssd1306.SSD1306(
        display_bus, width=128, height=32
    )

    display = Display(
        display=display_driver,
        entries=[
            TextEntry(text="WASD Pad", x=0, y=8),
            TextEntry(text="Ready", x=0, y=24),
        ],
    )
    keyboard.modules.append(display)
except ImportError:
    # Display libraries not installed / OLED not wired -- keyboard still works.
    pass

if __name__ == '__main__':
    keyboard.go()
