# Limits

**The outcome:** you know where MuseScore's
edges are before you lean on them — several
of these were found by this guide's lab
leaning, carefully, and measuring.

1. **The command line has silent corners.**
   In 4.7.6 the lab measured three: the
   `--transpose` interval mode that exits
   happily and transposes nothing; the
   parts flags (`-P`, `--score-parts`)
   that exit happily and write nothing when
   a score has no parts yet; and a
   multi-entry `-j` job that segfaults
   after its first conversion. The pattern
   is the problem, not any one bug: **exit
   code 0 from the converter is a claim,
   not a proof.** Chapters 9 and 10 exist
   to check the claims.
2. **Parts are born in the GUI.** There is
   no scripted path from "a score" to "a
   set of parts" in this build. One
   interactive session creates them; after
   that they live in the file. Automation
   starts after that session, not instead
   of it.
3. **Playback proves notes, not music.**
   The computer plays exactly what's
   written, including the impossible
   breath, the unplayable stretch, the
   balance no section could manage. It
   also can't tell you the piece is dull.
   Human players remain the only complete
   test, and rehearsal the only complete
   debugger.
4. **The bundled sounds are a workhorse,
   not an orchestra.** MS Basic covers the
   instruments decently. MuseSounds is
   better by reputation and by design, but
   it is a separate download through
   MuseHub, and no playback library turns
   a notation program into a recording:
   for a finished-sounding demo, the road
   runs through MIDI export into a DAW
   (chapter 11).
5. **Interchange is lossy at the edges.**
   MusicXML carries the music and most of
   the meaning; fine layout and playback
   settings are MuseScore's own and do not
   all travel. MIDI carries less. Anyone
   promising a perfect round trip between
   notation programs is selling something.
6. **Engraving taste is still yours.** The
   defaults are good — good enough that
   most scores need no layout work at all —
   but professional publishing (house
   styles, critical editions, dense
   contemporary notation) reaches for
   controls and guarantees that belong to
   the commercial tools' home ground
   (chapter 11).
7. **The web side is a shop.** The program
   is free software; musescore.com is a
   commercial service with subscriptions
   and licensed content, and its terms
   change independently of the program's
   releases. Nothing in the program
   requires it.
8. **This guide's evidence has a version.**
   The measured chapters describe 4.7.6,
   the current release when the lab ran.
   The silent corners of chapter 9 are
   exactly the kind of thing a point
   release fixes; the checks in chapter 10
   are how you find out whether yours did.
