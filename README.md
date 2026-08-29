# Nouveau-Pad ⚡

A 4-key macropad + rotary encoder + OLED + 6x addressable RGB, built on a Seeed XIAO RP2040. Submitted to Hack Club's **Hackpad** You Ship, We Ship program.

<img width="1068" height="769" alt="image" src="https://github.com/user-attachments/assets/359d5414-1abe-48ef-8677-294710a19af4" />


> Repo: [github.com/iloveadrenaline/Nouveau-Pad](https://github.com/iloveadrenaline/Nouveau-Pad)

---

## Overview

**Nouveau Pad** is a compact macropad designed around the Seeed XIAO RP2040. It combines  4 mechanical keys, a rotary encoder with push function, a 0.91" 128×32 I2C OLED, and a 6-LED SK6812 MINI addressable RGB strip and can be very usefull >:)

## Features

- **4x** mechanical switches (hot-swappable footprint, `SW_Push`)
- **1x** rotary encoder w/ push switch (EC11-style, `RotaryEncoder_Switch_MP`) 
- **1x** 0.91" 128×32 I2C OLED display (`SSD1306`-class)
- **6x** SK6812 MINI addressable RGB LEDs
- **Seeed XIAO RP2040** microcontroller 
- 2-layer PCB, single USB-C connector, multi-part 3D-printed enclosure (black color scheme with a viewing window)

## Hardware Specs (Hackpad compliance)

| Requirement | Limit |
|---|---|
| Microcontroller | Seeed XIAO RP2040 (THT) | 
| PCB size | ≤ 100 × 100 mm |
| PCB layers | 2 layers |
| Total inputs | ≤ 16 | 
| Encoders | ≤ 2 |
| OLED | ≤ 1 |
| LEDs | ≤ 16 | 
| Case | 3D printed only |

## PCB Schematics
 <img width="1229" height="842" alt="PCBV333" src="https://github.com/user-attachments/assets/25c86581-de1b-4869-8d85-eb1fb19ad5aa" /> 
 <img width="1049" height="810" alt="SCHEMATICS" src="https://github.com/user-attachments/assets/5dff3d8b-6fed-48a2-8cf9-0e022569f28f" />
 

## Bill of Materials (BOM)


1x Seeed XIAO RP2040
1x 0.91 inch OLED display
4x MX-Style switches
1x EC11 Rotary encoder
6x SK6812 MINI-E LEDs
4x white blank DSA keycaps
4x M3 heatset inserts
4x M3 screws

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
- The KMK software was made with minimal use with Antrophic Claude
