# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set i_wb_cyc high
    dut.uio_in[0].value = 1
    # Set i_wb_stb high
    dut.uio_in[1].value = 1
    # Set i_wb_we high
    dut.uio_in[2].value = 1
    # Set i_wb_addr[2:0] to 3'b100 
    dut.uio_in[3].value = 0
    dut.uio_in[4].value = 0
    dut.uio_in[5].value = 1
    # Set i_wb_data to 8'b00000001
    dut.ui_in.value = 1

    # Wait one clock cycle
    await ClockCycles(dut.clk, 1)

    # Set i_wb_cyc low
    dut.uio_in[0].value = 0
    # Set i_wb_stb low 
    dut.uio_in[1].value = 0
    # Set i_wb_we low
    dut.uio_in[2].value = 0

    # Load seed into memory byte zero
    
    await ClockCycles(dut.clk, 1)

    dut.uio_in[0].value = 1
    dut.uio_in[1].value = 1
    dut.uio_in[2].value = 1

    # Set i_wb_addr[2:0] to 3'b000
    dut.uio_in[3].value = 0
    dut.uio_in[4].value = 0
    dut.uio_in[5].value = 0

    # Set i_wb_data to 8'b00010101
    dut.ui_in.value = 21
    
    await ClockCycles(dut.clk, 1)
    
    # Set i_wb_cyc low
    dut.uio_in[0].value = 0
    # Set i_wb_stb low 
    dut.uio_in[1].value = 0
    # Set i_wb_we low
    dut.uio_in[2].value = 0
    
    # Load seed into memory byte one
    
    await ClockCycles(dut.clk, 1)

    dut.uio_in[0].value = 1
    dut.uio_in[1].value = 1
    dut.uio_in[2].value = 1

    # Set i_wb_addr[2:0] to 3'b001
    dut.uio_in[3].value = 1
    dut.uio_in[4].value = 0
    dut.uio_in[5].value = 0

    # Set i_wb_data to 8'b00001111
    dut.ui_in.value = 15
    
    await ClockCycles(dut.clk, 1)
    
    # Set i_wb_cyc low
    dut.uio_in[0].value = 0
    # Set i_wb_stb low 
    dut.uio_in[1].value = 0
    # Set i_wb_we low
    dut.uio_in[2].value = 0
    
    # Load seed into memory byte two
    
    await ClockCycles(dut.clk, 1)

    dut.uio_in[0].value = 1
    dut.uio_in[1].value = 1
    dut.uio_in[2].value = 1

    # Set i_wb_addr[2:0] to 3'b010
    dut.uio_in[3].value = 0
    dut.uio_in[4].value = 1
    dut.uio_in[5].value = 0

    # Set i_wb_data to 8'b00100100
    dut.ui_in.value = 36
    
    await ClockCycles(dut.clk, 1)
    
    # Set i_wb_cyc low
    dut.uio_in[0].value = 0
    # Set i_wb_stb low 
    dut.uio_in[1].value = 0
    # Set i_wb_we low
    dut.uio_in[2].value = 0
    
    # Load seed into memory byte three
    
    await ClockCycles(dut.clk, 1)

    dut.uio_in[0].value = 1
    dut.uio_in[1].value = 1
    dut.uio_in[2].value = 1

    # Set i_wb_addr[2:0] to 3'b011
    dut.uio_in[3].value = 1
    dut.uio_in[4].value = 1
    dut.uio_in[5].value = 0

    # Set i_wb_data to 8'b01100100
    dut.ui_in.value = 21
    
    await ClockCycles(dut.clk, 1)
    
    # Set i_wb_cyc low
    dut.uio_in[0].value = 0
    # Set i_wb_stb low 
    dut.uio_in[1].value = 0
    # Set i_wb_we low
    dut.uio_in[2].value = 0
    
    # Load seed into LFSR
    
    await ClockCycles(dut.clk, 1)

    dut.uio_in[0].value = 1
    dut.uio_in[1].value = 1
    dut.uio_in[2].value = 1

    # Set i_wb_addr[2:0] to 3'b100
    dut.uio_in[3].value = 0
    dut.uio_in[4].value = 0
    dut.uio_in[5].value = 1

    # Set i_wb_data to 8'b01100100
    dut.ui_in.value = 2
    
    await ClockCycles(dut.clk, 1)
    
    # Set i_wb_cyc low
    dut.uio_in[0].value = 0
    # Set i_wb_stb low 
    dut.uio_in[1].value = 0
    # Set i_wb_we low
    dut.uio_in[2].value = 0
    
    # Load seed into LFSR and exit reset state
    
    await ClockCycles(dut.clk, 1)

    dut.uio_in[0].value = 1
    dut.uio_in[1].value = 1
    dut.uio_in[2].value = 1

    # Set i_wb_addr[2:0] to 3'b100
    dut.uio_in[3].value = 0
    dut.uio_in[4].value = 0
    dut.uio_in[5].value = 1

    # Set i_wb_data to 8'b00000000
    dut.ui_in.value = 0
    
    await ClockCycles(dut.clk, 1)
    
    # Set i_wb_cyc low
    dut.uio_in[0].value = 0
    # Set i_wb_stb low 
    dut.uio_in[1].value = 0
    # Set i_wb_we low
    dut.uio_in[2].value = 0
    
    await ClockCycles(dut.clk, 1)
    
    # Set i_wb_cyc high
    dut.uio_in[0].value = 1
    # Set i_wb_stb high 
    dut.uio_in[1].value = 1
    # Set i_wb_we low
    dut.uio_in[2].value = 0

    await ClockCycles(dut.clk, 1) 
    
    await ClockCycles(dut.clk, 1)  
    
    assert dut.uo_out[1].value == 0
    
    await ClockCycles(dut.clk, 1) 
    
    assert dut.uo_out[1].value == 1
    
    await ClockCycles(dut.clk, 1) 
    
    assert dut.uo_out[1].value == 0
    
    await ClockCycles(dut.clk, 1) 
    
    assert dut.uo_out[1].value == 0
    
    await ClockCycles(dut.clk, 1) 
    
    assert dut.uo_out[1].value == 0
    
    await ClockCycles(dut.clk, 1) 
    
    assert dut.uo_out[1].value == 1
    
    await ClockCycles(dut.clk, 1) 
    
    assert dut.uo_out[1].value == 1
    
    await ClockCycles(dut.clk, 1) 
    
    assert dut.uo_out[1].value == 0 
    
    await ClockCycles(dut.clk, 1) 
    
    assert dut.uo_out[1].value == 0
    
    await ClockCycles(dut.clk, 1) 
    
    assert dut.uo_out[1].value == 1
    
    await ClockCycles(dut.clk, 1) 


