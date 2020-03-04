#!/usr/bin/env python

from gimpfu import *

"""
Ruben Alvarez Reyes
"""

# how many frames we doing this for
n_times = 4
# spread vars
spread_amount = (10.0, 10.0)
# slur vars
rndm_pct = 85.0
# save vars
interlace = 0
compression = 9
bkgd = 0
gama = 0
offs = 0
phys = 0
time = 0


def death_anim_batch(input_path, output_path, h_frames, starting_frame):

    # load img
    image = pdb.file_png_load(input_path, input_path)
    drawable = image.active_layer

    if not pdb.gimp_drawable_is_rgb(drawable):
        pdb.gimp_convert_rgb(image)

    # selection vars
    width = int(image.width / h_frames)
    height = int(image.height)
    x = (starting_frame - 1) * width
    y = 0
    
    # sprite to duplicate (what the death effect is based off)
    pdb.gimp_image_select_rectangle(image, CHANNEL_OP_REPLACE, x, y, width, height)
    sprite = pdb.gimp_edit_named_copy(drawable, "sprite_death")

    # passes to do for each filter
    spread_passes = 1
    
    # apply filters
    for i in range(n_times):

        # select
        x = (i + starting_frame) * width
        pdb.gimp_image_select_rectangle(image, CHANNEL_OP_REPLACE, x, y, width, height)

        # delete previous sprite cell
        pdb.gimp_edit_clear(drawable)

        # paste base sprite
        floating_sel = pdb.gimp_edit_named_paste(drawable, sprite, True)
        pdb.gimp_floating_sel_to_layer(floating_sel)
        drawable = pdb.gimp_image_merge_down(image, image.active_layer, EXPAND_AS_NECESSARY)

        # select again due to selection being lost from paste
        pdb.gimp_image_select_rectangle(image, CHANNEL_OP_REPLACE, x, y, width, height)

        # slur
        slur_passes = i + 1
        pdb.plug_in_randomize_slur(image, drawable, rndm_pct, slur_passes, True, 0)

        # spread on the last half of death animation
        if i > (n_times - 1) // 2:
            for j in range(spread_passes):
                pdb.plug_in_spread(image, drawable, *spread_amount)
            spread_passes += 1
            
    # save image
    pdb.file_png_save(image, drawable, output_path, output_path, interlace,
        compression, bkgd, gama, offs, phys, time)


blurb = "Make ToW death animations, meant to be runned from console." + \
    "\nSide effect: makes image into RGB.\nWarning: Inplace operation!"

register(
    # proc_name
    "death_anim_batch",
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
    "<Toolbox>/Xtns/Languages/Python-Fu/ToW Death Animation Batch",
    # imagetypes
    "",
    # params
    [(PF_STRING, "input_path", "Input path (file path)", ""),
     (PF_STRING, "output_path", "Output path (file path)", ""),
     (PF_INT, "h_frames", "Horizontal frames. Not 0 based.", 1),
     (PF_INT, "starting_frame", "Stating frame of death animation. 0 based.", 0)],
    # results
    [],
    # function
    death_anim_batch)

main()
