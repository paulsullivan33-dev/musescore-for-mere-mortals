# Layout and Parts

**The outcome:** your score prints as pages a
musician can actually read, each player gets a
sheet with only their music on it — and you
understand the one idea (transposing
instruments) that makes parts look "wrong"
until it clicks.

## Layout: the page is a promise

Notation is read at arm's length, at speed,
often in bad light, by someone who cannot ask
the page a question. Layout is how the score
keeps its promises anyway:

- **Staff size** is the master control
  (Format → Style, or the Layout panel). Full
  scores for a conductor are small; a part a
  player reads on a stand is larger. When a
  page looks cramped or desolate, this number
  is usually the honest fix, not dragging
  systems around.
- **Page size and margins** live in the same
  place. Set the page to the paper your
  printer and your players' folders actually
  use (A4 or Letter, consistently) — a part
  composed for A4 and printed on Letter loses
  its edges silently.
- **System breaks** — where lines of music
  break — MuseScore chooses decently by
  default. Force them only where a page turn
  demands it, and put page turns where the
  player has a rest long enough to turn.
  The best page turn is the one in a rest;
  the worst is mid-phrase, and it is a
  layout bug, not a player failure.
- **Measure numbers** every system (the
  default for parts) are how "from bar 41"
  works in rehearsal. Leave them on.

The lab's fixture, exported untouched, made
one A4 page (595 × 842 points, measured with
`pdfinfo`) — because eight bars ask little.
Your two-hundred-bar part asks more; the
controls above are the whole conversation,
and taste beyond them belongs to you and
your players.

## Parts: one sheet per player

A **part** is a separate document, generated
from the score, showing one instrument's
staves (plus cues from neighbours at the
tricky moments, which MuseScore can add).
The score and its parts are one file and one
source of music: fix a wrong note in the
score and every part is fixed; that is the
entire reason parts are generated rather
than copied.

Creating them is a graphical step: the
**Parts** button (in the main window, visible
in the lab's screenshot) opens a dialog
listing the score's instruments; you create a
part per instrument (or accept "create all"),
and each appears as a tab beside the score,
ready to lay out and print on its own.

Here the lab must be plain, because it
measured a boundary: **the command line
cannot create parts.** Fed a score with no
parts yet defined, the converter's part
options (`-P`, `--score-parts`) exit
successfully and produce nothing — the
imported score it examined contains zero
part definitions, and the flags operate on
parts that already exist
(`musescore-lab/transcripts/t06-parts-and-meta.txt`).
So: create parts once in the window; from
then on they live in the file, print with
the score from the GUI, and travel with it.

## Transposing instruments: the truth

Some instruments do not sound the note they
read. This is not perversity; it is history
plus hand size, and it is the single idea
that makes band scores confuse beginners:

- A **clarinet in B flat** reading C sounds
  B flat — a whole tone *below* what's
  written. Its part is written a whole tone
  *above* the intended sound.
- A **trumpet in B flat**: the same, a tone
  apart.
- A **horn in F** reading C sounds the F
  below — a perfect fifth down; its part is
  written a fifth up.
- An **alto saxophone in E flat** reading C
  sounds E flat a major sixth below.

The full score, to be useful to a conductor,
is usually shown at **concert pitch** —
everything as it sounds, clarinet line
written in B flat's sounding key. The
player's part must show the *written* pitch
— the clarinet's part in C, so the player's
fingers are right. MuseScore knows each
instrument's transposition, keeps one body
of music, and shows it both ways: the
**Concert pitch** switch in the status bar
(flipped in the lab's screenshot) toggles the
score view, and generated parts come out at
written pitch automatically.

The arranger's rule follows: **write (or
import) at concert pitch, trust the parts,
and check one part against the score before
printing forty.** The classic disaster — a
part manually "corrected" to match the
concert score — puts one player a tone away
from the band for a whole piece, in a way
that sounds like the player's fault. It is
the file's fault, and now it won't be yours.

## The check

For any score with parts: open one part,
pick a bar where you know the concert
pitch, and confirm the part shows it
transposed correctly for that instrument
(a tone up for the clarinet). Thirty
seconds, once per score — the cheapest
insurance in this guide.
