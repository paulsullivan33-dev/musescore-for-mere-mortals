# Playback and Sound

**The outcome:** you can make a score play,
you know which sounds it is using and how to
get better ones — and you know exactly what a
playback can prove about your writing and
what it cannot.

## What playback is for

Playback is a proofreader that never gets
tired and has no taste. It is superb at:

- **Wrong notes.** A pitch you misread on
  entry sounds wrong immediately.
- **Broken rhythms.** A measure with too
  many beats announces itself.
- **Balance disasters.** The melody buried
  under the accompaniment you wrote too loud
  is audible in a way it is not visible.

It is useless at judging whether the music
is any good, whether a real player can
breathe there, or whether the phrasing marks
you skipped matter. A score played perfectly
by the computer can still be unplayable by
the band. Use playback as the lab used it:
as measurement, not as a listener.

## The sounds you already have: MS Basic

Every install carries **MS Basic**, one
soundfont (samples of real instruments, in a
single `.sf3` file) covering the standard
orchestra, band and common instruments. The
lab verified this from the inside: the
AppImage contains exactly one soundfont
(`share/mscore4portable-4.7/sound/MS Basic.sf3`),
and a score exported by the converter
recorded `"activeSoundProfile": "MuseScore
Basic"` in its saved audio settings. MS Basic
is the honest workhorse: every instrument
recognisable, none of them beautiful, all of
them free and present offline.

Each staff's sound is chosen in the **Mixer**
(the button at the top of the window), which
also holds per-staff volume and pan. If a
staff plays with the wrong instrument's
voice — a flute line honking like a reed —
the Mixer is where the mix-up lives, and it
is a playback setting, not a wrong note:
the printed part is unaffected.

## MuseSounds: the bigger library

**MuseSounds** is the newer generation:
separate, larger sample libraries per
instrument family, with more articulations
and expression, published by the MuseScore
project and delivered through **MuseHub**
as free downloads (with some premium
libraries sold alongside). They are *not*
inside the program download — if your
install offers only MS Basic, nothing is
broken; the big library simply hasn't been
fetched yet.

This guide will not tell you MuseSounds
sounds better, because its lab has no ears
and measured nothing of the kind; by every
account of people with ears, it does, by a
lot, and it costs disk space and download
time instead of money for the core set. The
decision is genuinely yours and reversible:
sounds are a playback setting, so changing
libraries never touches the written score.

## Rendering audio to a file

Playback can be frozen into an audio file —
chapter 8 covers exporting in general; the
playback-specific facts the lab measured:

- The render **plays the repeats**: the
  fixture as written is 32 beats at 100 BPM
  = 19.2 s; played with its repeat it is
  48 beats = 28.8 s, and the
  rendered files run 31.8–31.9 s — the extra
  is the last note's release and reverb
  tail, rendered honestly.
- WAV export is 44.1 kHz, 32-bit float —
  editing-grade, and large (11 MB for half
  a minute). MP3 export defaults to 128
  kbps (the `-b` / bitrate option in
  chapter 9) and runs a tenth of the size.
- The rendered fixture was **proved not to
  be silence**, the way this series proves
  things: measured peak −17.5 dB, RMS
  −28.8 dB — a quiet flute at the score's
  written dynamic, present and accounted
  for (`musescore-lab/transcripts/t03-conversions.txt`).

Rendered audio is how you send a score to
someone who reads no notation: a singer
learning a line, a band hearing the new
arrangement on the drive to rehearsal.
Chapter 10's recipes make it a habit.
