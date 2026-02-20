.. START:section:0:0
What is the RB-RA8D1 Board?
===========================

.. END:section:0:0

.. START:main_content:0:0
The RB-RA8D1 is a powerful development board, Designed for building smart electronics projects. At its core is the RA8D1 microcontroller, a fast chip (480 MHz) with built-in features like LVGL library for LCD interface, internet connectivity, and memory for smooth operation.

.. END:main_content:0:0

**Key Features:**

- **Processor:** Arm Cortex-M85 with 2MB Flash and 1MB SRAM
- **Connectivity:** USB, Ethernet, Wi-Fi/Bluetooth support, and expansion ports
- **Peripherals:** LEDs, buttons, touchscreen LCD, camera, and sensors
- **Power:** USB-powered with efficient regulators
- **Expansion:** Add-on boards for graphics and imaging


.. START:section:0:1
Hardware Architecture and Default Configuration
===============================================

.. END:section:0:1

.. START:main_content:0:1
This section dives into the RB-RA8D1's hardware setup – like the blueprint of the board. It covers the brain (MCU), power system, pins, and default settings. Understanding this helps you customize projects.

.. END:main_content:0:1

MCU Overview
------------

The RA8D1 microcontroller is the board's core.

**Features:**

- Arm Cortex-M85
- 480 MHz
- 2MB Flash
- 1MB SRAM
- TrustZone security

**Architecture:**

- 32-bit processor
- Peripherals: USB, Ethernet, SDRAM

**Why Important:** Handles all tasks. Defaults to efficient mode.

Power Supply Architecture
-------------------------

How the board gets and manages power

.. START:table:0:1:3

.. csv-table:: **MCU Specifications**
   :header: "Spec", "Value"
   :widths: 20, 30
   :align: center

   "Core", "Cortex-M85"
   "Speed", "480 MHz"
   "Memory", "2MB Flash, 1MB SRAM"

.. END:table:0:1:3

**Setup:** 5V input via USB. Regulators for 3.3V, 1.8V, 1.2V.

**Defaults:** Auto-on with USB. Supports low-power modes.

**Why Important:** Ensures stable operation of the board and peripherals.

.. START:table:0:1:5

.. csv-table:: Power Supply Rails
   :header: "Rail", "Voltage", "Source"
   :widths: 20, 20, 30
   :align: center

   "Main", "3.3V", "USB 5V"
   "Core", "1.2V", "Regulator"
   "I/O", "1.8V", "Regulator"

.. END:table:0:1:5

Default Pin Configurations
--------------------------

How pins are set up out of the box.

**Defaults:** GPIO for I/O. Pull-ups for stability.

**Examples:** LEDs on P200. Buttons on P200.

**Why Important:** Ready for basic use.



Clock and Reset Setup
---------------------

Timing and startup basics.

**Clocks:** 24MHz crystal for MCU.

**Reset:** Button for restarts.

**Defaults:** Stable timing on boot.

**Why Important:** Keeps everything in sync.

.. START:section:0:2
System Control and Ecosystem Access
===================================

.. END:section:0:2

.. START:main_content:0:2
This section explains the basic controls and connections on the RB-RA8D1 board that let you interact with it, power it up, and add extra gadgets. These are like the "buttons and plugs" that make the board user-friendly. We'll cover power, lights, buttons, and ways to connect sensors or modules. Everything is based on the board's pin assignments (from the pinmux sheet) for accuracy.

.. END:main_content:0:2

Power and Debug MCU and Power Select
------------------------------------

he board needs power to work, and you can choose how to supply it. It also has built-in debugging tools to help you program and test it.

**How It Works:** Plug in a USB cable for power and debugging. Switches select power modes (e.g., for different voltages). Debug port connects to your computer for uploading code or checking errors.

**Why It's Useful:** Easy to power from a USB port (like charging your phone). Debugging helps fix problems quickly

.. START:table:0:2:2

