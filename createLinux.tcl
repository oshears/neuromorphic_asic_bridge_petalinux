#xsct createLinux.tcl

petalinux-install-path /home/oshears/PetaLinux/

petalinux-create --type project --template zynq --name neuormorphic_petalinux
petalinux-config --get-hw-description=~/Documents/vt/research/code/verilog/neuromorphic_asic_bridge/vivado/neuromorphic_asic_bridge_system_project/neuromorphic_asic_bridge_system_wrapper.xsa
# Auto Config Settings -> u-boot autoconfig
# Subsystem AUTO Hardware Settings -> Ethernet Settings -> Primary Ethernet -> Manual
# DTG Settings -> MACHINE_NAME -> zedboard
# Image Packaging Configuration -> Root filesystem type -> EXT4 (SD/eMMC/SATA/USB)
# Image Packaging Configuration -> Disable "Copy final images to tftpboot"
petalinux-config -c rootfs
# Filesystem Packages -> misc -> gcc-runtime
# Filesystem Packages -> misc -> packagegroup-core-build-essential
# Filesystem Packages -> misc -> python3 -> python3
# Filesystem Packages -> misc -> python3 -> python3-threading
# Filesystem Packages -> misc -> python3 -> python3-threading
# Filesystem Packages -> misc -> python3 -> python3-mmap
# Filesystem Packages -> misc -> python3-smmap
# Petalinux Package Groups -> packagegroup-petalinux-opencv
# Petalinux Package Groups -> packagegroup-petalinux-python-modules
# Image Features -> auto-login
# apps -> peekpoke
#petalinux-build -x clean
#petalinux-build
petalinux-config -c kernel
#petalinux-build -c kernel -x update-recipe
#petalinux-build -c kernel -x finish
#petalinux-build -c kernel
# For Webcam Support:
# Device Drivers
# USB support
#     <*> Support for Host-side USB
#     <*> OTG support
#     <*> EHCI HCD (USB 2.0) support
#     <*> USB Mass Storage support
#     <*> ChipIdea Highspeed Dual Role Controller
#     <*> ChipIdea host controller
#     <*> ChipIdea device controller
#         USB Physical Layer drivers --->
#         <*> NOP USB Transceiver Driver
#     <*> USB Gadget Support
#           <M> USB Gadget Drivers
#           <M> USB functions configurable through configfs
#           [*] Mass storage
#           [*] USB Webcam function
#           [*] USB Webcam function
#           [*] USB Webcam Gadget
# Multimedia Support
#     [*] Media USB Adapters
#           <M> USB Video Class(UVC)
#               [*] USB Video Class(UVC) Input Event Support

# Device Drivers > Multimedia Support > Media USB Adapter > USB Video Class (UVC)
# Device Drivers > Multimedia Support > Media USB Adapter > USB Video Class (UVC) Input Event Support
# Device Drivers -> Industrial I/O support -> Analog to digital converters -> < > Xilinx XADC driver
# Device Drivers -> Userspace I/O drivers
# <*> Userspace I/O platform driver with generic IRQ handing
# <*> Userspace platform driver with generic irq and dynamic memory
# <*> Xilinx AI Engine driver
# Exclde USB 2.0 OTG FSM Implementation in Device Drivers > USB Support
petalinux-build
petalinux-package --boot --fsbl ./images/linux/zynq_fsbl.elf --fpga ~/Documents/vt/research/code/verilog/neuromorphic_asic_bridge/vivado/neuromorphic_asic_bridge_system_project/neuromorphic_asic_bridge_system_project.runs/impl_1/neuromorphic_asic_bridge_system_wrapper.bit --u-boot --force
cp images/linux/BOOT.BIN /media/oshears/BOOT/
cp images/linux/image.ub /media/oshears/BOOT/
cp images/linux/boot.scr /media/oshears/BOOT/
sudo tar xvf ./images/linux/rootfs.tar.gz -C /media/oshears/ROOTFS/
sync
# watch grep -e Dirty: -e Writeback: /proc/meminfo
#udisksctl unmount -b /dev/sdb1
#udisksctl power-off -b /dev/sdb
# also if you run petalinux-build ic kernel -x finish it will copy the fragment to you recipe
# Copying Kernel Config
# https://forums.xilinx.com/t5/Embedded-Linux/petalinux-2020-1-kernel-config-file/td-p/1147298
# Creating Custom Linux UIO
# https://forums.xilinx.com/t5/Embedded-Linux/Custom-Hardware-with-UIO/td-p/804303
# I also checked Yocto/build-tool in petalinux-config. Default setting is bitbake, not devtool. 
# After changing to devtool, the bahaviour of whole process is slightly different. 
# I found it inconvenient, especially due to different file naming scheme in meta-user.
# XRT
# https://xilinx.github.io/XRT/2018.3/html/yocto.html#add-xrt-kernel-node-in-device-tree
#petalinux-build -c device-tree -x cleansstate
#petalinux-build -c device-tree
#petalinux-config -c kernel
#petalinux-build -c kernel
#petalinux-build -c kernel -x update-recipe
#petalinux-build -c kernel -x finish
#petalinux-build -x mrproper -f

# setenv bootargs 'console=ttyPS0,115200 earlyprintk uio_pdrv_genirq.of_id=generic-uio root=/dev/mmcblk0p2'
# saveenv
# boot