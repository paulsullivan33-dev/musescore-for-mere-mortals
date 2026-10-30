# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's fixture is one short invented melody, nothing
   personal.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 12 names what the tool —
   and this guide's lab — cannot do: parts must exist before
   the command line can print them, the AppImage carries one
   basic soundfont and nothing grander, one of the transpose
   modes silently does nothing in the taught version,
   multi-entry job files crash, and nothing here was judged
   by ear.
8. **The ethics rule is in the text, early.** MuseScore raises
   no interception question; its own line is drawn in chapter 1
   and the sharing chapter instead — the program is free
   software and a score you write is yours, but uploading to
   musescore.com is for music you have the right to share, and
   the site's account and subscription side is stated plainly,
   in chapter 8, before any reader is pointed at it.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a small shared Ubuntu sandbox with no
sound device and no FUSE. The guide teaches **MuseScore Studio
4.7.6** — the current release at build time (GitHub release
v4.7.6, dated 2026-10-26) — so there is no version gap to
disclose; what there is instead is an extraction step, below.

**How the software was obtained, disclosed in full:** the
official x86_64 AppImage (`MuseScore-Studio-4.7.6.261022093-x86_64.AppImage`,
192,616,952 bytes) was downloaded from the project's own GitHub
release, and its SHA-256
(`5fcbd1f292270eca5c3867d56b767c31a173a155216a415f5caee22553f8e7a6`)
matches the release's published `checksums.sha256.txt` exactly
(transcript `t00`). The sandbox has no FUSE, so the AppImage
could not run as an AppImage; it was unpacked with
`--appimage-extract` and the guide's commands run the extracted
program, `usr/bin/mscore4portable`, from the tree — the same
binary the AppImage would have run. On a normal machine the
AppImage runs as-is and the commands are identical. The program
also needs a display even for file conversion: every conversion
below ran under `xvfb-run` (the `offscreen` Qt platform fails
with an xcb plugin error, recorded in chapter 13).

**The lab had no speakers and no way to listen.** Every claim
about audio is therefore a measurement — durations, sample-level
peak and RMS levels from ffmpeg's `astats` — and the guide never
grades how the playback *sounds*.

The fixture is the guide's own: `musescore-lab/first-light.musicxml`,
a short melody written by hand as MusicXML — 8 bars, 29 notes,
a repeat around bars 1–4, a key change from C major to G major
at bar 5, a stated tempo of 100 BPM, titled "First Light — a
short study melody". The MIDI measuring script is
`musescore-lab/check-midi.py`, written for this lab in pure
Python (no libraries) so a reader can rerun it anywhere.

Run for real, with transcripts as evidence (`musescore-lab/`):

- Download, checksum verification against the release's own
  checksums file, extraction, and `--version` reporting
  `MuseScore4 4.7.6` (`t00`, `t01`); the full `--help` surface
  read before any flag was taught — every flag in chapter 9
  comes from it (`t02`).
- Conversions from the MusicXML fixture, each with the same
  command shape (`t03`): `.mscz` (30,847 bytes; unzipped and
  inventoried — the `.mscx` inside, a style file, a thumbnail,
  settings files), standalone `.mscx` (13,809 bytes), PDF
  (37,645 bytes; `pdfinfo` proves 1 page at A4, 595×842 pts),
  PNG (exported page-numbered as `first-light-1.png`,
  9924×14028 pixels — about 1200 DPI at default settings).
- Audio exports measured, not listened to (`t03`): WAV is
  `pcm_f32le`, 44.1 kHz stereo, 31.80 s, peak −17.48 dB,
  RMS −28.81 dB — real signal, not silence; MP3 is 128 kbps
  by default, 31.87 s, levels within a decibel of the WAV.
  The score's written length is 19.2 s at its stated tempo,
  28.8 s with the repeat played; the files run about 3 s
  longer, the instrument's release tail.
