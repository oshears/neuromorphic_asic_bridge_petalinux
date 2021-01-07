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
petalinux-config -c kernel
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
# Exclde USB 2.0 OTG FSM Implementation in Device Drivers > USB Support
petalinux-build
petalinux-package --boot --fsbl ./images/linux/zynq_fsbl.elf --fpga ~/Documents/vt/research/code/verilog/neuromorphic_asic_bridge/vivado/neuromorphic_asic_bridge_system_project/neuromorphic_asic_bridge_system_project.runs/impl_1/neuromorphic_asic_bridge_system_wrapper.bit --u-boot --force
cp images/linux/BOOT.BIN /media/oshears/BOOT/
cp images/linux/image.ub /media/oshears/BOOT/
cp images/linux/boot.scr /media/oshears/BOOT/
sudo tar xvf ./images/linux/rootfs.tar.gz -C /media/oshears/ROOTFS/