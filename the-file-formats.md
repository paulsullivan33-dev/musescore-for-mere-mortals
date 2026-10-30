# The File Formats

**The outcome:** you know what each format
keeps and what it throws away, and you can
open an `.mscz` yourself and read what's
inside.

Formats decide what survives: a trip to
another program, to a printer, to a musician
with different software, to yourself in ten
years. MuseScore speaks several. This
chapter is the map, and every claim in it
was measured by the lab on one melody
(`musescore-lab/first-light.musicxml`).

## The native pair: .mscz and .mscx

**`.mscz`** is the working format — what
Save writes. It is not a private binary
blob. It is a **zip archive**, and you can
list its contents with any archive tool:

```text
score_style.mss          the score's style settings
first-light.mscx         the music itself, as XML text
Thumbnails/thumbnail.png a preview image
audiosettings.json       the playback setup, including
                         "activeSoundProfile": "MuseScore Basic"
viewsettings.json        how the score was last viewed
META-INF/container.xml   the archive's table of contents
```

(The lab's listing is in
`musescore-lab/transcripts/t03-conversions.txt`.)

**`.mscx`** is that inner XML, uncompressed —
the same document without the envelope. It is
the form to use when you want text tools on
your music: it can be diffed, grepped, and
kept in version control, where a zipped
`.mscz` diffs as noise. Everything in
`.mscz` beyond the `.mscx` is presentation
and playback state; the notes live in the XML.

Practical rule: **work and archive in
`.mscz`** (or `.mscx` if you live in git),
and treat every other format as an *export* —
a view of the score for a particular purpose,
not the score itself.

## MusicXML: the travelling format

**MusicXML** (`.musicxml`, `.xml`, or zipped
as `.mxl`) is the notation world's interchange
standard, maintained by the W3C music notation
group and read by essentially every notation
program: MuseScore, Dorico, Finale's
successors, Sibelius, and dozens of smaller
tools, plus this guide's lab, which wrote its
fixture as MusicXML by hand precisely because
the format is documented well enough to write
by hand.

What travels in MusicXML: pitches, rhythms,
staves, voices, key and time signatures,
dynamics, articulations, lyrics, layout hints.
What does not travel perfectly: the fine
details of *MuseScore's* layout and playback
settings, and program-specific features with
no standard spelling. The rule for
collaboration is simple: **send MusicXML when
the other person uses something else; expect
to tidy the layout on arrival; keep your
`.mscz` as the original.**

Import runs the other way too — MuseScore
opens MusicXML and takes its best, usually
very good, reading of it. Old notation in
other programs' native formats is a different
story: see "importing" below.

## MIDI: narrower, and honest about it

A **MIDI file** (`.mid`) is a performance
sketch: note on, note off, this loud, this
instrument number, at this tempo. It has no
spelling (F sharp and G flat are the same
number), no voices as notation means them,
no layout, no lyrics worth the name. What it
keeps, it keeps precisely. The lab parsed
its export byte by byte with its own reader
(`musescore-lab/check-midi.py`); the export
of the fixture reported:

- 44 notes — the 29 written notes with bars
  1–4's 15 played twice, because **MIDI
  export performs the repeats**;
- tempo 100 BPM, stated twice (once per pass
  through the repeated section);
- one program change, naming the instrument
  by General MIDI number;
- note lengths of 455 ticks against a
  480-tick quarter: exported notes are
  slightly detached, as a player would play
  them, not mathematically butt-jointed.

Use MIDI to move a *performance-shaped*
sketch into a DAW (chapter 11) or a keyboard.
Never use it as the only copy of a score:
too much of the writing is gone.

## Importing other programs' files

MuseScore imports, beyond MusicXML and MIDI:
**Guitar Pro** files (`.gp`, `.gp5`, `.gpx`
and family — tablature lands as notation
plus a tab staff), **Capella**, **Muse
Score's own older formats** (scores from
MuseScore 2 and 3 open and are migrated;
the migration is good and still worth
checking bar by bar on anything precious),
and a few niche formats listed in the Open
dialog. Finale's and Sibelius's *native*
files are not importable — the way out of
those programs is their MusicXML export,
which is why the travelling format matters.

One import setting worth knowing exists:
MuseScore's MIDI import *guesses* notation
from performance data (quantising timing,
guessing voices and spelling). Its guesses
are respectable, not authoritative; an
imported MIDI file is a draft to edit, not
a score to print.

## The one-paragraph summary

`.mscz` is home. MusicXML is the passport.
MIDI is a postcard of how it sounded. PDF
(next chapters) is the printed page. Keep
the home copy, and no journey can lose the
music.
