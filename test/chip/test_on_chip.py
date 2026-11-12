# Test the real TT07 LFSR chip on the Tiny Tapeout demoboard.
#
# 1. Turn the ui_in DIP switches OFF and unplug any PMODs.
# 2. Copy this file to the board:   mpremote cp test/chip/test_on_chip.py :
# 3. In the board's REPL, where `tt` already exists, run:
#        import test_on_chip
#        test_on_chip.run(tt)
#
# It prints PASS or FAIL for each check, then a summary.
#
# The LFSR's feedback is ff[31] ^ ff[6] ^ ff[5] ^ ff[1], so in the output stream
# every bit equals the XOR of the bits 2, 6, 7 and 32 places before it.

from ttboard.mode import RPMode

MACRO = "tt_um_lfsr"   # this design's top module


def run(tt):
    failures = []

    def check(name, ok, detail):
        print("{}  {}  ({})".format("PASS" if ok else "FAIL", name, detail))
        if not ok:
            failures.append(name)

    def clock(cyc, stb, we, addr, data):
        # Set the bus pins, then give the chip one clock edge.
        tt.uio_in.value = cyc | (stb << 1) | (we << 2) | (addr << 3)
        tt.ui_in.value = data
        tt.clock_project_once()

    def write(addr, data):
        clock(1, 1, 1, addr, data)   # cyc = stb = we = 1: write
        clock(0, 0, 0, 0, data)      # then one idle clock

    def read_bits(seed, count):
        write(4, 1)                                  # hold the LFSR in reset
        for i in range(4):
            write(i, (seed >> (8 * i)) & 0xFF)       # the four seed bytes
        write(4, 2)                                  # load the seed
        write(4, 0)                                  # run
        clock(1, 1, 0, 0, 0)                         # start a read cycle
        bits = []
        acks = 0
        for _ in range(count):
            clock(1, 1, 0, 0, 0)                     # one new bit per clock
            out = int(tt.uo_out.value)
            bits.append((out >> 1) & 1)              # uo_out[1]: the LFSR bit
            acks += (out >> 2) & 1                   # uo_out[2]: ack
        return bits, acks

    # Let the RP2040 drive the chip, and select this design.
    tt.mode = RPMode.ASIC_RP_CONTROL
    getattr(tt.shuttle, MACRO).enable()
    tt.clock_project_stop()
    tt.uio_oe_pico.value = 0b0011_1111   # the RP2040 drives cyc, stb, we and addr
    tt.reset_project(True)
    tt.clock_project_once()
    tt.reset_project(False)

    for seed in (0x87654321, 0x00000001, 0xDEADBEEF):
        bits, acks = read_bits(seed, 1000)
        broken = [n for n in range(32, len(bits))
                  if bits[n] != bits[n - 2] ^ bits[n - 6] ^ bits[n - 7] ^ bits[n - 32]]
        check("seed 0x%08X follows the LFSR rule" % seed, not broken,
              "%d of %d bits break it" % (len(broken), len(bits) - 32))
        check("seed 0x%08X is about half ones" % seed, 400 < sum(bits) < 600,
              "%d ones in %d bits" % (sum(bits), len(bits)))
        check("seed 0x%08X ack stays high while reading" % seed, acks == len(bits),
              "high on %d of %d clocks" % (acks, len(bits)))

    bits, _ = read_bits(0, 200)
    check("seed 0 gives only zeros", sum(bits) == 0, "%d ones in %d bits" % (sum(bits), len(bits)))

    write(4, 1)                       # leave the LFSR in reset
    tt.uio_oe_pico.value = 0          # back to all inputs

    if failures:
        print("%d check(s) FAILED: %s" % (len(failures), ", ".join(failures)))
    else:
        print("ALL PASS")
    return not failures
