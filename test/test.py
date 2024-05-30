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