.. csv-table:: Power and Debug Assignments
   :header: "Component", "Pin Number", "Signal Name", "Description"
   :widths: 20, 20, 20, 40
   :align: center

   "Power Select", "SW1", "Various", "Switches for mode selection (e.g., SW1-3 ON for camera)"
   "Debug MCU", "J10", "USB Debug", "Micro-USB for programming and serial console"
   "Power LED", "LED4", "Power Indicator", "Lights up white when powered on"
   "Debug LED", "LED5", "Debug Indicator", "Blinks orange during programming"

.. END:table:0:2:2

User LED
--------

LEDs are little lights that show what's happening on the board.


.. START:tip:0:2:4

.. tip::

   Use the micro-USB port (J10) for both power and debug. Flip switches on SW1 for different modes (e.g., ON for camera, OFF for Ethernet).
   Table: Power and Debug Pin Assignments (From Pinmux Sheet)

.. END:tip:0:2:4

.. START:tip:0:2:5



.. END:tip:0:2:5

.. START:table:0:2:6

.. csv-table:: User LED Pin Assignments
   :header: "LED Color", "MCU Pin", "Signal", "Description"
   :widths: 20, 25, 20, 35
   :align: center

   "Blue (LED1)", "P200 (example)", "GPIO", "Blinks at 1 Hz by default"
   "Green (LED2)", "P200 (example)", "GPIO", "Stays on full brightness"
   "Red (LED3)", "P200 (example)", "GPIO", "Off by default"

.. END:table:0:2:6

.. tip::

   No extra setup needed; they're ready to use. In demos, press buttons to change their brightness or speed.
   Table: User LED Pin Assignments (From Pinmux Sheet – Controlled via MCU pins)

User Button
-----------

Buttons let you interact with the board manually.

**How It Works:** Two push buttons (**S1** and **S2**) that you press to trigger actions. Connected directly to the MCU for easy programming.

**Why It's Useful:** Useful for testing input. Example: press **S1** to change LED brightness, **S2** to change blink speed. Works like remote controls for your board.

.. START:tip:0:2:9

.. tip::

   Press gently; they're on the board's edge. In demos, they control the LEDs without needing code.

.. END:tip:0:2:9

.. START:table:0:2:10

.. csv-table:: User Button Pin Assignments
   :header: "Button", "MCU Pin", "Signal", "Description"
   :widths: 15, 25, 25, 35
   :align: center

   "S1", "P200 (example)", "GPIO Input", "Changes LED1 intensity"
   "S2", "P200 (example)", "GPIO Input", "Changes LED1 blink frequency"

.. END:table:0:2:10

Mikro Bus
---------

Mikro Bus is a standard connector for adding small modules (like sensors).


**How It Works:** A header (like a plug) where you connect "click" modules from MikroElRBtronika. Provides pins for power, data, and communication.

**Why It's Useful:** Add extra functionality easily without soldering. Example: plug in a temperature sensor or display. Works like Lego blocks for electronics.

.. START:tip:0:2:13

.. tip::

   - Align the module carefully and push it in
   - Power the board first
   - Great for rapid prototyping

.. END:tip:0:2:13

.. START:table:0:2:14

.. csv-table:: Mikro Bus Pin Assignments
   :header: "Pin", "MCU Pin", "Signal", "Description"
   :widths: 15, 25, 20, 40
   :align: center

   "VCC", "+3.3V", "Power", "Supplies 3.3V to modules"
   "GND", "GND", "Ground", "Common ground"
   "SDA", "P511", "I2C SDA", "Data line for I2C"
   "SCL", "P512", "I2C SCL", "Clock line for I2C"
   "TX", "P409", "UART TX", "Serial transmit"
   "RX", "P408", "UART RX", "Serial receive"
   "PWM", "P200", "PWM", "Pulse output for motors/LEDs"

.. END:table:0:2:14

PMOD
----

PMOD is another standard connector for add-on boards.


**How It Works:** 12-pin header for PMOD modules (from Digilent). Supports SPI, I2C, UART, and GPIO.

