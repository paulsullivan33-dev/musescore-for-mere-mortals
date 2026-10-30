# Installing MuseScore

**The outcome:** the program is on your machine,
and you have run the one command that proves
which version you actually got.

## Get it from the project

MuseScore Studio is free. Download it from
**musescore.org** (the program's home) or from
the project's GitHub releases — and be wary of
look-alike download sites, which bundle free
programs with things nobody asked for. The
program is open source (GPL), so other sources
*can* be legitimate; the project's own are the
ones this guide can vouch for.

The current release at the time of writing is
**4.7.6** (published 26 October 2026). The
project releases often; whatever the number
is when you read this, the shape of the
install is the same.

- **Windows:** an `.msi` installer, plus a
  portable `.paf.exe` build that runs without
  installing.
- **macOS:** a `.dmg`; open it and drag the
  app to Applications.
- **Linux:** an **AppImage** — one file that
  contains the whole program. Make it
  executable (`chmod +x`), run it. No
  installation in the system sense, and
  removing the file removes the program.

Linux distributions also package MuseScore.
A package from your distribution is convenient
and updates with everything else, but its
version is whatever the distribution froze,
which can lag the project's by a long way.
This guide does not quote a number it didn't
read: the lab used the AppImage, and where a
behaviour in these chapters is version-sensitive,
it says which version showed it.

## How this lab ran it (and a check you can copy)

The lab's sandbox has no FUSE, the kernel
helper AppImages normally use to mount
themselves, so the AppImage could not run the
usual way. The fallback is built into every
AppImage and is worth knowing on any machine
where the double-click does nothing:

```sh
./MuseScore-Studio-4.7.6.261022093-x86_64.AppImage --appimage-extract
./squashfs-root/usr/bin/mscore4portable --version
```

Extraction unpacks the program into
`squashfs-root/` and the real binary inside is
`mscore4portable`. Before running it, the lab
verified the download: the release publishes
a `checksums.sha256.txt`, and the AppImage's
SHA-256 matched it exactly (transcript
`musescore-lab/transcripts/t00-download-and-extract.txt`).
Thirty seconds with `sha256sum` is cheap
insurance for a 193 MB download from anywhere.

On a headless Linux box (no display at all),
the binary still needs *some* screen to draw
on, real or virtual. The lab used a virtual
one (`xvfb-run`), the same trick other guides
in this series use for graphical programs on
servers. On a normal desktop you will never
meet this problem.

## The version check

Whatever route you took, prove what you have:

```sh
mscore4portable --version
```

The lab's answer:

```text
MuseScore4 4.7.6
```

(The command may be `mscore`, `msescore` or a
full path on your system; `--help` on the same
binary prints the whole command-line surface —
the lab's copy is `musescore-lab/transcripts/t02-help.txt`,
and chapter 9 is built from it.)

If the version surprises you — an old distro
package, a leftover from a previous install —
believe the command, not the icon. More than
one MuseScore generation can live on one
machine, and file associations follow their
own rules.

## MuseHub, briefly

On Windows and macOS the installer offers
**MuseHub**, a companion app that manages
MuseSounds libraries and other add-ons. It is
optional for notation itself: the program
writes, prints and plays with its bundled
sounds without it. Install it when you want
the larger sound libraries of chapter 7, and
not before — one less moving part while you
learn. On Linux, MuseSounds are obtained
through MuseHub's Linux build as well;
the AppImage contains only MS Basic, as
chapter 2 recorded.

## First launch

The first launch shows a welcome wizard
(theme, an optional tour) and may offer a
start screen of recent and example scores.
Open the example score if one is offered and
press play: you should eventually hear
something. If you don't, chapter 13 has the
sound checks in order. Then close it — the
next chapter starts from an empty page.
