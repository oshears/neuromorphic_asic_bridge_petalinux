import os
import mmap
import time


mem_file = os.open("/dev/mem", os.O_SYNC | os.O_RDWR)
neuromorphic_bridge_axi_base_addr = 0x43C00000
neuromorphic_bridge_axi_addr_size = 0x10000
neuromorphic_bridge_registers = mmap.mmap(mem_file, neuromorphic_bridge_axi_addr_size, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, 0, neuromorphic_bridge_axi_base_addr) 

CHAR_SEL_REG = 0
NET_OUT_REG = 4
DIRECT_CTRL_REG = 8
DBG_REG = 12

DBG_REG_1HZ = 0x8
DBG_REG_DIRECT_CTRL_DIGIT_OUT = 0x4
DBG_REG_DIRECT_CTRL_LED_OUT = 0x2
DBG_REG_CHAR_SELECT_LED_OUT = 0x1

# Change Frequency to 1HZ
# Display Char Select Reg Outputs on LEDS
neuromorphic_bridge_registers[DBG_REG] = DBG_REG_1HZ | DBG_REG_CHAR_SELECT_LED_OUT
print(f"Debug Register: { neuromorphic_bridge_registers[DBG_REG] }")

# Test Char Select Register
for i in range(4):
    neuromorphic_bridge_registers[CHAR_SEL_REG] = i
    print(f"Character Select Register: { neuromorphic_bridge_registers[CHAR_SEL_REG] }")
    time.sleep(5)

# Network Output Register
print(f"Network Output Register: { neuromorphic_bridge_registers[NET_OUT_REG] }")

# Change Frequency to 1HZ
# Display Direct Control Reg Outputs on LEDS
# Place Direct Control Outputs on Digit Outputs
neuromorphic_bridge_registers[DBG_REG] = DBG_REG_1HZ | DBG_REG_DIRECT_CTRL_LED_OUT | DBG_REG_DIRECT_CTRL_DIGIT_OUT
print(f"Debug Register: { neuromorphic_bridge_registers[DBG_REG] }")


# Test Direct Control Register
for i in range(2**16):
    neuromorphic_bridge_registers[DIRECT_CTRL_REG] = i
    print(f"Direct Control Register: { neuromorphic_bridge_registers[DIRECT_CTRL_REG] }")
    time.sleep(0.1)
