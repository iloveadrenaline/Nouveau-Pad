# Nouveau-Pad ⚡

A 4-key macropad + rotary encoder + OLED + 6x addressable RGB, built on a Seeed XIAO RP2040. Submitted to Hack Club's **Hackpad** You Ship, We Ship program.

![Nouveau-Pad 3D render](assets/render.png)

> Repo: [github.com/iloveadrenaline/Nouveau-Pad](https://github.com/iloveadrenaline/Nouveau-Pad)

---

## Overview

**nouveauXpad** is a compact hackpad-class macropad designed around the Seeed XIAO RP2040. It combines 4 mechanical keys, a rotary encoder with push function, a 0.91" 128×32 I2C OLED for status/layer display, and a 6-LED SK6812 MINI addressable RGB strip for backlighting/feedback — all on a single 2-layer PCB inside the Hackpad size and component limits.

## Features

- **4x** mechanical switches (hot-swappable footprint, `SW_Push`), individually wired to GPIO
- **1x** rotary encoder w/ push switch (EC11-style, `RotaryEncoder_Switch_MP`) — great for volume/scroll/zoom
- **1x** 0.91" 128×32 I2C OLED display (`SSD1306`-class) for layer/status feedback
- **6x** SK6812 MINI addressable RGB LEDs, daisy-chained off a single data pin
- **Seeed XIAO RP2040** microcontroller (through-hole mount, per Hackpad spec)
- 2-layer PCB, single USB-C connector, multi-part 3D-printed enclosure (black/red color scheme with a viewing window)

## Hardware Specs (Hackpad compliance)

| Requirement | Limit | Nouveau-Pad |
|---|---|---|
| Microcontroller | Seeed XIAO RP2040 (THT) | ✅ XIAO RP2040 |
| PCB size | ≤ 100 × 100 mm | ✅ 100 × 70 mm |
| PCB layers | 2 layers | ✅ 2 layers |
| Total inputs | ≤ 16 | ✅ 6 (4 switches + encoder + encoder-push) |
| Encoders | ≤ 2 | ✅ 1 |
| OLED | ≤ 1 | ✅ 1 |
| LEDs | ≤ 16 | ✅ 6 |
| Case | 3D printed only | ✅ multi-part, black/red, viewing window |

## Images

| PCB Layout | 3D Render | Schematic |
|---|---|---|
| ![PCB](assets/pcb.png) | ![Render](assets/render-top.png) | ![Schematic](assets/schematic.png) |

## Bill of Materials (BOM)

| Ref | Part | Qty | Notes |
|---|---|---|---|
| U1 | Seeed XIAO RP2040 | 1 | Main MCU, through-hole mount |
| U2 | 0.91" 128×32 I2C OLED (SSD1306-class) | 1 | Layer/status display |
| SW1–SW4 | Mechanical switch (`SW_Push`, MX-style) | 4 | Hot-swap or direct solder |
| SW5 | Rotary encoder w/ push (EC11-style) | 1 | A/B quadrature + switch |
| D1–D6 | SK6812 MINI-E addressable RGB LED | 6 | Daisy-chained, single data line |
| — | M3 heatset inserts | 4+ | Case assembly |
| — | M3 screws | 4+ | Case assembly |
| — | USB-C cable | 1 | Power + data |
| — | Keycaps (DSA/XDA) | 4 | From Hackpad kit |

## Pinout

| XIAO RP2040 Pin | Function | Connected To |
|---|---|---|
| D0 / A0 | GPIO | SW1 |
| D1 / A1 | GPIO | SW2 |
| D2 / A2 | GPIO | SW3 |
| D3 / A3 | GPIO | SW4 |
| D4 / A4 (SDA) | I2C SDA | Encoder A / OLED SDA |
| D5 / A5 (SCL) | I2C SCL | Encoder B / OLED SCL |
| D6 (TX) | GPIO | Encoder push (S1) |
| D10 (MOSI) | GPIO | RGB chain DIN (D1→D6) |
| 3V3 | Power | OLED VCC, LED VDD |
| GND | Ground | Common ground |

*(Cross-check against `pcb/nouveaupad.kicad_sch` before flashing — SDA/SCL are shared between the OLED and the encoder per the schematic.)*

## Firmware

Firmware targets **KMK** (CircuitPython-based, runs natively on the XIAO RP2040) — QMK/other pre-existing firmware is also Hackpad-approved if preferred.

Planned firmware behavior:
- 4 keys mapped to a configurable macro layer
- Rotary encoder defaults to volume up/down, push = mute (remappable per layer)
- OLED shows the active layer name
- RGB chain reacts to key presses / layer changes

> Firmware source lives in `firmware/` — see that folder's README for flashing instructions.

## Repository Structure

```
Nouveau-Pad/
├── README.md
├── LICENSE
├── assets/
│   ├── render.png
│   ├── render-top.png
│   ├── pcb.png
│   └── schematic.png
├── cad/
│   ├── nouveaupad.step        # full assembly
│   └── nouveaupad.stl
├── pcb/
│   ├── nouveaupad.kicad_pro
│   ├── nouveaupad.kicad_sch
│   ├── nouveaupad.kicad_pcb
│   └── gerbers/
└── firmware/
    ├── README.md
    └── KMK/
```

## Assembly

1. Order PCB (2-layer) via JLCPCB using the Gerbers in `pcb/gerbers/`.
2. Solder U1 (XIAO RP2040), U2 (OLED), SW1–SW5, and D1–D6 in that order (MCU → display → switches → LEDs).
3. Flash firmware from `firmware/KMK/` onto the XIAO RP2040.
4. 3D print the case parts from `cad/` (black bottom tray + red top plate w/ viewing window).
5. Heat-set M3 inserts, assemble top/bottom with screws, snap in keycaps.

## License

This project is released under the MIT License — see [LICENSE](LICENSE).

## Credits

- Built for [Hack Club's Hackpad](https://hackpad.hackclub.com) YSWS program
- MX switch / XIAO / SK6812 footprints from the Hackpad KiCad starter library
- Designed by [iloveadrenaline](https://github.com/iloveadrenaline)
