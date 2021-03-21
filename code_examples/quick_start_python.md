# Quick Start with Python3

## Letter Reference Sheet
https://drive.google.com/file/d/1NKk71k131ZONjTr-Jv4CoLerobeFP7Y_/view?usp=sharing

----------------

## Registers
### Address Map

| Register Name | Register Address
|-|-
| Character Selection Register | 0x0
| Network Output Register | 0x4
| Direct Control Register | 0x8
| Debug Register | 0xC
| Analog Channel 0 Register | 0x10
| Analog Channel 1 Register | 0x14
| Analog Channel 2 Register | 0x18
| Analog Channel 3 Register | 0x1C

## Register Details

### Character Selection Register [0x0]
| Bit | Description 
|-|-
| 1:0 | Used to indicate the selected character
| 31:2 | Reserved

### Network Output Register [0x4]
| Bit | Description 
|-|-
| 1:0 | Used to report the network's prediction
| 31:2 | Reserved

### Direct Control Register [0x8]
| Bit | Description 
|-|-
| 15:0 | Used to send a custom character to the network
| 31:16 | Reserved

### Debug Register [0xC]
| Bit | Description 
|-|-
| 0 | Used to display the first 8 bits of the selected character output
| 1 | Used to display the first 8 bits of the direct control character output
| 2 | Used to output the direct control register's character output on the PMOD pins
| 3 | Uses slow 1Hz clock for character selection
| 4 | Enables 1-Hot encoding for XADC multiplexer bits
| 5 | Used to send a logic 1 (HIGH) to the XADC header's GPIO3 pin
| 5 | Used to send a logic 1 (HIGH) to the XADC header's GPIO3 pin
| 6 | Used to output the PWM Block's Clock on one of the digit outputs
| 15:16 | Reserved

### Analog Channel Registers [0x10 - 0x1C]
| Bit | Description 
|-|-
| 11:0 | Used report the analog value read in from the XADC
| 31:12 | Reserved

----------------

## Setup

### Import `os` and `mmap`
```
import os
import mmap
```

### Load Registers
```
mem_file = os.open("/dev/uio0", os.O_SYNC | os.O_RDWR)
regs = mmap.mmap(mem_file, 0x10000, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, 0)
```

----------------

## Character Selection

### Change Selected Character
#### Change Character to A:
```
regs[0x0] = 0x00
```
#### Change Character to J:
```
regs[0x0] = 0x01
```
#### Change Character to N:
```
regs[0x0] = 0x10
```
#### Change Character to X:
```
regs[0x0] = 0x11
```

----------------

## Network Output and Analog Values
### Read Network Output
```
regs[0x1]
```
### Read Analog Values
#### Channel 0
```
regs[0x10]
```
#### Channel 1
```
regs[0x14]
```
#### Channel 2
```
regs[0x18]
```
#### Channel 3
```
regs[0x1C]
```

----------------

## Configure LEDs
### Character Output on LEDs
```
regs[0xC] = 0x1
```
### Direct Control Output on LEDs
```
regs[0xC] = 0x2
```

----------------

## Slow Output Mode
### Enable Slow Clock
```
regs[0xC] = 0x08
```
### Set PWM Clock Divider
```
regs[0x20] = 0x14
```

----------------

## Direct Control Mode

### Direct Control Mode Output
```
regs[0xC] = 0x4
```
### 1 HZ Frequency
```
regs[0x20] = 0x14
```

### Change Direct CTRL Mode Characters
#### Change Character to A:
```
regs[8:12] = bytes([0b1111_1001,0b1111_1001,0b0000_0000,0b0000_0000])
```
#### Change Character to J:
```
regs[8:12] = bytes([0b1001_0110,0b0001_0001,0b0000_0000,0b0000_0000])
```
#### Change Character to N:
```
regs[8:12] = bytes([0b1011_1001,0b1001_1101,0b0000_0000,0b0000_0000])
```
#### Change Character to X:
```
regs[8:12] = bytes([0b0110_1001,0b1001_0110,0b0000_0000,0b0000_0000])
```

----------------

## Miscellaneous
### Drive GPIO3 High
```
regs[0xC] = 0x20
```

----------------

## PWM Block
### Enable PWM Clock Output
```
regs[0xC] = 0x40
```
### Set PWM Clock Divider
```
regs[0x20] = 0x14
```
### Set PWM Duty Cycle
```
regs[0x24:0x28] = bytes([0x00,0x00,0x08,0x00])
```
### Common Configurations 
#### 1Hz, 50% Duty Cycle (1MHz PWM Clock)
```
regs[0xC] = 0x40
regs[0x20] = 0x14
regs[0x24:0x28] = bytes([0x00,0x00,0x08,0x00])
```
#### 100Khz, 50% Duty Cycle (1MHz PWM Clock)
```
regs[0xC] = 0x40
regs[0x20] = 0x03
regs[0x24:0x28] = bytes([0x04,0x00,0x00,0x00])
```
#### 1Hz, 50% Duty Cycle (100MHz PWM Clock)
```
regs[0xC] = 0xC0
regs[0x20] = 0x1B
regs[0x24:0x28] = bytes([0x00,0x00,0x00,0x04])
```
#### 100Khz, 50% Duty Cycle (100MHz PWM Clock)
```
regs[0xC] = 0xC0
regs[0x20] = 0x09
regs[0x24:0x28] = bytes([0x00,0x01,0x00,0x00])
```

