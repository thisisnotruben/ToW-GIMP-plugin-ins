# Tides of War GIMP plug-ins

![icon](icon.png)

## Author:
Ruben Alvarez Reyes

Email: rubenar1996@gmail.com

Twitter: [thisisnotruben_](https://twitter.com/thisisnotruben_)

Instagram: [thisisnotruben](https://www.instagram.com/thisisnotruben/)

Facebook: [Ruben Alvarez Reyes](https://www.facebook.com/thisisnotruben)

## Description:
* Makes the the death effect animation for [Tides of War](https://github.com/thisisnotruben/Tides-of-War).

## Program used for:
* [Tides of War](https://github.com/thisisnotruben/Tides-of-War)
* [GIMP](https://www.gimp.org/) *tested on version 2.8.22*

## Installation:
Once downloaded, copy plug-ins to GIMP plug-in directory.

*Copy **only** the scripts*

```bash
cp *.py $HOME/.gimp-2.8/plug-ins/
```

## Example console usage:

*The following syntax after **-b** is in scheme*

* SRC and DEST = string value; absolute file paths to png.

* NUM_OF_FRAMES = int value; total number of frames in sprite-sheet.

* STARTING_FRAME = int value; index frame number of where death animation begins.

```bash
gimp -idf -b '(python-fu-death-anim-batch RUN-NONINTERACTIVE "SRC" "DEST" NUM_OF_FRAMES STARTING_FRAME)' -b '(gimp-quit 0)'
```

## Example output:
![example](example.png)

## End Result:
![example-death-animation](example_anim.gif)
