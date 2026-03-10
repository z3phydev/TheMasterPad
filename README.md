# TheMasterPad
## What is this thing?
Well it is USB Hub that has 5 USB A ports and a USB C port... **But** it has 8 MX switches which are Programable Buttons aswell as a Rotary Encoder all of which are powered by a Seeed XIAO RP2040

## How to use
1) Assemble
2) Flash CircutPython to the Pico (or QMK, if you do skip step 3 and 4, and if you are flashing QMK you know what you are doing anyway)
3) Download the adafruit hid lib and put it into the lib folder
4) Upload the code (which you can edit to your liking)
5) Enjoy
## Why did I make it?
I made this project because to my knowledge it hasn't been made. Even though it hasn't I still think its a good combo. It is also an intrusive thought after looking at keyboards.
## Repo Guide
- In the Folder 3D you will find the step and wrl (Kicad 3D file) files, the step is in a zip cause github said its to big and the keycaps wouldn't export so thats in ther aswell :)
- In the Kicad Folder you will find the PCB and Schematic files awell as a sub-folder containing custom footprints
- In the Firmware folder you'll find the code
- In the Production Folder you will find 3 files needed for JLC, gerbers, A BOM and Pick and Place file for assembly
- BOM.csv is the whole project cost basically. It also contains all the parts for building

## 3D Model

<img width="1600" height="960" alt="TheMasterPadISO" src="https://github.com/user-attachments/assets/5ee1e653-0565-4fff-b36d-298c48c02341" />

<img width="1080" height="1080" alt="TheMasterPadPLAN" src="https://github.com/user-attachments/assets/211fa44a-bcff-4204-954c-4079781cec95" />

## PCB

<img width="700" height="700" alt="Screenshot 2026-02-24 191859" src="https://github.com/user-attachments/assets/0f612aa4-415f-43d0-aeb1-29d5dcd22fff" />

## Schematic

![image (7)](https://github.com/user-attachments/assets/60b537a7-fc7e-48d3-8906-f5970ee66af4)

## BOM

|Reference(s)|Qty            |Value/Description             |MFR         |MFR No.           |Unit Price GBP|Total Price GBP|Link                                                                                    |FIELD9             |FIELD10               |FIELD11        |
|------------|---------------|------------------------------|------------|------------------|--------------|---------------|----------------------------------------------------------------------------------------|-------------------|----------------------|---------------|
|~           |5 (2 assebeled)|PCB and Partial assebly       |JLCPCB      |~                 |~             |19.78          |https://jlcpcb.com/                                                                     |                   |                      |               |
|U3          |1              |Seeed XIAO RP2040 with Headers|Raspberry Pi|102010428         |4.8           |4.8            |https://thepihut.com/products/seeed-xiao-rp2040                                         |                   |                      |               |
|SW2-9       |8              |Cherry Mx Brown Swtich        |CHERRY      |MX1A-G1NW         |0.48          |4.32           |https://www.keyboardco.com/product/cherry-key-switch-module-brown-tactile-pcb-mount.asp |                   |                      |               |
|SW1         |1              |Rotary Encoder                |Bourns      |PEC11R-4325F-S0012|1.87          |1.87           |https://uk.rs-online.com/web/p/mechanical-rotary-encoders/7377767                       |                   |                      |               |
|~           |8              |Keycaps In Various Colours    |JYTECH      |JYT--1657         |0.15          |1.2            |https://www.alibaba.com/product-detail/Multi-color-XDA-Blank-Keycap-1_1601173995121.html|                   |                      |               |
|J2-6        |5              |USB A Port                    |Molex       |67643-2911        |1.78          |8.87           |https://uk.rs-online.com/web/p/usb-connectors/9048200                                   |                   |                      |               |
|            |               |                              |            |                  |              |               |                                                                                        |                   |                      |               |
|            |               |                              |            |                  |              |               |                                                                                        |                   |Total Price USD approx|Total Price GBP|
|            |               |                              |            |                  |              |               |                                                                                        |Items              |54.91                 |40.84          |
|            |               |                              |            |                  |              |               |                                                                                        |Shipping (and fees)|30.92                 |23             |
|            |               |                              |            |                  |              |               |                                                                                        |Final              |85.82                 |63.84          |
