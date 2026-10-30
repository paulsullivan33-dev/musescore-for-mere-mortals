#!/usr/bin/env python3
"""Read a Standard MIDI File and report what is actually in it:
format, ticks per quarter note, tempo map, program changes, and
every note (pitch name, start, duration in ticks).

Pure standard library — a MIDI file is a documented byte format,
and this guide's lab rule is that claims get measured, not assumed.

Usage: check-midi.py <file.mid>
"""
import struct
import sys

NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def name(pitch):
    return f"{NAMES[pitch % 12]}{pitch // 12 - 1}"


def read_vlq(data, pos):
    value = 0
    while True:
        byte = data[pos]
        pos += 1
        value = (value << 7) | (byte & 0x7F)
        if not byte & 0x80:
            return value, pos


def main(path):
    data = open(path, "rb").read()
    assert data[0:4] == b"MThd", "not a MIDI file"
    fmt, ntracks, division = struct.unpack(">HHH", data[8:14])
    print(f"file: {path}")
    print(f"format: {fmt}, tracks: {ntracks}, ticks per quarter note: {division}")
    pos = 14
    notes = []
    tempos = []
    programs = []
    for _ in range(ntracks):
        assert data[pos:pos + 4] == b"MTrk"
        length = struct.unpack(">I", data[pos + 4:pos + 8])[0]
        end = pos + 8 + length
        pos += 8
        tick = 0
        running = None
        open_notes = {}
        while pos < end:
            delta, pos = read_vlq(data, pos)
            tick += delta
            byte = data[pos]
            if byte & 0x80:
                running = byte
                pos += 1
            status = running
            kind = status & 0xF0
            channel = status & 0x0F
            if status == 0xFF:
                meta = data[pos]
                pos += 1
                mlen, pos = read_vlq(data, pos)
                payload = data[pos:pos + mlen]
                pos += mlen
                if meta == 0x51 and mlen == 3:
                    usec = int.from_bytes(payload, "big")
                    tempos.append((tick, usec, round(60_000_000 / usec, 2)))
                if meta == 0x03:
                    print(f"track name: {payload.decode('utf-8', 'replace')}")
            elif status in (0xF0, 0xF7):
                mlen, pos = read_vlq(data, pos)
                pos += mlen
            elif kind in (0x90, 0x80):
                pitch, velocity = data[pos], data[pos + 1]
                pos += 2
                if kind == 0x90 and velocity > 0:
                    open_notes.setdefault((channel, pitch), []).append(tick)
                else:
                    starts = open_notes.get((channel, pitch), [])
                    if starts:
                        start = starts.pop(0)
                        notes.append((start, tick - start, channel, pitch))
            elif kind == 0xC0:
                programs.append((tick, channel, data[pos]))
                pos += 1
            elif kind == 0xD0:
                pos += 1
            else:
                pos += 2
        pos = end
    for tick, usec, bpm in tempos:
        print(f"tempo at tick {tick}: {usec} us per quarter note = {bpm} BPM")
    for tick, channel, program in programs:
        print(f"program change at tick {tick}, channel {channel + 1}: program {program}")
    notes.sort()
    print(f"notes: {len(notes)}")
    for start, dur, channel, pitch in notes:
        print(f"  tick {start:>6}  len {dur:>5}  ch {channel + 1}  {name(pitch)} (MIDI {pitch})")
    if notes:
        last_end = max(s + d for s, d, _, _ in notes)
        print(f"last note ends at tick {last_end}")


if __name__ == "__main__":
    main(sys.argv[1])
