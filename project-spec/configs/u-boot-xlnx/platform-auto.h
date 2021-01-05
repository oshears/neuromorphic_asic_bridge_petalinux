/*
 * This file is auto-generated by PetaLinux SDK 
 * DO NOT MODIFY this file, the modification will not persist
 */

#ifndef __PLNX_CONFIG_H
#define __PLNX_CONFIG_H

/* The following table includes the supported baudrates */


#define CONFIG_SYS_BAUDRATE_TABLE  { 300, 600, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200, 230400 }



/* processor - ps7_cortexa9_0 */
#define CONFIG_CPU_FREQ_HZ	666666687
#define CONFIG_CLOCKS
#define CONFIG_ARM_DCC
#define CONFIG_REMAKE_ELF
#define CONFIG_SYS_LDSCRIPT	"arch/arm/mach-zynq/u-boot.lds"

/* main_memory - ps7_ddr_0 */

/* uart - ps7_uart_1 */
#define PSSERIAL0	"psserial0=setenv stdout ttyPS0;setenv stdin ttyPS0\0"
#define SERIAL_MULTI	"serial=setenv stdout serial;setenv stdin serial\0"
#define CONSOLE_ARG	"console=console=ttyPS0,115200\0"
#define SERIAL_MULTI  "serial=setenv stdout serial;setenv stdin serial\0"
#define CONFIG_BAUDRATE	115200

/* spi_flash - ps7_qspi_0 */
#define XILINX_PS7_QSPI_CLK_FREQ_HZ	200000000
#define CONFIG_SF_DEFAULT_SPEED	(XILINX_PS7_QSPI_CLK_FREQ_HZ / 4)

/* sdio - ps7_sd_0 */

/* usb - ps7_usb_0 */
#define CONFIG_EHCI_IS_TDI
#define CONFIG_THOR_RESET_OFF
#define CONFIG_SYS_DFU_DATA_BUF_SIZE 0x600000
#define DFU_DEFAULT_POLL_TIMEOUT 300

/* devcfg - ps7_dev_cfg_0 */
#define CONFIG_FPGA_ZYNQPL

/* ps7_scutimer_0 */
#define ZYNQ_SCUTIMER_BASEADDR	0xF8F00600
#define CONFIG_SYS_TIMER_COUNTS_DOWN
#define CONFIG_SYS_TIMERBASE	ZYNQ_SCUTIMER_BASEADDR
#define CONFIG_SYS_TIMER_COUNTER	(CONFIG_SYS_TIMERBASE + 0x4)

/* FPGA */

/* Memory testing handling */
#define CONFIG_SYS_MEMTEST_START	0x0
#define CONFIG_SYS_MEMTEST_END	(0x0 + 0x1000)
#define CONFIG_SYS_LOAD_ADDR	0x0 /* default load address */
#define CONFIG_NR_DRAM_BANKS	1

/* Size of malloc() pool */
#define SIZE	0xC00000
#define CONFIG_SYS_MALLOC_LEN	SIZE

/* Physical Memory Map */
#define CONFIG_SYS_INIT_RAM_ADDR	0xFFFF0000
#define CONFIG_SYS_INIT_RAM_SIZE	0x2000
#define CONFIG_SYS_INIT_SP_ADDR	(CONFIG_SYS_INIT_RAM_ADDR + \ 
				CONFIG_SYS_INIT_RAM_SIZE - \ 
				GENERATED_GBL_DATA_SIZE)


/* BOOTP options */
#define CONFIG_BOOTP_SERVERIP
#define CONFIG_BOOTP_BOOTFILESIZE
#define CONFIG_BOOTP_BOOTPATH
#define CONFIG_BOOTP_GATEWAY
#define CONFIG_BOOTP_HOSTNAME
#define CONFIG_BOOTP_MAY_FAIL
#define CONFIG_BOOTP_DNS
#define CONFIG_BOOTP_SUBNETMASK
#define CONFIG_BOOTP_PXE

/*Command line configuration.*/
#define CONFIG_CMDLINE_EDITING
#define CONFIG_AUTO_COMPLETE

#define CONFIG_SUPPORT_RAW_INITRD

/* Miscellaneous configurable options */
#define CONFIG_SYS_CBSIZE	2048/* Console I/O Buffer Size      */
#define CONFIG_SYS_PBSIZE	(CONFIG_SYS_CBSIZE + sizeof(CONFIG_SYS_PROMPT) + 16)
#define CONFIG_SYS_BARGSIZE CONFIG_SYS_CBSIZE

/* Use the HUSH parser */
#define CONFIG_SYS_PROMPT_HUSH_PS2 "> "

#define CONFIG_ENV_VARS_UBOOT_CONFIG
#define CONFIG_ENV_OVERWRITE	/* Allow to overwrite the u-boot environment variables */

#define CONFIG_LMB

/* FDT support */
#define CONFIG_DISPLAY_BOARDINFO_LATE


/* architecture dependent code */
#define CONFIG_SYS_HZ   1000

/* Boot Argument Buffer Size */
#define CONFIG_SYS_MAXARGS      32      /* max number of command args */
#define CONFIG_SYS_LONGHELP


#undef CONFIG_BOOTM_NETBSD

/* Initial memory map for Linux */
#define CONFIG_SYS_BOOTMAPSZ 0x08000000

#endif /* __PLNX_CONFIG_H */
