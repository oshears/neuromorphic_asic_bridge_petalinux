import os
import mmap

mem_file = os.open("/dev/uio0", os.O_SYNC | os.O_RDWR)
regs = mmap.mmap(mem_file, 0x10000, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, 0)

# Direct Ctrl Mode Output, Slow Clk, Digits on LEDs
regs[0x0C] = 0x0D
# 500Hz
regs[0x20] = 0x0B
# All in Phase
regs[8:12] = bytes([0b1111_1111,0b1111_1111,0b1111_1111,0b1111_1111])
# Half in Phase
regs[8:12] = bytes([0b1010_1010,0b1010_1010,0b1010_1010,0b1010_1010])
# Corrected J


# PMOD DAC
# PMOD DAC Output
regs[0x0C:0x10] = bytes([0x00,0x01,0x00,0x00])
# 0xFFFF (2.5V)
regs[0x2C:0x30] = bytes([0xFF,0xFF,0x03,0x00])
# 0xFFFF (1.25V)
regs[0x2C:0x30] = bytes([0xFF,0x7F,0x03,0x00])
# 0xFFFF (1.25V)
regs[0x2C:0x30] = bytes([0xFF,0x3F,0x03,0x00])