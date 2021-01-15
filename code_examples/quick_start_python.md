# Quick Start with Python3

## Letter Reference Sheet
https://drive.google.com/file/d/1NKk71k131ZONjTr-Jv4CoLerobeFP7Y_/view?usp=sharing

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
| 15:6 | Reserved

### Analog Channel Registers [0x10 - 0x1C]
| Bit | Description 
|-|-
| 11:0 | Used report the analog value read in from the XADC
| 31:12 | Reserved

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

## Direct Control Mode

### Direct Control Mode Output
```
regs[0xC] = 0x4
```

### Change Direct CTRL Mode Characters
#### Change Character to A:
```
regs[8:12] = bytes([0b1111_1001,0b1111_1001,0b0000_0000_,0b0000_0000])
```
#### Change Character to J:
```
regs[8:12] = bytes([0b1001_0110,0b0001_0001,0b0000_0000_,0b0000_0000])
```
#### Change Character to N:
```
regs[8:12] = bytes([0b1011_1001,0b1001_1101,0b0000_0000_,0b0000_0000])
```
#### Change Character to X:
```
regs[8:12] = bytes([0b0110_1001,0b1001_0110,0b0000_0000_,0b0000_0000])
```
## Miscellaneous
### Drive GPIO3 High
```
regs[0xC] = 0x20
```