- MIDI parsed back with the lab's own script (`t04`): format 1,
  one track named "Flute", 480 ticks per quarter, tempo stated
  as 100 BPM, **44 notes** — the 29 written plus the repeated
  bars, because MIDI export plays repeats — ending at tick
  22943, notes held 455 of each 480 ticks.
- `--unroll-repeats` (`t05`): the `.mscx` grows from 8 to 12
  `<Measure>` elements while the notes in the two MIDI exports
  are identical. One oddity is reported as found, unexplained:
  the plain export's program change is 73, the unrolled
  export's is 72.
- Transpose (`t05`): `--transpose` in `by_key` mode works and
  is proven note by note — all 29 written pitches rise exactly
  two semitones, both key signatures move up the circle of
  fifths (C→D, then G→A), and the transposed MIDI starts on D4.
  The same command in `by_interval` mode exits 0 and changes
  nothing at all; the mode spellings `byInterval` and
  `chromatically` are rejected with exit 31. Chapter 9 teaches
  the working route and prints the finding plainly.
- `--score-meta` returning the score's own JSON — composer,
  a duration of 29 s with repeats counted, file version 470,
  no lyrics, no harmonies (`t06`).
- The graphical program launched once under a virtual display
  with the converted score open; the screenshot is kept at
  `musescore-lab/gui-first-run.png` and shows the typeset
  score, the first-run welcome wizard, the Palettes panel and
  the Parts and Mixer buttons (`t07`). The GUI was used for
  viewing; it was not clicked through.
- Job files (`t08`): a single-entry `-j` job converts cleanly
  (its MP3 is byte-for-byte the same size as the direct
  export); SVG export works and is page-numbered like PNG.

Boundaries hit and kept verbatim:

- **Parts cannot be conjured from the command line.** The
  imported score contains no `<Excerpt>` elements; `-P` and
  `--score-parts` exit 0 and write nothing, and
  `--score-parts-pdf` prints nothing usable (`t06`). Parts
  are created first in the GUI's Parts dialog — chapter 6
  teaches exactly that order, with this transcript as the
  evidence for why.
- **A two-entry job file segfaults** (exit 139) after writing
  its first output, reproduced on two separate attempts
  (`t08`). Chapter 10's batch recipe is therefore a shell
  loop over single conversions, and says why.
- **The bundled sound is one basic soundfont.** The AppImage
  carries exactly one, `MS Basic.sf3`, and the exported
  score's own settings name the active profile "MuseScore
  Basic" (`t03`). Chapter 7 says plainly that this is a
  proof-listening sound, not a performance one.
- One self-inflicted trap is recorded in chapter 13:
  `pkill -f musescore` matched the invoking shell's own
  command line and killed the lab's shell instead of the
  program. The chapter teaches matching on the exact path or
  a recorded PID.

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- Writing music in the GUI: note entry by mouse, keyboard or
  MIDI keyboard, the Palettes and Inspector click-paths, and
  creating parts in the Parts dialog. The program was opened
  and screenshotted; no clicking was automated.
- Installing on Windows and macOS, MuseScore Hub, and the
  distribution package routes — chapter 3 describes the
  landscape; only the Linux AppImage route was run.
- MuseSounds and any sound library beyond the bundled
  `MS Basic.sf3`: named, explained, never downloaded here.
- musescore.com accounts, uploading, and the subscription
  side: described from the site's public pages, not used.
- All judgement by ear — playback quality, whether one
  soundfont flatters a score more than another.
- Transposing-instrument parts for a real band (the clarinet
  and trumpet truth in chapter 6 is standard practice,
  explained; the lab's fixture is a single flute line).
- The neighbour tools of chapter 11 — characterised, not run
  or benchmarked here (Ardour, Audacity and ffmpeg have their
  own guides in this series).

Fixtures are this guide's own and deliberately generic: one
invented eight-bar melody with an invented title and the
byline "The Guide's Lab". No real compositions, names,
organisations or events.
