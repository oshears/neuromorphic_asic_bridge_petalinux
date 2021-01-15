# Quick Start with Python3

## Letter Reference Sheet
https://drive.google.com/file/d/1NKk71k131ZONjTr-Jv4CoLerobeFP7Y_/view?usp=sharing

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
regs[0x8] = 0b1111_1001_1111_1001
```
#### Change Character to J:
```
regs[0x8] = 0b0001_0001_1001_0110
```
#### Change Character to N:
```
regs[0x8] = 0b1001_1101_1011_1001
```
#### Change Character to X:
```
regs[0x8] = 0b1001_0110_0110_1001
```
## Miscellaneous
### Drive GPIO3 High
```
regs[0xC] = 0x20
```