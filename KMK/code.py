import board
import bitbangio
import neopixel

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# ---------------------------------------------------------------
# PIN MAP - your fabricated PCB (XIAO RP2040)
#   W = D0, A = D1, S = D2, D = D3
#   Encoder A = D4, B = D5, switch = D6
#   OLED SDA = D7, SCL = D8 (software I2C)
#   SK6812 data = D9 (6 LEDs)
# ---------------------------------------------------------------

# ---- LEDs: all purple (edit PURPLE for another shade) ----
PURPLE = (128, 0, 128)
try:
    pixels = neopixel.NeoPixel(
        board.D9, 6, brightness=0.2, auto_write=False, pixel_order=neopixel.GRB
    )
    pixels.fill(PURPLE)
    pixels.show()
except Exception as e:
    print("LED error:", e)

# ---- OLED: static message, drawn once (needs font5x8.bin in the root) ----
try:
    import adafruit_ssd1306

    i2c = bitbangio.I2C(board.D8, board.D7)  # SCL, SDA
    oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C)
    oled.fill(0)
    oled.text("HELLO", 0, 0, 1)
    oled.text("MACROPAD", 0, 16, 1)
    oled.show()
except Exception as e:
    print("OLED error:", e)

# ---- Keys: WASD ----
keyboard.matrix = KeysScanner(
    pins=[board.D0, board.D1, board.D2, board.D3],
    value_when_pressed=False,  # switches wired from pin to GND
    pull=True,
)
keyboard.keymap = [
    [KC.W, KC.A, KC.S, KC.D],
]

# ---- Media keys: REQUIRED for KC.VOLU / KC.VOLD / KC.MUTE ----
# Without this, KMK silently turns those names into "no key".
# Must come BEFORE encoder.map below.
keyboard.extensions.append(MediaKeys())

# ---- Rotary encoder (EC11) ----
encoder = EncoderHandler()
keyboard.modules.append(encoder)
# (pin_a, pin_b, pin_button, is_inverted, divisor)
#  - knob turns the wrong way for volume?  change False -> True
#  - knob reacts only on every 2nd click?  change 4 -> 2
encoder.pins = ((board.D4, board.D5, board.D6, False, 4),)
# (turn left, turn right, press)
encoder.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
]

if __name__ == "__main__":
    keyboard.go()
