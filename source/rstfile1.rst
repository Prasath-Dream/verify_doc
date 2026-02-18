=====================================
Hardware Configuration and Connection
===================================== 



.. START:section:0:0
Default HW configuration
========================

.. END:section:0:0

.. START:main_content:0:0
Use Debug On-Board mode: EK-RA8D1 board require to configure the jumpers for serial communication with host.

.. END:main_content:0:0

.. START:table:0:0:0

.. csv-table:: Jumper configuration
   :header: "Jumper", "Configurations"
   :align: center
   :widths: 20, 60

   "J6", "Open"
   "J8", "Jumper on pins 1-2"
   "J9", "Open"
   "J29", "Jumpers on pins 1-2, 3-4, 5-6, 7-8"

.. END:table:0:0:0

.. START:section:0:1
Hardware connection for UART samples
====================================

.. END:section:0:1

.. container:: spx-list-head

    1)echo_bot (samples/drivers/uart/echo_bot):

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:1:1

.. code-block:: console

   west build -p always -b ek_ra8d1 samples/drivers/uart/echo_bot/

.. END:code:0:1:1

.. container:: spx-list-head

    2)zTest uart_basic_api (tests/drivers/uart/uart_basic_api):

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:1:3

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/drivers/uart/uart_basic_api/

.. END:code:0:1:3

.. container:: spx-list-head

    3)zTest uart_async_api (tests/drivers/uart/uart_async_api):



- Hardware configuration: Loopback for TXD and RXD

.. START:table:0:1:5

.. csv-table:: SCI2 Loopback Connections
   :header: "Board", "Channel", "Pin function", "Pin", "Connect to"
   :align: center
   :widths: 15, 15, 20, 15, 35

   "EK-RA8D1", "SCI2", "TXD2_C", "PA03", "Loopback to RXD2_C pin"
   "EK-RA8D1", "SCI2", "RXD2_C", "PA02", "Loopback from TXD2_C pin"

.. END:table:0:1:5

- Build command:

.. START:code:0:1:8

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/drivers/uart/uart_async_api/

.. END:code:0:1:8

.. START:section:0:2
Hardware connection for SPI samples
===================================

.. END:section:0:2

.. START:main_content:0:2
- spi_bitbang (samples/drivers/spi_bitbang): Loopback for MISO and MOSI

- Note: The purpose of testing sample spi_bitbang on RA boards is to provide users with an understanding of the RA SPI driver. To test this sample using the SPI hardware IP, you can configure it by adding the overlay and configuration files with the following content:
 samples/drivers/spi_bitbang/boards/ek_ra8d1.conf

.. END:main_content:0:2

- Hardware configuration:

.. START:table:0:2:5

.. csv-table:: SPI1 Loopback Connections
   :header: "Board", "Channel", "Pin function", "Pin", "Connect to"
   :align: center
   :widths: 15, 15, 20, 15, 35

   "EK-RA8D1", "SPI1", "MISOB_B", "P410", "Loopback to MOSIB_B"
   "EK-RA8D1", "SPI1", "MOSIB_B", "P411", "Loopback to MISOB_B"

.. END:table:0:2:5

- Build command:

.. START:code:0:2:11

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/drivers/spi/spi_loopback

.. END:code:0:2:11

.. START:code:0:2:0

.. code-block:: console

   CONFIG_STDOUT_CONSOLE=y
   CONFIG_SPI=y
   CONFIG_SPI_B_INTERRUPT=y
   CONFIG_SPI_B_RA_DTC=y
   CONFIG_LOG=y
   CONFIG_SPI_BITBANG=n

.. END:code:0:2:0

.. START:note:0:2:2

.. note::

   We have to disable the CONFIG_SPI_BITBANG since we use SPI hardware IP to test spi_bitbang.

.. END:note:0:2:2



samples/drivers/spi_bitbang/boards/ek_ra8d1.overlay

.. START:code:0:2:3

.. code-block:: console

    spibb0: &spi1 {
      		rx-dtc;
      		tx-dtc;
      		pinctrl-0 = <&spi1_default>;
      		pinctrl-names = "default";
      		cs-gpios = <&ioport4 13 GPIO_ACTIVE_LOW>; // dummy config
      		status = "okay";
      	};
   
    &ioport4 {
      		status = "okay";
    };

.. END:code:0:2:3

- Build command:

.. START:code:0:2:7

.. code-block:: console

   west build -p always -b ek_ra8d1 samples/drivers/spi_bitbang

.. END:code:0:2:7

.. container:: spx-list-head

    zTest spi_loopback (tests/drivers/spi/spi_loopback)

- Hardware configuration: Loopback for MISO and MOSI

.. START:table:0:2:9

