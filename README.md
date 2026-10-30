# MuseScore for Mere Mortals

Most music on a computer is sound: recordings,
streams, audio files. **MuseScore** works with the
other kind — music as *writing*. It is a program
for **notation**: you put notes on staves, and it
keeps them as a **score** you can print for real
musicians to play, play back through speakers to
check your work, rearrange, transpose, and hand to
other software. The score is the document; the
sound and the printed page are both things the
score can produce.

This guide explains how a MuseScore score is put
together, how to install the program (its current
name is **MuseScore Studio**), and how to make
your first score. Then it does the thing this
series does: it takes the file formats apart. The
lab behind this guide fed one small hand-written
melody through every door MuseScore offers —
its own formats, print, images, MIDI, audio — and
**measured what came out**: page counts, note
counts, pitches, decibel levels. A notation
program's failures are quiet ones (a wrong octave
looks fine on screen), so measurement is not a
luxury here.

The lab ran the real thing: **MuseScore Studio
4.7.6**, the official AppImage, extracted and run
unmodified on a small Linux machine with no
speakers, no ears and no music paper. Its fixture
is an eight-bar melody the lab wrote by hand as
MusicXML — 29 notes, a repeated section, a key
change halfway — chosen because every one of those
features leaves a measurable trace in the output.
Against it the lab converted formats both ways,
printed to PDF and checked the page, rendered a
PNG at a measured 1200 DPI, parsed the exported
MIDI note by note with its own reader, rendered
audio and proved it was not silence by measuring
its levels, transposed the score and verified
every single pitch moved, and found the places
where the command line quietly does nothing —
which are in this guide too, labelled.

What the lab could not do, it did not fake. It
could not listen, so it never claims one playback
sound is *better* than another; it reports which
sounds were in the file and which were not. It
opened the graphical program once, under a
virtual screen, and photographed it — but it
entered no notes by hand, so the note-entry
craft in chapter 4 is taught from the program's
own documentation and labelled as such.
`criteria.md` keeps the full ledger of what was
run and what was only read.

## What this guide covers

- [**What MuseScore Is**](what-musescore-is.md) —
  notation versus audio, who writes scores and
  why, and where MuseScore sits among the tools
- [**The Moving Parts**](the-moving-parts.md) —
  the program, the score document, staves and
  voices, palettes, the mixer, and the two kinds
  of playback sound
- [**Installing MuseScore**](installing-musescore.md) —
  the official downloads, the AppImage on Linux
  and how this lab ran it without installing
  anything, MuseHub, and checking your version
- [**Your First Score**](your-first-score.md) —
  starting a score, entering and editing notes,
  and the habits that keep a score healthy
- [**The File Formats**](the-file-formats.md) —
  .mscz and .mscx taken apart, MusicXML as the
  travelling format, MIDI's narrower promise,
  and importing other programs' files
- [**Layout and Parts**](layout-and-parts.md) —
  making pages musicians can read, generating
  each player's part, and the transposing-
  instrument truth every arranger learns once
- [**Playback and Sound**](playback-and-sound.md) —
  hearing your score, the bundled MS Basic
  sounds, MuseSounds, and what playback can
  and cannot tell you
- [**Exporting, Printing and Sharing**](exporting-and-sharing.md) —
  PDF for print, images, audio files, and
  musescore.com with its commercial side
  stated plainly
- [**The Command Line**](the-command-line.md) —
  converting scores without opening the program:
  what the lab verified, the transpose that
  worked, and the options that silently didn't
- [**Recipes**](recipes.md) — convert a folder
  of scores, render practice audio, print a
  set of parts, and check a score's contents
  without opening it
- [**The Neighbours**](the-neighbours.md) —
  the audio editors and DAWs, LilyPond's
  text-driven engraving, and the commercial
  notation programs: what each does that
  MuseScore doesn't, and vice versa
- [**Limits**](limits.md) — parts that must be
  created before they can be automated, a
  command line with silent corners, playback
  that proves notes but not music, and more
- [**Troubleshooting**](troubleshooting.md) —
  the export that "didn't happen" because it
  was written under a page-numbered name, the
  crash after the first job, the empty sound,
  and the traps this guide's lab fell into
- [**Glossary**](glossary.md) — the terms,
  collected in one place

## What it doesn't cover

Music theory. This guide assumes you can read
a staff about as well as you can read a map —
it explains the program, not the language the
program writes in. It also doesn't teach
engraving as an art: it shows the controls
that change how a score looks and the checks
that catch a broken one, and leaves taste to
you and your players. Orchestration, arranging
and composition are crafts with their own
books. Scores from the internet raise
copyright questions this guide names once, in
chapter 1, and then leaves alone: a score
being downloadable does not make it yours to
perform or sell.

## How to use this guide

Read chapter 1 for the model and chapter 2
before installing anything — knowing which
part holds what (in particular, that a score
file is a small archive you can open) turns
later confusion into a named problem. Chapters
3 and 4 get you a program and a first score.
Chapter 5 is the one to read slowly: formats
decide what survives the trip to another
program or another decade. The lab's fixture
and transcripts live in `musescore-lab/`, and
its MIDI reader is `musescore-lab/check-midi.py`
— run it on your own exports when a conversion
matters and you want to know, not hope.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Ardour for Mere Mortals](https://paulsullivan33-dev.github.io/ardour-for-mere-mortals/)
- [Audacity for Mere Mortals](https://paulsullivan33-dev.github.io/audacity-for-mere-mortals/)
- [ffmpeg for Mere Mortals](https://paulsullivan33-dev.github.io/ffmpeg-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/musescore-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/musescore-for-mere-mortals/blob/main/LICENSE-CODE).