**Why It's Useful:** Connect displays, motors, or sensors. Similar to Mikro Bus but from a different maker.


.. START:tip:0:2:17

.. tip::

   Plug in the module and secure it. Use for RS485 or digital I/O expansions.

.. END:tip:0:2:17

.. START:table:0:2:18

.. csv-table:: PMOD Pin Assignments
   :header: "Pin", "MCU Pin", "Signal", "Description"
   :widths: 10, 20, 20, 40
   :align: center

   "1", "P300", "GPIO", "General input/output"
   "2", "P301", "GPIO", "General input/output"
   "3", "+3.3V", "Power", "3.3V supply"
   "4", "GND", "Ground", "Common ground"
   "5", "P302", "SPI MOSI", "SPI data out"
   "6", "P303", "SPI MISO", "SPI data in"
   "7", "P304", "SPI SCK", "SPI clock"
   "8", "P305", "SPI CS", "SPI chip select"

.. END:table:0:2:18

I2C
---

I2C is a simple way to connect devices like sensors or displays.

**How It Works:** Two-wire protocol: SDA (data) and SCL (clock). Used for RTC and other modules

**Why It's Useful:** Add sensors or touchscreens. Low-power and simple to use


.. START:tip:0:2:21

.. tip::

   Connect SDA and SCL pins. Supports Qwiic connectors too.

.. END:tip:0:2:21

.. START:table:0:2:22

.. csv-table:: I2C Pin Assignments
   :header: "Component", "MCU Pin", "Signal", "Description"
   :widths: 20, 20, 20, 40
   :align: center

   "I2C1 (RTC)", "P511", "SDA1", "Data line for RTC"
   "I2C1 (RTC)", "P512", "SCL1", "Clock line for RTC"
   "I2C (General)", "P511", "SDA", "Data for displays/sensors"
   "I2C (General)", "P512", "SCL", "Clock for displays/sensors"

.. END:table:0:2:22

USB
---

USB lets you connect the board to computers or devices.

**How It Works:** Supports High-Speed (HS) and Full-Speed (FS). Used for debugging, Wi-Fi, or peripherals.

**Why It's Useful:** Program the board. Add wireless or storage devices.

.. START:tip:0:2:25

.. tip::

   Use **J10** for debug and **J2** for devices. Drivers install automatically.

.. END:tip:0:2:25

.. START:table:0:2:26

.. csv-table:: USB Pin Assignments
   :header: "Component", "Pin Number", "Signal", "Description"
   :widths: 25, 20, 25, 30
   :align: center

   "USB HS", "P814", "USB_DP", "Data positive for high-speed"
   "USB HS", "P815", "USB_DM", "Data negative for high-speed"
   "USB FS", "F15", "USBHS_DM", "Data for Wi-Fi/Bluetooth"
   "USB FS", "F14", "USBHS_DP", "Data for Wi-Fi/Bluetooth"
   "USB VBUS", "P411", "VBUS", "Power for connected devices"
   "USB ID", "P407", "ID", "Identifies device type"

.. END:table:0:2:26

.. START:section:0:3
Special Feature Access
======================

.. END:section:0:3

.. START:main_content:0:3
This section covers the advanced features on the RB-RA8D1 board that make it powerful for projects like internet-connected devices or graphics displays. These are like "superpowers" for the board, letting it handle fast data, extra memory, or visuals. We'll explain each one, how to use it, and include pin details from the pinmux sheet.

.. END:main_content:0:3

Ethernet
--------

