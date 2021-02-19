import os
import mmap
import time


mem_file = os.open("/dev/uio0", os.O_SYNC | os.O_RDWR)
neuromorphic_bridge_axi_addr_size = 0x10000
neuromorphic_bridge_registers = mmap.mmap(mem_file, neuromorphic_bridge_axi_addr_size, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, 0) 
regs = neuromorphic_bridge_registers

CHAR_SEL_REG = 0x0
NET_OUT_REG = 0x4
DIRECT_CTRL_REG = 0x8
DBG_REG = 0xC
VAUX0_REG = 0x10
VAUX1_REG = 0x14
VAUX2_REG = 0x18
VAUX3_REG = 0x1C
PWM_CLK_DIV_REG = 0x20
PWM_BLK_DUTY_CYCLE_REG = 0x24

# DBG Controls
# BIT 0: IF ACTIVE, then display char information on LEDs, ELSE display network output on LEDS
# BIT 1: IF ACTIVE, then display direct_ctrl_reg values on LEDS, ELSE display char_pwm_gen outputs on LEDS 
# BIT 2: Use direct_ctrl_reg value as digit outputs ELSE use char_pwm_gen
# BIT 3: Use slow 1HZ Clock
# BIT 4: Use 1-Hot Encoding for XADC Multiplexer
# BIT 5: debug_reg[5] output on XADC header GPIO3
PWM_BLK_HS_CLK_SEL = 0x80
PWM_BLK_CLK_OUT = 0x40
DBG_REG_GPIO3_HIGH = 0x20
DBG_REG_1HOT = 0x10
DBG_REG_1HZ = 0x08
DBG_REG_DIRECT_CTRL_DIGIT_OUT = 0x04
DBG_REG_DIRECT_CTRL_LED_OUT = 0x02
DBG_REG_CHAR_SELECT_LED_OUT = 0x01

# Change Frequency to 1HZ
# Display Char Select Reg Outputs on LEDS
neuromorphic_bridge_registers[DBG_REG] = DBG_REG_1HZ | DBG_REG_CHAR_SELECT_LED_OUT
print(f"Debug Register: { neuromorphic_bridge_registers[DBG_REG] }")

# Test Char Select Register
for i in range(4):
    neuromorphic_bridge_registers[CHAR_SEL_REG] = i
    print(f"Character Select Register: { neuromorphic_bridge_registers[CHAR_SEL_REG] }")
    time.sleep(2)

# Network Output Register
print(f"Network Output Register: { neuromorphic_bridge_registers[NET_OUT_REG] }")

# Change Frequency to 1HZ
# Display Direct Control Reg Outputs on LEDS
# Place Direct Control Outputs on Digit Outputs
neuromorphic_bridge_registers[DBG_REG] = DBG_REG_1HZ | DBG_REG_DIRECT_CTRL_LED_OUT | DBG_REG_DIRECT_CTRL_DIGIT_OUT
print(f"Debug Register: { neuromorphic_bridge_registers[DBG_REG] }")


# Test Direct Control Register
for i in range(16):
    neuromorphic_bridge_registers[DIRECT_CTRL_REG] = i
    print(f"Direct Control Register: { neuromorphic_bridge_registers[DIRECT_CTRL_REG] }")
    time.sleep(0.1)


# Cycle Through Network Output
userInput = ""
neuromorphic_bridge_registers[DBG_REG] = 0x0

print("Press [ENTER] to cycle through network output and analog voltage registers.")

while userInput != "q":
    print(f"Network Output: {neuromorphic_bridge_registers[NET_OUT_REG]}")
    print(f"VAUX0: {neuromorphic_bridge_registers[VAUX0_REG]}")
    print(f"VAUX1: {neuromorphic_bridge_registers[VAUX1_REG]}")
    print(f"VAUX2: {neuromorphic_bridge_registers[VAUX2_REG]}")
    print(f"VAUX3: {neuromorphic_bridge_registers[VAUX3_REG]}")

    userInput = input()


# Cycle Through Duty Cycles At 100KHz (1MHz Ref Clk)
regs[0xC] = 0x40
regs[0x20] = 0x03
regs[0x24:0x28] = bytes([0x00,0x00,0x00,0x00])
for i in range(0,10,1):
    print(f"Duty Cycle: {(i/9)*100}%")
    regs[0x24:0x28] = bytes([i,0x00,0x00,0x00])
    time.sleep(1)

# Cycle Through Duty Cycles At 100KHz (1MHz Ref Clk)
regs[0xC] = 0x40
regs[0x20] = 0x03
regs[0x24:0x28] = bytes([0x00,0x00,0x00,0x00])
max_count = 0x8
step_size = max(int(max_count / 10),1)
for i in range(0,max_count,step_size):
    print(f"Duty Cycle: {(i/max_count)*100}%")
    regs[0x24:0x28] = bytes([(i >> 0) & 0xF,(i >> 8) & 0xF,(i >> 16) & 0xF,(i >> 24) & 0xF])
    time.sleep(1)

# Cycle Through Duty Cycles At 1Hz (1MHz Ref Clk)
regs[0xC] = 0x40
regs[0x20] = 0x14
regs[0x24:0x28] = bytes([0x00,0x00,0x00,0x00])
max_count = 0x80000
step_size = max(int(max_count / 10),1)
for i in range(0,max_count,step_size):
    print(f"Duty Cycle: {(i/max_count)*100}%")
    regs[0x24:0x28] = bytes([(i >> 0) & 0xF,(i >> 8) & 0xF,(i >> 16) & 0xF,(i >> 24) & 0xF])
    time.sleep(1)
    
    
# Cycle Through Duty Cycles At 100KHz (100MHz Ref Clk)
regs[0xC] = 0xC0
regs[0x20] = 0x0A
regs[0x24:0x28] = bytes([0x00,0x00,0x00,0x00])
max_count = 0x200
step_size = int(max_count / 10)
for i in range(0,max_count,step_size):
    print(f"Duty Cycle: {(i/max_count)*100}%")
    regs[0x24:0x28] = bytes([(i >> 0) & 0xF,(i >> 8) & 0xF,(i >> 16) & 0xF,(i >> 24) & 0xF])
    time.sleep(1)
    