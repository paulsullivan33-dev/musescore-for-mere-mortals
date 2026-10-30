# The Moving Parts

**The outcome:** you can name the pieces a
MuseScore score is made of — and say which file
holds what — so that when something looks or
sounds wrong you know which part to blame.

## The score document

Everything revolves around one document: the
**score**. A score holds one or more **parts**
(in the musician's sense: the flute's music,
the piano's music), each part has one or more
**staves**, and each staff holds **measures**
of notes, rests, chords and markings. A staff
can carry up to four **voices** — independent
rhythmic lines, shown in different colours
while editing so you can tell them apart.

The score also holds things that are not notes:
the title and composer text, the page layout
(page size, margins, staff size), the playback
settings, and — once you create them — the
extracted **parts** in the printer's sense:
one document per player, generated from the
same music. Chapter 6 is about those; the
distinction matters, because MuseScore uses
"part" for both the instrument's line in the
score and the sheet that player reads.

On disk the score is a `.mscz` file, and it is
not a black box: it is a small zip archive.
Chapter 5 opens one up. The short version is
worth having now: inside is the music as XML
text (`.mscx`), a style file, a thumbnail
image, and small settings files. You can look.
Nothing in this guide asks you to edit those
files by hand — but knowing they are readable
turns "the file is corrupted" from a mystery
into a checkable claim.

## The program window

The lab opened the real program once, under a
virtual screen, and photographed it
(`musescore-lab/gui-first-run.png`). The layout
it shows is the standard one:

- The **score view** in the middle: the page,
  as it will print.
- The **toolbar** across the top: note values,
  accidentals, articulations — the writing tools.
- **Palettes** on the left: the warehouse of
  everything that can be added to a score —
  clefs, key signatures, time signatures, tempo
  marks, dynamics, articulations, text, repeats
  and jumps, barlines, layout elements. Most
  notation work is "find it in Palettes, put it
  on the score."
- **Layout** and **Properties** panels beside
  them: Properties is where a selected element's
  details are adjusted.
- The **Parts** and **Mixer** buttons at the
  top: Parts opens the dialog that creates each
  player's sheet; the Mixer holds a volume,
  pan and sound for every instrument.
- A status bar with two switches worth knowing
  on day one: **Concert pitch** (chapter 6
  explains the transposing-instrument problem
  it solves) and the view and zoom controls.

A first-run **welcome wizard** offers a theme
and a tour before any of this; it is harmless
and skippable, and the screenshot in the lab
shows it exactly as a new user meets it.

## The playback engine

Press play and MuseScore performs the score
itself. Two things decide what you hear:

- The **sound library**. The standard install
  carries one bundled library, **MS Basic** —
  a soundfont (a file of sampled instrument
  sounds, `.sf3`) covering the usual orchestra
  and band instruments decently and without
  ceremony. The lab verified from the
  AppImage's own contents that exactly one
  soundfont ships in it, and the score it
  exported recorded `"activeSoundProfile":
  "MuseScore Basic"` in its settings.
- **MuseSounds**, the newer, larger sampled
  libraries — one per instrument family, more
  expressive, more disk. They are *not* in the
  program download; they arrive through
  **MuseHub**, the companion app, as separate
  downloads. Chapter 7 covers the difference
  and the honest limits of judging sounds you
  cannot hear — this lab couldn't, and says so.

Playback settings (which sound each staff
uses, volumes, effects) live in the score's
audio settings and the Mixer, *not* in the
notes. The same score can be silent, decent
or deafening without a single pitch changing.

## The conversion engine

Underneath the window sits a second program:
the **converter**, driven from the command
line, which opens a score and writes it out
as something else — another score format, a
PDF, an image, a MIDI file, audio — without
the window ever opening. Chapter 9 is devoted
to it because this guide's lab lived there:
it is the scriptable, measurable face of
MuseScore, and the one a reader can use to
convert a whole folder of scores while making
tea. It has sharp edges the lab found and
named; they are in chapters 9 and 13, not
hidden.
