# Troubleshooting

**The outcome:** the failure in front of you
has a name, a cause, and a next step. Each
entry begins with what you see.

## "The export didn't happen — there's no file"

Look for the page number. Image exports are
written one file per page with the number
appended: you asked for `page.png`, the
program wrote `page-1.png` (and `page-2.png`
if there are two pages). The lab "lost" its
first PNG and its first SVG exactly this
way. PDF and audio exports use the name you
gave; images never do.

## "The command said nothing and did nothing"

The converter's failure mode, three times
over in the lab's experience:

- Parts flags on a part-less score: exit 0,
  no file. Create the parts in the window
  first (chapter 6).
- `--transpose` with the interval mode:
  exit 0, file written, *music unchanged*.
  Check the output's first pitches against
  the original (chapter 10's checker), and
  use `by_key` mode, which the lab verified.
- A misspelt transpose mode (`byInterval`,
  `chromatically`) is at least loud about
  it: exit 31, no file. Believe exit codes
  when they're nonzero; verify when they're
  zero.

## "The batch crashed after the first file"

If you used a `-j` job file with more than
one entry: known behaviour in 4.7.6,
reproduced twice by this lab — the first
output is written, then the process dies
(exit 139). Use a shell loop over single
conversions (chapter 10, recipe 1). Your
first output is fine; the rest were never
attempted.

## "Playback is silent"

In order: system volume and the right output
device; then the **Mixer** — a staff can be
muted or faded there while looking innocent
in the score; then the staff's assigned
sound (a staff pointing at a library that
isn't installed plays nothing — reassign it
to MS Basic to test); then, for a *rendered*
file, measure it before blaming your ears:
`ffprobe` for duration, ffmpeg's `astats`
for peak level. A peak of −infinity is a
silent render (usually a sound assignment
problem); a peak like −17 dB is a quiet
piece, and the fix is the score's dynamics
or the mixer's levels, not the exporter.

## "It sounds like the wrong instrument"

Same address as above, different room: the
Mixer holds each staff's sound, and an
import can guess wrong — MIDI imports
especially, where "instrument" is a number
in a table and one export's 73 is another's
72 (the lab's two MIDI exports of one score
differed in exactly that byte). Reassign
the sound in the Mixer; the written notes
were never wrong.

## "The score looks exploded after import"

Imported MusicXML and MIDI arrive with
someone else's layout decisions (or none).
The order of operations that fixes most of
it: check the staff size and page size
(chapter 6) before touching individual
elements; remove stray manual breaks the
source may have baked in; then, in the GUI,
select all and let the program re-lay the
score out. MIDI imports additionally need
their notation guesses edited — treat them
as drafts (chapter 5).

## "A part is a tone away from everyone else"

The transposing-instrument trap of chapter
6, in its natural habitat. Either the part
was "helpfully" edited to match the concert
score, or the score itself was entered from
a written-pitch source without saying so.
Fix the model, not the note: make the
score concert pitch (or deliberately the
other way, once, everywhere), regenerate
the part, and run chapter 6's one-bar check
before printing.

## "My helper command killed my own shell"

A lab confession, kept because it will
happen to someone automating conversions:
`pkill -f musescore` matches any process
whose command line *mentions* musescore —
including the shell running the `pkill`
command itself, if the pattern is in its
command line. Match on the binary's exact
path or a PID you recorded, and never on a
bare name that also appears in your own
scripts.
