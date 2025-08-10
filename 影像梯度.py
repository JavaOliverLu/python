from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


image_opened = Image.open('visual_cloud_16263_20220820_1038LT.jpg')

width = image_opened.size[0]
height = image_opened.size[1]


image_saved_r = Image.open('visual_cloud_16263_20220820_1038LT.jpg')
image_saved_g = Image.open('visual_cloud_16263_20220820_1038LT.jpg')
image_saved_b = Image.open('visual_cloud_16263_20220820_1038LT.jpg')
image_saved_color = Image.open('visual_cloud_16263_20220820_1038LT.jpg')

image_rgb = image_opened.convert('RGB')



for x in range(2,width-2):
    for y in range(2,height-2):
        r_extr, g_extr, b_extr = image_rgb.getpixel((x,y))
        r_extr_ul, g_extr_ul, b_extr_ul = image_rgb.getpixel((x-1,y-1))
        r_extr_um, g_extr_um, b_extr_um = image_rgb.getpixel((x,y-1))
        r_extr_ur, g_extr_ur, b_extr_ur = image_rgb.getpixel((x+1,y-1))
        r_extr_ml, g_extr_ml, b_extr_ml = image_rgb.getpixel((x-1,y))
        r_extr_mr, g_extr_mr, b_extr_mr = image_rgb.getpixel((x+1,y))
        r_extr_dl, g_extr_dl, b_extr_dl = image_rgb.getpixel((x-1,y+1))
        r_extr_dm, g_extr_dm, b_extr_dm = image_rgb.getpixel((x,y+1))
        r_extr_dr, g_extr_dr, b_extr_dr = image_rgb.getpixel((x+1,y+1))


        image_saved_r.putpixel((x,y),(r_extr*8-r_extr_ul-r_extr_um-r_extr_ur-r_extr_ml-r_extr_mr-r_extr_dl-r_extr_dm-r_extr_dr,0,0))
        image_saved_g.putpixel((x,y),(0,g_extr*8-g_extr_ul-g_extr_um-g_extr_ur-g_extr_ml-g_extr_mr-g_extr_dl-g_extr_dm-g_extr_dr,0))
        image_saved_b.putpixel((x,y),(0,0,b_extr*8-b_extr_ul-b_extr_um-b_extr_ur-b_extr_ml-b_extr_mr-b_extr_dl-b_extr_dm-b_extr_dr))
        image_saved_color.putpixel((x,y),(r_extr*8-r_extr_ul-r_extr_um-r_extr_ur-r_extr_ml-r_extr_mr-r_extr_dl-r_extr_dm-r_extr_dr,g_extr*8-g_extr_ul-g_extr_um-g_extr_ur-g_extr_ml-g_extr_mr-g_extr_dl-g_extr_dm-g_extr_dr,b_extr*8-b_extr_ul-b_extr_um-b_extr_ur-b_extr_ml-b_extr_mr-b_extr_dl-b_extr_dm-b_extr_dr))

image_saved_r.save("r_gradient.jpg")
image_saved_g.save("g_gradient.jpg")
image_saved_b.save("b_gradient.jpg")
image_saved_color.save("color_gradient.jpg")
