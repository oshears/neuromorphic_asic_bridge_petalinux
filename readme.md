# PetaLinux Build for Neuromorphic ASIC Bridge Project

## How to Build PetaLinux and Load the SD Card

### Configure PetaLinux
```
petalinux-config --get-hw-description=<PATH_TO_XSA_FILE>
```
- Auto Config Settings -> u-boot autoconfig
- Subsystem AUTO Hardware Settings -> Ethernet Settings -> Primary Ethernet -> Manual
- DTG Settings -> MACHINE_NAME -> zedboard
- Image Packaging Configuration -> Root filesystem type -> EXT4 (SD/eMMC/SATA/USB)
- Image Packaging Configuration -> Disable "Copy final images to tftpboot"

### Configure the Root File System
```
petalinux-config -c rootfs
```
- Filesystem Packages -> misc -> gcc-runtime
- Filesystem Packages -> misc -> packagegroup-core-build-essential
- Filesystem Packages -> misc -> python3 -> python3
- Filesystem Packages -> misc -> python3 -> python3-mmap
- Filesystem Packages -> misc -> python3-smmap
- Image Features -> auto-login
- apps -> peekpoke

### Build PetaLinux
```
petalinux-build
```
### Generate Boot Files
```
petalinux-package --boot --fsbl ./images/linux/zynq_fsbl.elf --fpga <PATH_TO_BIT_FILE> --u-boot --force
```
### Copy Files to SD Card
```
cp images/linux/BOOT.BIN /media/oshears/BOOT/
cp images/linux/image.ub /media/oshears/BOOT/
cp images/linux/boot.scr /media/oshears/BOOT/
sudo tar xvf ./images/linux/rootfs.tar.gz -C /media/oshears/ROOTFS/
sync
```

---



## Logging Into PetaLinux and Running Tests

### Configuring UART
```
sudo minicom -D /dev/ttyACM0
```

### Logging In
username: `root`

password: `root`

### Read and Write Registers from U-Boot
```
md 0x43c00000 
mw 0x43c00000 0x000000FF
```

### Read and Write Registers from Linux Commmand Line
#### Using `devmem`
```
devmem 0x43c00000
devmem 0x43c00000 32 0x000000FF
```
#### Using `peek` and `poke`
```
poke 0x43C00000
poke 0x43C00000 1
```

### Compile and Run the Demo from PetaLinux
C Demo
```
gcc -o demo demo.c
demo
```

Python Demo
```
python demo.py
```

---

## Terminology
### Board Support Package (BSP)
### First Stage Boot Loader (FSBL) Image
### U-Boot
### YOCTO
