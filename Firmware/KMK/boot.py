"""
boot.py - runs once at power-up, before code.py

By default this disables the CIRCUITPY mass-storage drive, which
protects your firmware files from corruption if the keyboard loses
power while a file is being written (a common cause of "bricked"
boards).

To get the drive back so you can edit code.py again, hold the W key
(D0) while plugging the board in / while it powers on.
"""

import board
import digitalio
import storage

# Use the W key (D0) as the "unlock storage" button at boot.
boot_key = digitalio.DigitalInOut(board.D0)
boot_key.switch_to_input(pull=digitalio.Pull.UP)

# If the key is NOT held down at boot, disable the drive.
if boot_key.value:  # True = not pressed (pulled up, wired to GND when pressed)
    storage.disable_usb_drive()

boot_key.deinit()
