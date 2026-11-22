# Hardware diagnostic for the macropad. Run it as code.py, watch the serial console.
import board
import digitalio
import time
import neopixel

# 1) LED test: fixed colors, no KMK, no animation
try:
    px = neopixel.NeoPixel(board.D9, 6, brightness=0.1, auto_write=False,
                           pixel_order=neopixel.GRB)
    cols = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
    for i, c in enumerate(cols):
        px[i] = c
    px.show()
    print("LEDs set to: RED GREEN BLUE RED GREEN BLUE (first to last)")
except Exception as e:
    print("LED error:", repr(e))

# 2) OLED bus scan on D7 (SDA) / D8 (SCL) with software I2C
try:
    import bitbangio
    i2c = bitbangio.I2C(board.D8, board.D7)  # SCL, SDA
    while not i2c.try_lock():
        pass
    print("I2C scan:", [hex(a) for a in i2c.scan()])
    i2c.unlock()
    i2c.deinit()
except Exception as e:
    print("I2C error:", repr(e))

# 3) Pin monitor: shows which pin really changes when you press a key or turn the knob
names = ["D0", "D1", "D2", "D3", "D4", "D5", "D6", "D10"]
pins = {}
for n in names:
    try:
        p = digitalio.DigitalInOut(getattr(board, n))
        p.switch_to_input(pull=digitalio.Pull.UP)
        pins[n] = p
    except Exception as e:
        print(n, "init error:", repr(e))

last = {n: p.value for n, p in pins.items()}
print("Start state (True = idle/HIGH):", last)
print("Now press W, A, S, D one at a time, then turn the knob, then press it.")

while True:
    for n, p in pins.items():
        v = p.value
        if v != last[n]:
            last[n] = v
            print(n, "HIGH (released)" if v else "LOW (pressed)")
    time.sleep(0.001)