.. csv-table:: SPI1 Loopback Connections
   :header: "Board", "Channel", "Pin function", "Pin", "Connect to"
   :align: center
   :widths: 15, 15, 20, 15, 35

   "EK-RA8D1", "SPI1", "MISOB_B", "P410", "Loopback to MOSIB_B"
   "EK-RA8D1", "SPI1", "MOSIB_B", "P411", "Loopback to MISOB_B"

.. END:table:0:2:9

.. START:section:0:3
Hardware connection for I2C sample
==================================

.. END:section:0:3

.. container:: spx-list-head

    1) zTest i2c_api (tests/drivers/i2c/i2c_api): Require GY-271 QMC5883L module

- Hardware configuration:

.. START:table:0:3:1

.. csv-table:: GY271 to EK-RA8D1 Connections
   :header: "GY271", "EK-RA8D1"
   :align: center
   :widths: 15, 25

   "VCC", "P3V3"
   "GND", "GND"
   "SCL", "P512 (SCL1_A)"
   "SDA", "P511 (SDA1_A)"
   "DDBY", "-"

.. END:table:0:3:1

- Build command:

.. START:code:0:3:3

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/drivers/i2c/i2c_api

.. END:code:0:3:3

.. START:section:0:4
Hardware connection for Flash samples
=====================================

.. END:section:0:4

.. START:code:0:4:1

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/drivers/flash/common

.. END:code:0:4:1

.. container:: spx-list-head

    1) zTest flash common (tests/drivers/flash/common):

- Hardware configuration: No additional connection.
- Build command:

.. START:section:0:5
Hardware connection for Entropy samples
=======================================

.. END:section:0:5

.. START:code:0:5:1

.. code-block:: python

   west build -p always -b ek_ra8d1 tests/drivers/entropy/api

.. END:code:0:5:1

.. container:: spx-list-head

    1) zTest entropy api (tests/drivers/entropy/api):

- Hardware configuration: No additional connection.
- Build command:

.. START:section:0:6
Hardware connection for can samples
===================================

.. END:section:0:6

.. container:: spx-list-head

    1) zTest can api (tests/drivers/can/api):

- Hardware configuration: No additional connection.
- Build command:

.. container:: spx-list-head

    2) zTest can timing (tests/drivers/can/timing):

- Hardware configuration: No additional connection.
- Build command:

.. container:: spx-list-head

    3) zTest canbus conformance (tests/subsys/canbus/isotp/conformance):

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:6:5

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/subsys/canbus/isotp/conformance

.. END:code:0:6:5

.. container:: spx-list-head

    4) zTest canbus implementation (tests/subsys/canbus/isotp/implementation):

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:6:7

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/subsys/canbus/isotp/implementation

.. END:code:0:6:7

.. START:code:0:6:1

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/drivers/can/api

.. END:code:0:6:1

.. START:code:0:6:3

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/drivers/can/timing

.. END:code:0:6:3

.. START:section:0:7
Hardware connection for ospi samples
====================================

.. END:section:0:7

.. container:: spx-list-head

    1) zTest spi_flash (samples/drivers/spi_flash):

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:7:1

.. code-block:: python

   west build -p always -b ek_ra8d1 samples/drivers/spi_flash

.. END:code:0:7:1

.. container:: spx-list-head

    2) zTest jesd216 (samples/drivers/jesd216):

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:7:4

.. code-block:: console

   west build -p always -b ek_ra8d1 samples/drivers/jesd216

.. END:code:0:7:4

.. START:section:0:8
Hardware connection for SDHC samples
====================================

.. END:section:0:8

.. START:main_content:0:8
Hardware configuration:


.. END:main_content:0:8

.. START:table:0:8:0

.. csv-table:: PMOD SD to EK-RA8D1 Connections
   :header: "Board", "Channel", "Pin", "PMOD SD's Pin"
   :align: center
   :widths: 15, 15, 30, 20

   "EK-RA8D1", "SDMMC1", "P405 (DAT3) (J51 Pin8)", "Pin1 (CS)"
   "-", "-", "P401 (CMD) (J51 Pin7)", "Pin2 (MOSI)"
   "-", "-", "P402 (DAT0) (J52 Pin15)", "Pin3 (MISO)"
   "-", "-", "P400 (CLK) (J51 Pin10)", "Pin4 (SCLK)"
   "-", "-", "GND", "Pin5 (GND)"
   "-", "-", "+3V3 (VCC)", "Pin6 (VCC)"
   "-", "-", "P403 (DAT1) (J51 Pin9)", "Pin7 (DAT1)"
   "-", "-", "P404 (DAT2) (J57 Pin1)", "Pin8 (DAT2)"
   "-", "-", "P406 (CD) (J51 Pin5)", "Pin9 (CD)"
   "-", "-", "P700 (WP) (J51 Pin6)", "Pin10 (WP)"