**How It Works:** Uses an RJ45 port (like your router's cable) for 10/100 Mbps speeds. It sends/receives data via RMII protocol.  

**Why It's Useful:** Access online services (e.g., weather data or currency rates). Great for IoT devices needing reliable internet without Wi-Fi.  

.. START:tip:0:3:1

.. tip::

      Plug in an Ethernet cable to **J1**. Set **SW1-5 ON** for Ethernet mode (conflicts with camera).  
   

.. END:tip:0:3:1

.. START:table:0:3:2

.. csv-table:: Ethernet Pin Assignments
   :header: "Component", "MCU Pin", "Signal", "Description"
   :widths: 25, 20, 25, 30
   :align: center

   "Ethernet TXD0", "P700", "ENET_RMII_TXD0", "Sends data out"
   "Ethernet TXD1", "P406", "ENET_RMII_TXD1", "Sends data out"
   "Ethernet RXD0", "P702", "ENET_RMII_RXD0", "Receives data in"
   "Ethernet RXD1", "P703", "ENET_RMII_RXD1", "Receives data in"
   "Ethernet MDC", "P401", "ENET_RMII_MDC", "Clock for management"
   "Ethernet MDIO", "P402", "ENET_RMII_MDIO", "Data for management"
   "Ethernet REFCLK", "P701", "ENET_RMII_REFCLK", "Reference clock"

.. END:table:0:3:2

USB High Speed
--------------

**How It Works:** Supports up to 480 Mbps via DP/DM lines. Works in host mode or for debugging.  

**Why It's Useful:** Connects high-speed gadgets like cameras or storage. Faster than regular USB.

.. START:tip:0:3:4

.. tip::

      Use **J2** for peripherals. For demos, it handles USB CDC (serial) for console.  
   

.. END:tip:0:3:4

.. START:table:0:3:5

.. csv-table:: USB High Speed Pin Assignments
   :header: "Component", "MCU Pin", "Signal", "Description"
   :widths: 25, 20, 25, 30
   :align: center

   "USB HS DP", "P814", "USB_DP", "Data positive line"
   "USB HS DM", "P815", "USB_DM", "Data negative line"
   "USB HS VBUS", "P411", "USB_VBUS", "Power for devices"
   "USB HS ID", "P407", "USB_ID", "Identifies device type"

.. END:table:0:3:5

SPI Flash
---------

**How It Works:** Serial Peripheral Interface (SPI) connects to flash memory for storing programs or settings.  

**Why It's Useful:** Holds code even when powered off. Like a tiny hard drive for the board.  


.. START:tip:0:3:7

.. tip::

      Used automatically in demos to store API keys or firmware.  
   

.. END:tip:0:3:7

.. START:table:0:3:8

.. csv-table:: SPI Flash Pin Assignments
   :header: "Component", "MCU Pin", "Signal", "Description"
   :widths: 25, 20, 25, 30
   :align: center

   "SPI Flash MOSI", "P413", "MOSIA", "Data out to flash"
   "SPI Flash MISO", "P412", "MISOA", "Data in from flash"
   "SPI Flash SCK", "P410", "RSPCKA", "Clock signal"
   "SPI Flash CS", "P414", "SSLA0", "Chip select"

.. END:table:0:3:8

.. START:note:0:3:9

.. note::

      SPI is used for external flash. Check pinmux for all mappings.
   

.. END:note:0:3:9

SDRAM
-----

**How It Works:** 32 MB of fast RAM connected via 16-bit bus.  

**Why It's Useful:** Handles video, AI, or graphics tasks smoothly.  


.. START:tip:0:3:11

.. tip::

      Built-in; no manual setup required.  
   

.. END:tip:0:3:11

.. START:table:0:3:12

.. csv-table:: SDRAM Pin Assignments
   :header: "Component", "MCU Pin", "Signal", "Description"
   :widths: 25, 20, 25, 30
   :align: center

   "SDRAM A0", "P300", "SDRAM_A0", "Address line 0"
   "SDRAM D0", "P601", "SDRAM_D0", "Data line 0"
   "SDRAM CKE", "P113", "SDRAM_CKE", "Clock enable"
   "SDRAM WE", "P114", "SDRAM_WE", "Write enable"
   "SDRAM CAS", "P908", "SDRAM_CAS", "Column address strobe"
   "SDRAM RAS", "P909", "SDRAM_RAS", "Row address strobe"
   "SDRAM CS", "P115", "SDRAM_CS", "Chip select"

.. END:table:0:3:12

.. START:note:0:3:13

.. note::

      Full SDRAM mapping is in the pinmux sheet. Only key pins shown here.
   

.. END:note:0:3:13

Graphics Expansion Port
-----------------------

**How It Works:** 40-pin header (J57) connects LCDs with RGB signals, I2C touch, and power.  

**Why It's Useful:** Adds a screen with touch for GUIs or interactive apps.  


.. START:tip:0:3:15

.. tip::

      Attach the MIPI Graphics Board with pillars.  
   

.. END:tip:0:3:15

.. START:table:0:3:16

.. csv-table:: Graphics Expansion Port Pin Assignments
   :header: "Component", "MCU Pin", "Signal", "Description"
   :widths: 25, 20, 25, 30
   :align: center

   "LCD BLEN", "P404", "DISP_BLEN", "Backlight enable"
   "LCD SDA", "P511", "I2C_SDA", "Touch data"
   "LCD SCL", "P512", "I2C_SCL", "Touch clock"
   "LCD DATA0", "P914", "LCD_DATA00", "RGB data bit 0"
   "LCD CLK", "P806", "LCD_CLK", "Pixel clock"
   "LCD RST", "PA01", "DISP_RST", "Reset signal"

.. END:table:0:3:16

.. START:section:0:4
Native Pin Access
=================

.. END:section:0:4

.. START:main_content:0:4
This section explains the "native pin access" on the RB-RA8D1 board, which means the direct connections (breakout headers) to the microcontroller's pins. These are like open plugs where you can connect wires, sensors, or circuits. It's great for advanced users who want to build custom projects. We'll cover what they are, how to use them, and pin details.


.. END:main_content:0:4

Breakout Headers Overview
-------------------------

Breakout headers are rows of pins (J51 to J56) that expose almost all MCU signals, voltages, and grounds.


**How It Works:** Each header has labeled pins for power (e.g., 3.3V), ground, and signals (e.g., GPIO for inputs/outputs).  

**Why It's Useful:** Connect breadboards or custom circuits without soldering. Like extension cords for electronics.






.. START:tip:0:4:2

.. tip::

      Use a standard breadboard. Headers are spaced for easy plugging. Refer to schematic for exact layouts.
   

.. END:tip:0:4:2

Pin Functions and Assignments
-----------------------------

Pins on the headers handle different tasks like digital I/O, analog, or communication.


**How It Works:** Pins are grouped by function (e.g., GPIO for buttons, ADC for sensors).  

**Why It's Useful:** Flexible for projects – add LEDs, motors, or sensors.




.. START:table:0:4:5

.. csv-table:: Sample Pin Assignments (J51 Example)
   :header: "Header", "Pin", "MCU Pin", "Signal", "Function"
   :widths: 10, 10, 15, 15, 20

   "J51", "1", "P400", "TXD1", "UART Transmit"
   "J51", "2", "P401", "RXD1", "UART Receive"
   "J51", "3", "P404", "CTS1", "UART Control"
   "J51", "4", "GND", "GND", "Ground"
   "J51", "5", "+3.3V", "+3.3V", "Power"

.. END:table:0:4:5

.. START:tip:0:4:6

.. tip::

      Check voltage levels (3.3V max). Use jumpers for connections.
   

.. END:tip:0:4:6

How to Use Breakout Pins
------------------------

Steps to connect and program the pins.


**How It Works:** Wire to pins, then code in e2 studio to control them.  

**Why It's Useful:** Prototype quickly – e.g., connect a sensor to read temperature.

.. START:tip:0:4:9

.. tip::

      Power off before connecting. Use GPIO pins for simple tests.
   
   

.. END:tip:0:4:9

.. START:table:0:4:13

.. csv-table:: Current Measurement Points
   :header: "Test Point", "Measures", "Resistor Location"
   :widths: 15, 30, 25

   "TP1 / TP3", "MCU 3.3V Current", "Across 5mΩ resistor"
   "TP2 / TP4", "USB 3.3V Current", "Across 5mΩ resistor"

.. END:table:0:4:13

Current Measurement
-------------------

Built-in resistors for measuring power use.


**How It Works:** Resistors (5mΩ) on power lines with test points (TP1-TP4) for voltage drops.  

**Why It's Useful:** Monitor MCU or USB current with Ohm's Law. Like a fuel gauge for power.

.. START:tip:0:4:12

.. tip::

      Measure voltage across resistors. Use for efficiency tests.
   

.. END:tip:0:4:12

.. START:section:0:5
Expansion Boards
================

.. END:section:0:5

.. START:main_content:0:5
Expansion boards are add-on modules that plug into the RB-RA8D1 to add features like displays or cameras. They're key for projects needing visuals or imaging. This section details the two included boards, how to connect them, and what you can do.

.. END:main_content:0:5

MIPI Graphics Expansion Board
-----------------------------

This board adds a touchscreen LCD for graphics and user interfaces.

**Features:** 4.5-inch TFT LCD with capacitive touch, 854x480 resolution, 16.7M colors, backlight. Part: E45RA-MW276-C.
.  
**How It Works:** Connects via 2-lane MIPI interface (J58) with I2C for touch and power pins.  

**Why Useful:** Display menus, demos, or apps. Like a mini screen for interactive projects.

.. START:tip:0:5:2

.. tip::

   Mount with nylon pillars.  
   Connect to J58.  
   Power on; splash screen appears.  
   Use touch for navigation.

.. END:tip:0:5:2

.. START:table:0:5:3

.. csv-table:: MIPI Graphics Port Pin Assignments (From Pinmux Sheet)
   :header: "Pin", "MCU Pin", "Signal", "Description"
   :widths: 10, 15, 20, 25

   "J58-1", "GND", "GND", "Ground"
   "J58-3", "-", "MIPI_DL0_P", "Data lane 0 positive"
   "J58-4", "-", "MIPI_DL1_P", "Data lane 1 positive"
   "J58-9", "P206", "MIPI_CL_P", "Clock positive"
   "J58-14", "P511", "I2C_SDA", "Touch data"
   "J58-16", "P512", "I2C_SCL", "Touch clock"
   "J58-15", "P404", "DISP_BLEN", "Backlight enable"
   "J58-18", "PA01", "DISP_RST", "Reset"

.. END:table:0:5:3

.. START:tip:0:5:4

.. tip::

   Enable pull-up for touch. In demos, shows AI results or weather.  
   Demos: Interactive menus, LED control, currency converter.

.. END:tip:0:5:4

Camera Expansion Board
----------------------

This board adds a camera for capturing images/videos.


**Features:** 3MP OV3640 camera, JPEG output, parallel interface, 15-30 fps. Part: ArduCam B0156.  

**How It Works:** Connects via camera port (J59) with I2C for control and data pins.  

**Why Useful:** For AI vision (face detection) or video projects. Like a webcam for the board.


.. START:tip:0:5:7

.. tip::

   Connect to J59.  
   Power on.  
   In demos, camera activates.

.. END:tip:0:5:7

.. START:note:0:5:8

.. note::

   Set SW1-3 ON (conflicts with Ethernet). Use for object classification.  
   Demos: Face detection, image classification.

.. END:note:0:5:8

.. START:table:0:5:9

.. csv-table:: Camera Port Pin Assignments (From Pinmux Sheet)
   :header: "Pin", "MCU Pin", "Signal", "Description"
   :widths: 10, 15, 20, 25

   "J59-1", "GND", "GND", "Ground"
   "J59-3", "P511", "I2C_SDA", "Control data"
   "J59-4", "P512", "I2C_SCL", "Control clock"
   "J59-5", "P709", "CAM_HD", "Horizontal sync"
   "J59-6", "P710", "CAM_VD", "Vertical sync"
   "J59-7", "P708", "CAM_XCLK", "Clock"
   "J59-8", "P403", "CAM_CLK", "Pixel clock"
   "J59-9", "P702", "CAM_D6", "Data bit 6"

.. END:table:0:5:9