----------------

## Clock Divider Calculations (1MHz PWM_CLK)
The duty cycle of the clock can be calculated using the following equation:
```
DUTY_CYCLE = DUTY_CYCLE_REG / MAX_COUNTER
```
| Divider Value | Divider Reg | HZ           | Seconds     | Duty Cycle Resolution | Max Counter | Max Counter (Hex) | 50% Duty Cycle Reg Value |
|---------------|-------------|--------------|-------------|-----------------------|-------------|-------------------|--------------------------|
| 0             | 00          | 333333.33333 | 0.000003    | 3                     | 1           | 00000001          | 00000000                 |
| 1             | 01          | 250000.00000 | 0.000004    | 4                     | 2           | 00000002          | 00000001                 |
| 2             | 02          | 166666.66667 | 0.000006    | 6                     | 4           | 00000004          | 00000002                 |
| 3             | 03          | 100000.00000 | 0.000010    | 10                    | 8           | 00000008          | 00000004                 |
| 4             | 04          | 55555.55556  | 0.000018    | 18                    | 16          | 00000010          | 00000008                 |
| 5             | 05          | 29411.76471  | 0.000034    | 34                    | 32          | 00000020          | 00000010                 |
| 6             | 06          | 15151.51515  | 0.000066    | 66                    | 64          | 00000040          | 00000020                 |
| 7             | 07          | 7692.30769   | 0.000130    | 130                   | 128         | 00000080          | 00000040                 |
| 8             | 08          | 3875.96899   | 0.000258    | 258                   | 256         | 00000100          | 00000080                 |
| 9             | 09          | 1945.52529   | 0.000514    | 514                   | 512         | 00000200          | 00000100                 |
| 10            | 0A          | 974.65887    | 0.001026    | 1026                  | 1024        | 00000400          | 00000200                 |
| 11            | 0B          | 487.80488    | 0.002050    | 2050                  | 2048        | 00000800          | 00000400                 |
| 12            | 0C          | 244.02147    | 0.004098    | 4098                  | 4096        | 00001000          | 00000800                 |
| 13            | 0D          | 122.04052    | 0.008194    | 8194                  | 8192        | 00002000          | 00001000                 |
| 14            | 0E          | 61.02771     | 0.016386    | 16386                 | 16384       | 00004000          | 00002000                 |
| 15            | 0F          | 30.51572     | 0.032770    | 32770                 | 32768       | 00008000          | 00004000                 |
| 16            | 10          | 15.25832     | 0.065538    | 65538                 | 65536       | 00010000          | 00008000                 |
| 17            | 11          | 7.62928      | 0.131074    | 131074                | 131072      | 00020000          | 00010000                 |
| 18            | 12          | 3.81467      | 0.262146    | 262146                | 262144      | 00040000          | 00020000                 |
| 19            | 13          | 1.90734      | 0.524290    | 524290                | 524288      | 00080000          | 00040000                 |
| 20            | 14          | 0.95367      | 1.048578    | 1048578               | 1048576     | 00100000          | 00080000                 |
| 21            | 15          | 0.47684      | 2.097154    | 2097154               | 2097152     | 00200000          | 00100000                 |
| 22            | 16          | 0.23842      | 4.194306    | 4194306               | 4194304     | 00400000          | 00200000                 |
| 23            | 17          | 0.11921      | 8.388610    | 8388610               | 8388608     | 00800000          | 00400000                 |
| 24            | 18          | 0.05960      | 16.777218   | 16777218              | 16777216    | 01000000          | 00800000                 |
| 25            | 19          | 0.02980      | 33.554434   | 33554434              | 33554432    | 02000000          | 01000000                 |
| 26            | 1A          | 0.01490      | 67.108866   | 67108866              | 67108864    | 04000000          | 02000000                 |
| 27            | 1B          | 0.00745      | 134.217730  | 134217730             | 134217728   | 08000000          | 04000000                 |
| 28            | 1C          | 0.00373      | 268.435458  | 268435458             | 268435456   | 10000000          | 08000000                 |
| 29            | 1D          | 0.00186      | 536.870914  | 536870914             | 536870912   | 20000000          | 10000000                 |
| 30            | 1E          | 0.00093      | 1073.741826 | 1073741826            | 1073741824  | 40000000          | 20000000                 |
| 31            | 1F          | 0.00047      | 2147.483650 | 2147483650            | 2147483648  | 80000000          | 40000000                 |

----------------

