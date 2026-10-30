# Recipes

**The outcome:** four jobs readers actually
have, each built only from operations the
lab verified in chapter 9.

Paths below use `mscore4portable`; substitute
your binary's name. Fixtures and the checker
script live in `musescore-lab/`.

## 1. Convert a folder of scores

Every `.mscz` in a folder becomes a PDF
beside it:

```sh
for f in scores/*.mscz; do
  mscore4portable -o "${f%.mscz}.pdf" "$f"
done
```

Why a loop and not a `-j` job file: chapter
9 measured the job-file crash after the
first entry. The loop is one conversion per
process — slower by seconds, immune to one
bad file taking the batch with it, and each
failure leaves the culprit's name in your
terminal. Add `.mp3` to taste by changing
the extension and the output name.

## 2. Practice audio for the whole band

Render an MP3 of a score (and, after
creating them in the GUI, of each part) so
players can rehearse against the whole:

```sh
mscore4portable -o rehearsal/full-band.mp3 -b 192 score.mscz
```

Ideas that cost nothing: also render each
part *with its own line turned up* in the
Mixer (save those as separate scores —
`score-flute-up.mscz` — so the settings are
part of the file), and render one at a
reduced tempo by changing the score's tempo
marking in a copy. A singer learning a line
needs a slow, loud-against-the-band copy
far more than another full-speed one.

## 3. Check what a conversion really did

After any conversion that matters, measure
the output instead of believing the exit
code. For MIDI, the lab's reader prints
every note:

```sh
python3 musescore-lab/check-midi.py exported.mid
```

Note count, pitches, tempo and program,
from the file's own bytes. After a
transpose, compare first notes before and
after (the lab compared *every* pitch,
with a handful of lines of Python over the
`.mscx` XML — the format being text is
what makes that possible). For audio,
`ffprobe` gives duration and format, and
ffmpeg's `astats` filter gives peak and
RMS levels — the difference between
"rendered the piece" and "rendered 30
seconds of silence" is one command, and
silent renders do happen (chapter 13).

## 4. A set of parts for Friday

The honest sequence, using each tool where
it is strong:

1. In the window: open the score, click
   **Parts**, create all parts, and give
   each a once-over for page turns
   (chapter 6).
2. Check one transposing part against the
   concert score (chapter 6's check).
3. Save. The parts now live in the `.mscz`.
4. Print or PDF from the window, choosing
   the parts the rehearsal needs.

The scriptable version of step 4 is the
one thing the converter couldn't do for a
score without pre-made parts (chapter 9),
so the recipe doesn't pretend otherwise:
twenty clicks once, correct paper every
rehearsal after.