# ---------------------------------------------------------------------------
# A short, self-checking test of the LFSR sequence.
#
# The LFSR's feedback is ff[31] ^ ff[6] ^ ff[5] ^ ff[1], so in the output stream
# every bit equals the XOR of the bits 2, 6, 7 and 32 places before it.
# The test loads a seed, reads 300 bits, and checks that rule for every bit.

async def bus_write(dut, addr, data):
    """One Wishbone write: cyc = stb = we = 1 for one clock edge, then idle."""
    dut.ui_in.value = data
    dut.uio_in.value = 0b111 | (addr << 3)
    await ClockCycles(dut.clk, 1)
    dut.uio_in.value = 0
    await ClockCycles(dut.clk, 1)


async def read_bits(dut, seed, count):
    """Load a seed, run the LFSR, and read `count` bits from uo_out[1]."""
    await bus_write(dut, 4, 1)                      # hold the LFSR in reset
    for i in range(4):
        await bus_write(dut, i, (seed >> (8 * i)) & 0xFF)
    await bus_write(dut, 4, 2)                      # load the seed
    await bus_write(dut, 4, 0)                      # run
    dut.uio_in.value = 0b011                        # read cycle: cyc = stb = 1, we = 0
    await ClockCycles(dut.clk, 2)
    bits = []
    for _ in range(count):
        await ClockCycles(dut.clk, 1)
        bits.append((int(dut.uo_out.value) >> 1) & 1)   # uo_out[1]
    return bits


@cocotb.test()
async def test_lfsr_sequence(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="us").start())
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1

    bits = await read_bits(dut, 0x87654321, 300)
    for n in range(32, len(bits)):
        expected = bits[n - 2] ^ bits[n - 6] ^ bits[n - 7] ^ bits[n - 32]
        assert bits[n] == expected, f"bit {n} breaks the LFSR rule"
    assert 100 < sum(bits) < 200, "the output should be about half ones"

    # A seed of 0 is the one state an LFSR can never leave: it outputs only zeros.
    bits = await read_bits(dut, 0, 50)
    assert sum(bits) == 0, "seed 0 should give only zeros"