## Clock Divider Calculations (100MHz PWM_CLK)
| Divider Value | Divider Reg | HZ          | Seconds     | Duty Cycle Resolution | Max Counter | Max Counter (Hex) | 50% Duty Cycle Reg Value |
|---------------|-------------|-------------|-------------|-----------------------|-------------|-------------------|--------------------------|
| 0             | 00          | 33333333.33 | 0.00000003  | 3                     | 1           | 00000001          | 00000000                 |
| 1             | 01          | 25000000.00 | 0.00000004  | 4                     | 2           | 00000002          | 00000001                 |
| 2             | 02          | 16666666.67 | 0.00000006  | 6                     | 4           | 00000004          | 00000002                 |
| 3             | 03          | 10000000.00 | 0.00000010  | 10                    | 8           | 00000008          | 00000004                 |
| 4             | 04          | 5555555.56  | 0.00000018  | 18                    | 16          | 00000010          | 00000008                 |
| 5             | 05          | 2941176.47  | 0.00000034  | 34                    | 32          | 00000020          | 00000010                 |
| 6             | 06          | 1515151.52  | 0.00000066  | 66                    | 64          | 00000040          | 00000020                 |
| 7             | 07          | 769230.77   | 0.00000130  | 130                   | 128         | 00000080          | 00000040                 |
| 8             | 08          | 387596.90   | 0.00000258  | 258                   | 256         | 00000100          | 00000080                 |
| 9             | 09          | 194552.53   | 0.00000514  | 514                   | 512         | 00000200          | 00000100                 |
| 10            | 0A          | 97465.89    | 0.00001026  | 1026                  | 1024        | 00000400          | 00000200                 |
| 11            | 0B          | 48780.49    | 0.00002050  | 2050                  | 2048        | 00000800          | 00000400                 |
| 12            | 0C          | 24402.15    | 0.00004098  | 4098                  | 4096        | 00001000          | 00000800                 |
| 13            | 0D          | 12204.05    | 0.00008194  | 8194                  | 8192        | 00002000          | 00001000                 |
| 14            | 0E          | 6102.77     | 0.00016386  | 16386                 | 16384       | 00004000          | 00002000                 |
| 15            | 0F          | 3051.57     | 0.00032770  | 32770                 | 32768       | 00008000          | 00004000                 |
| 16            | 10          | 1525.83     | 0.00065538  | 65538                 | 65536       | 00010000          | 00008000                 |
| 17            | 11          | 762.93      | 0.00131074  | 131074                | 131072      | 00020000          | 00010000                 |
| 18            | 12          | 381.47      | 0.00262146  | 262146                | 262144      | 00040000          | 00020000                 |
| 19            | 13          | 190.73      | 0.00524290  | 524290                | 524288      | 00080000          | 00040000                 |
| 20            | 14          | 95.37       | 0.01048578  | 1048578               | 1048576     | 00100000          | 00080000                 |
| 21            | 15          | 47.68       | 0.02097154  | 2097154               | 2097152     | 00200000          | 00100000                 |
| 22            | 16          | 23.84       | 0.04194306  | 4194306               | 4194304     | 00400000          | 00200000                 |
| 23            | 17          | 11.92       | 0.08388610  | 8388610               | 8388608     | 00800000          | 00400000                 |
| 24            | 18          | 5.96        | 0.16777218  | 16777218              | 16777216    | 01000000          | 00800000                 |
| 25            | 19          | 2.98        | 0.33554434  | 33554434              | 33554432    | 02000000          | 01000000                 |
| 26            | 1A          | 1.49        | 0.67108866  | 67108866              | 67108864    | 04000000          | 02000000                 |
| 27            | 1B          | 0.75        | 1.34217730  | 134217730             | 134217728   | 08000000          | 04000000                 |
| 28            | 1C          | 0.37        | 2.68435458  | 268435458             | 268435456   | 10000000          | 08000000                 |
| 29            | 1D          | 0.19        | 5.36870914  | 536870914             | 536870912   | 20000000          | 10000000                 |
| 30            | 1E          | 0.09        | 10.73741826 | 1073741826            | 1073741824  | 40000000          | 20000000                 |
| 31            | 1F          | 0.05        | 21.47483650 | 2147483650            | 2147483648  | 80000000          | 40000000                 |

----------------

## PMOD DAC Interface
### Enable PMOD DAC Interface on JA1 PMOD Pins
```
regs[0x0C:0x10] = bytes([0x00,0x01,0x00,0x00])
```
### Write Data to PMOD DAC
```
regs[0x2C:0x30] = bytes([0xFF,0xFF,0x03,0x00])
```
### Clear PMOD DAC CFG Reg
```
regs[0x2C:0x30] = bytes([0xFF,0xFF,0x00,0x00])
```

----------------

## Digit Output at 500kHz
### Slow Clock Enable, Display Digits on LEDs
```
regs[0x0C] = 0x09
```
### 500kHz Frequency
```
regs[0x20] = 0x01
```
### 0.5s Period
```
regs[0x20] = 0x13
```