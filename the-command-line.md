# The Command Line

**The outcome:** you can convert scores
without opening the program — singly, in a
folder, transposed — and you know which
options this lab verified, which it found
do nothing, and how to tell the difference
on your own machine.

The same binary that runs the window is a
converter. Its shape is:

```sh
mscore4portable -o <output-file> [options] <input-score>
```

The output format comes from the output
file's extension: `.pdf`, `.png`, `.svg`,
`.mp3`, `.wav`, `.mid`, `.mscz`, `.mscx`,
`.musicxml` and friends. Everything in this
chapter was run by the lab on MuseScore
4.7.6, and the full `--help` it worked from
is `musescore-lab/transcripts/t02-help.txt`.
On your system the binary may be called
`mscore`, `musescore` or an AppImage path;
the options are the same.

## The conversions, verified

From the lab's fixture (chapter 5 has the
measurements behind each line):

```sh
mscore4portable -o first-light.mscz first-light.musicxml
mscore4portable -o first-light.pdf  first-light.musicxml
mscore4portable -o first-light.mp3  first-light.musicxml
mscore4portable -o first-light.mid  first-light.musicxml
```

All succeeded from a MusicXML input; a
`.mscz` or `.mscx` input behaves the same.
Knobs the lab measured:

- `-b <kbps>` sets MP3 bitrate; the default
  measured was **128 kbps**.
- `-r <DPI>` sets image resolution; the
  default measured was **1200 DPI** (a
  9924 × 14028 PNG of an A4 page). Add
  `-T <pixels>` to trim image margins.
- Image exports (PNG, SVG) are written
  **one file per page**, named
  `name-1.png`, `name-2.png`, … — whether
  you asked for the suffix or not.

## Repeats: --unroll-repeats

Scores written with repeat barlines export
to MIDI and audio *with the repeats played*
— that is the default and usually what you
want. For score-format outputs, the flag
**`--unroll-repeats`** writes the repeated
bars out in full: the lab's 8-measure
fixture became a 12-measure `.mscx`, the
repeat pass visible as ordinary measures.
Unroll when the destination (a simpler
program, a human editor, a diff) is better
served by the long form.

One oddity, reported as found: the lab's
two MIDI exports (with and without the
flag) were identical in every note, but
differed in the instrument's program
number — 73 in one file, 72 in the other.
Nothing asked for that. It costs nothing
to know that converters have fingerprints
like this; chapter 10 shows the checking
habit that catches them.

## Transposing: the option that worked, and the one that didn't

`--transpose` takes a small JSON document
describing the transposition. The lab tried
several spellings against its fixture,
because the difference between them is the
difference between music and silence:

**By key — verified working:**

```sh
mscore4portable -o up-two.mscx \
  --transpose '{"mode": "by_key", "direction": "up",
                "targetKey": 2, "transposeKeySignatures": true}' \
  first-light.mscz
```

`targetKey` is the destination key's place
on the circle of fifths: 0 = C, 1 = G,
2 = D, −1 = F, and so on. The lab verified
the result rather than trusting it: **all
29 written pitches rose exactly 2
semitones**, the key signatures became D
major and A major (from C and G), and the
one F sharp in the piece became G sharp —
spelled correctly, not just shifted. This
is the way to make the "same song, singer's
key" copy from a script.

**By interval — verified not working (in
4.7.6):** the form `--transpose '{"mode":
"by_interval", "direction": "up",
"transposeInterval": 2}'` is *accepted* —
exit code 0, output file written — and the
output is **not transposed**. Every pitch
matches the original. Other spellings
(`byInterval`, `chromatically`) are
rejected outright with exit code 31 and
no output at all, which is at least honest.
The interval form may work in other
versions; on this one, treat any silent
converter option as a claim to be checked
(chapter 10's checker is the tool), and
use `by_key` for scripted key changes.

## Reading a score without opening it

**`--score-meta`** prints a JSON summary —
title, composer, duration with repeats
played (the fixture reported 29 seconds),
file version, whether it has lyrics or
harmony symbols. It is the fastest honest
answer to "what is in this file?" across a
folder of scores you didn't write.

## The parts flags: a measured dead end

`-P` ("export score and parts" to PDF) and
`--score-parts` look like the automation
for chapter 6. On a score whose parts have
not yet been created in the GUI, the lab
found they exit 0 and write **nothing at
all** — no file, no warning. The transcript
is `musescore-lab/transcripts/t06-parts-and-meta.txt`.
If your score already has parts (created in
the window), these flags have something to
operate on; if it hasn't, no script will
conjure them. Create parts interactively,
once.

## Job files: a measured crash

`-j job.json` accepts a JSON list of
`{"in": ..., "out": ...}` conversions in
one run. The lab's single-entry job worked
and produced byte-identical sizes to the
direct conversion. Its two-entry job
**wrote the first output and then crashed**
— exit code 139, a segfault — on two
separate attempts, identically
(`musescore-lab/transcripts/t08-jobs-and-svg.txt`).
Until that is different, batch work belongs
in a shell loop over single conversions —
which is the next chapter's first recipe.
