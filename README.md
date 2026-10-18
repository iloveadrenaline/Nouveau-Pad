# Nouveau-Pad ⚡

A 4-key  built by me  on a Seeed XIAO RP2040. Submitted to Hack Club's **Hackpad** You Ship, We Ship program.

<img width="1068" height="769" alt="image" src="https://github.com/user-attachments/assets/359d5414-1abe-48ef-8677-294710a19af4" />



---

## Overview

**Nouveau Pad** is a compact macropad designed around the Seeed XIAO RP2040. It has 4 keys that are programmable into whatever you like , I made this project so I can change my volume with the encoder because I'm tired to go into Windows Control Panel thing , Linux is better btw. Overall , I hope you like the project
**Project link** : https://stardance.hackclub.com/projects/39690

## Features

-4 Mechanical Switches
-0.91 inch oled screen for displaying cool stuff
-An encoder to change the volume because why not
-A window so you can see the pcb because it looks cool




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


## Firmware
The firmware is made in CircuitPython that's all I can tell you , I'm very begginer to this so you can just Google it . Psst I recommend Claude 


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
│   ├── README.md
│   └── KMK/
│
└── production/
    ├──KMK
    ├──Case_Bottom.stl
    ├──Case_Top.stl
    ├──Gerbers.zip
    └──Knob.stl

```

## Assembly

1. Order PCB  via JLCPCB or PCBWay using the Gerber
2. Solder U1 (XIAO RP2040), U2 (OLED), SW1–SW5, and D1–D6 in that order (MCU → display → switches → LEDs).
3. Flash firmware from `firmware/KMK/` onto the controller
4. 3D print the case parts
5. Heat-set M3 inserts, assemble top/bottom with screws, snap in keycaps.

## License

This project is released under the MIT License -- see in the repo

## Credits

- Built for [Hack Club's Hackpad](https://hackpad.hackclub.com) YSWS program
- MX switch / XIAO / SK6812 footprints from the Hackpad KiCad starter library
- Designed by [iloveadrenaline](https://github.com/iloveadrenaline)
- The KMK software was made with minimal use of Antrophic Claude
  Peace out
- Honorable mention to [Tensor](https://github.com/TensorSwe) , he guided me and made this project a reality