.. END:table:0:8:0

.. START:warning:0:8:1

.. warning::

   Please aware that connect PMOD: use short wiring connections (should be shorter than 10cm).

.. END:warning:0:8:1

.. container:: spx-list-head

    1) zTest sdhc (tests/drivers/sdhc): Require "--shield pmod_sd" in build command

- Hardware configuration: No additional connection.
- Build command

.. START:code:0:8:4

.. code-block:: python

   west build -p always -b ek_ra8d1 --shield pmod_sd tests/drivers/sdhc

.. END:code:0:8:4

.. container:: spx-list-head

    2) zTest sdmmc (tests/subsys/sd/sdmmc): Require "--shield pmod_sd" in build command

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:8:6

.. code-block:: console

   west build -p always -b ek_ra8d1 --shield pmod_sd tests/subsys/sd/sdmmc

.. END:code:0:8:6

.. container:: spx-list-head

    3) zTest disk_access (tests/drivers/disk/disk_access): Require "--shield pmod_sd" in build command

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:8:9

.. code-block:: console

   west build -p always -b ek_ra8d1 --shield pmod_sd tests/drivers/disk/disk_access

.. END:code:0:8:9

.. container:: spx-list-head

    4) zTest fs ext2 (tests/subsys/fs/ext2): Require "--shield pmod_sd" in build command

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:8:11

.. code-block:: console

   west build -p always -b ek_ra8d1 --shield pmod_sd tests/subsys/fs/ext2

.. END:code:0:8:11

.. container:: spx-list-head

    5) zTest fs_sample (samples/subsys/fs/fs_sample): Require "--shield pmod_sd" in build command

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:8:13

.. code-block:: console

   west build -p always -b ek_ra8d1 --shield pmod_sd samples/subsys/fs/fs_sample

.. END:code:0:8:13

.. START:section:0:9
Hardware connection for ADC samples
===================================

.. END:section:0:9

.. container:: spx-list-head

    1) west build -p always -b ek_ra8d1 --shield pmod_sd samples/subsys/fs/fs_sample

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:9:1

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/drivers/adc/adc_api

.. END:code:0:9:1

.. container:: spx-list-head

    zTest adc_accuracy_test (tests/drivers/adc/adc_accuracy_test):

- Hardware configuration: Loopback 3V3 and AN000 (P004).
- Build command:

.. START:code:0:9:3

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/drivers/adc/adc_accuracy_test

.. END:code:0:9:3

.. START:section:0:10
Hardware connection for PWM (GPT) samples
=========================================

.. END:section:0:10

.. container:: spx-list-head

    1) zTest pwm_api (tests/drivers/pwm/pwm_api):

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:10:1

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/drivers/pwm/pwm_api

.. END:code:0:10:1

.. container:: spx-list-head

    2) zTest pwm_loopback (tests/drivers/pwm/pwm_loopback):

- Hardware configuration: Loopback 2 channels (1 PWM output, 1 PMW capture)

.. START:table:0:10:3

.. csv-table:: PWM Loopback Configuration
   :header: "Board", "Channel", "Pin", "Pin function", "Remark"
   :align: center
   :widths: 15, 10, 15, 20, 40

   "EK-RA8D1", "PWM7", "PA07", "GTIOC7A", "PWM output, loopback to PWM capture pin"
   "-", "PWM9", "P411", "GTIOC9A", "PWM capture, loopback to PWM output pin"

.. END:table:0:10:3

- Build command:

.. START:code:0:10:6

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/drivers/pwm/pwm_loopback

.. END:code:0:10:6

.. START:section:0:11
Hardware connection for Counter (AGT) samples
=============================================

.. END:section:0:11

.. container:: spx-list-head

    1) west build -p always -b ek_ra8d1 tests/drivers/pwm/pwm_loopback

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:11:1

