#!/usr/bin/env python

from gimpfu import *

"""
Ruben Alvarez Reyes
"""

def death_anim(image, drawable, h_frames, starting_frame):
    pdb.python_fu_death_anim_batch(image.filename, image.filename, h_frames, starting_frame)
    image = pdb.file_png_load(image.filename, image.filename)
    gimp.Display(image)

blurb = "Make ToW death animations, wrapper around death-anim-batch." + \
    "\nSide effect: makes image into RGB.\nWarning: Inplace operation!"

register(
    # proc_name
    "death_anim",
    # blurb
    blurb,
    # help
    blurb,
    # author
    "Ruben Alvarez Reyes <rubenar1996@gmail.com>",
    # copyright
    "Ruben Alvarez Reyes",
    # date
    "2020",
    # label
    "<Image>/Filters/Noise/ToW Death Animation",
    # imagetypes
    "*",
    # params
    [(PF_INT, "h_frames", "Horizontal frames. Not 0 based.", 1),
     (PF_INT, "starting_frame", "Stating frame of death animation. 0 based.", 0)],
    # results
    [],
    # function
    death_anim)

main()
