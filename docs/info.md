<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

It is a linear feedback shift register random number generator connected to a wishbone bus to allow it to fit within the pin constraints of Tiny Tapeout. 

The LFSR is 32 bits long. Each new bit is `ff[31] ^ ff[6] ^ ff[5] ^ ff[1]`, shifted into bit 0. Its polynomial, x^32 + x^30 + x^26 + x^25 + 1, is primitive, so every nonzero seed gives a sequence that repeats only after 2^32 - 1 = 4,294,967,295 bits. A seed of 0 is the one exception: the LFSR stays at 0 forever.

A bus write happens on a rising edge of `clk` while `cyc`, `stb` and `we` (uio[0], uio[1], uio[2]) are all 1. The address is on uio[5:3] and the data on ui[7:0]:

| Address | Write | Effect |
| --- | --- | --- |
| 0 to 3 | one byte of the seed | address 0 is bits 7 to 0, address 3 is bits 31 to 24 |
| 4 | 1 | hold the LFSR at 0 (reset) |
| 4 | 2 | load the seed into the LFSR |
| 4 | 0 | run |
| 5 to 7 | anything | clear the seed to 0 |

A read cycle (`cyc` = 1, `stb` = 1, `we` = 0) puts a new LFSR bit on uo[1] on every clock edge. uo[2] (ack) goes high one clock after `stb`, and uo[0] (stall) is always 0.

## How to test

The TT07 demoboard is all you need: its RP2040 drives the bus and reads uo[1].

1. Write 1 to address 4 to hold the LFSR in reset. Do this first: `rst_n` does not reset this control register.
2. Write the four seed bytes to addresses 0 to 3. Use any value except 0.
3. Write 2 to address 4 to load the seed, then 0 to address 4 to run.
4. Hold a read cycle (`cyc` = 1, `stb` = 1, `we` = 0) and read one bit from uo[1] after each clock.

The cocotb testbench in test/test.py follows the same steps.

## External hardware

The TT07 demoboard on its own. Its microcontroller applies the startup signals and reads the output.