.. code-block:: console

   west build -p always -b ek_ra8d1 samples/drivers/counter/alarm`

.. END:code:0:11:1

.. START:section:0:12
Hardware connection for USB samples
===================================

.. END:section:0:12

1) USB Device

- USB-FS as device: Connect J11 to a host PC.

.. START:table:0:12:1

.. csv-table:: Hardware Configuration
   :header: "Board", "Jumper", "Configurations"
   :align: center
   :widths: 15, 15, 30

   "EK-RA8D1", "J12", "pins 2-3"
   "-", "J15", "Closed"

.. END:table:0:12:1

- USB-HS as device: Connect J31 to a host PC

.. START:table:0:12:5

.. csv-table:: Hardware Configuration
   :header: "Board", "Jumper", "Configurations"
   :align: center
   :widths: 15, 15, 30

   "EK-RA8D1", "J7", "pins 2-3"
   "-", "J17", "Closed"

.. END:table:0:12:5

- USB Mass Storage (samples/subsys/usb/mass):

- Hardware configuration: No additional connection.

- Build command:

.. START:code:0:12:7

.. code-block:: console

   west build -p always -b ek_ra8d1 samples/subsys/usb/cdc_acm -DCONF_FILE=usbd_next_prj.conf

.. END:code:0:12:7

2) zTest udc (tests/drivers/udc):

- Hardware configuration: No additional connection.

- Build command:

.. START:code:0:12:11

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/drivers/udc

.. END:code:0:12:11

3) USB Host

- USB-HS as host: Connect J31 to OTG cable (Micro to USB Host (Female)), connect the other end of OTG cable to a USB device


.. START:table:0:12:14

.. csv-table:: Hardware Configuration
   :header: "Board", "Jumper", "Configurations"
   :align: center
   :widths: 15, 15, 30

   "EK-RA8D1", "J7", "pins 1-2"
   "-", "J17", "Open"

.. END:table:0:12:14

- Set the configuration switches (SW1) on the EK-RA8D1 board as below:

.. START:table:0:12:16

.. csv-table:: SW1 Switch Configuration
   :header: "SW1-1 PMOD1", "SW1-2 TRACE", "SW1-3 CAMERA", "SW1-4 ETHA", "SW1-5 ETHB", "SW1-6 GLCD", "SW1-7 SDRAM", "SW1-8 I3C"
   :align: center
   :widths: 15, 15, 15, 15, 15, 15, 15, 15

   "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF"

.. END:table:0:12:16

- USB shell (samples/subsys/usb/shell):

- Hardware configuration: No additional connection.

- Build command:

.. START:code:0:12:18

.. code-block:: console

   west build -p always -b ek_ra8d1 samples/subsys/usb/shell -DCONF_FILE=device_and_host_prj.conf

.. END:code:0:12:18

Known issue of USB-HS as host: The USB-HS host cannot work correctly with USB-HS device due to USB Voltage dropping.

- Confirmed USB-HS host can work correctly with USB-HS device after remove R83 and R84 resistors. Find R83 & R84 resistors.

- USB-HS host can work correctly with USB Full Speed/Low Speed device.

.. START:section:0:13
Hardware connection for MIPI-DSI samples
========================================

.. END:section:0:13

.. START:main_content:0:13
Connect the MIPI Graphics Expansion Board (included in the kit) to J58 of EK-RA8D1.

- Set the configuration switches (SW1) on the EK-RA8D1 board as below:

.. END:main_content:0:13

.. START:table:0:13:0

.. csv-table:: SW1 Switch Configuration
   :header: "SW1-1 PMOD1", "SW1-2 TRACE", "SW1-3 CAMERA", "SW1-4 ETHA", "SW1-5 ETHB", "SW1-6 GLCD", "SW1-7 SDRAM", "SW1-8 I3C"
   :align: center
   :widths: 15, 15, 15, 15, 15, 15, 15, 15

   "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "ON", "OFF"

.. END:table:0:13:0

.. container:: spx-list-head

    1) ztest display_read_write (tests/drivers/display/display_read_write): Require "--shield rtkmipilcdb00000be" in build command

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:13:4

.. code-block:: console

   west build -p always -b ek_ra8d1 --shield rtkmipilcdb00000be tests/drivers/display/display_read_write

.. END:code:0:13:4

.. container:: spx-list-head

    2) LVGL basic sample (samples/subsys/display/lvgl): Require "--shield rtkmipilcdb00000be" in build command

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:13:6

.. code-block:: console

   west build -p always -b ek_ra8d1 --shield rtkmipilcdb00000be samples/subsys/display/lvgl

.. END:code:0:13:6

.. container:: spx-list-head

    3) LVGL demos (samples/modules/lvgl/demos):Require information of display shield in build command

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:13:8

.. code-block:: console

   west build -b ek_ra8d1 samples/modules/lvgl/demos/ -T sample.modules.lvgl.demos.rtkmipilcdb00000be -p

.. END:code:0:13:8

.. START:section:0:14
Hardware connection for DAC samples
===================================

.. END:section:0:14

.. container:: spx-list-head

    1) ztest dac_api (tests/drivers/dac/dac_api):

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:14:1

.. code-block:: console

   west build -p always -b ek_ra8d1 tests/drivers/dac/dac_api

.. END:code:0:14:1

.. container:: spx-list-head

    2) DAC sample (samples/drivers/dac):

- Hardware configuration: No additional connection.
- Build command:

.. START:code:0:14:3

.. code-block:: console

   west build -p always -b ek_ra8d1 samples/drivers/dac

.. END:code:0:14:3
