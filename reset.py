#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 14:41:46 2018

@author: qpetit
"""

import PIL.Image
import PIL.ImageTk
import sys
if sys.version_info[0] < 3:
    from Tkinter import * 
else:
    from tkinter import *

def reset_window(dynamic_screen, dic, input_xmin, input_xmax, input_ymin, input_ymax, check_custom, button_display, button_save, button1, button2, menubar, button_display_windows):
    global graphique
    
    for w in dynamic_screen.winfo_children():
        w.destroy()
    canvas = Canvas(dynamic_screen,width=800, height=600, bg='white')
    canvas.grid(sticky="NSEW")
    logo = PIL.Image.open('img/SMG2S_logomin.png')
    logof = PIL.ImageTk.PhotoImage(logo)
    dic['logo'] = logof
    canvas.create_image(400,300,image=logof)
    dynamic_screen.update_idletasks()
    dynamic_screen.update()
    
    menubar.entryconfigure(2, state=DISABLED)
    menubar.entryconfigure(3, state=DISABLED)
    #On écrase le chemin préalablement inscrit dans le fichier 1
    mon_fichier = open("data/files/file1.txt", "w") 
    mon_fichier.write("")
    mon_fichier.close()
    
    input_xmin.configure(state="disabled")
    input_xmin.select_clear()
    input_xmax.configure(state="disabled")
    input_xmax.select_clear()
    input_ymin.configure(state="disabled")
    input_ymin.select_clear()
    input_ymax.configure(state="disabled")
    input_ymax.select_clear()
    button_display.configure(state="disabled")
    button_save.configure(state="disabled")
    button_display_windows.configure(state="disabled")
    
    check_custom.deselect()
    
    #De même pour le fichier 2
    mon_fichier = open("data/files/file2.txt", "w")
    mon_fichier.write("")
    mon_fichier.close()
    
    button1.configure(fg = "#F3421C")
    button2.configure(fg = "#F3421C")
    
    #On efface les inscriptions potentiellement présentes dans les canvas de la fenêtre
#    can_plot.delete(ALL)
#    text_image1 = can_plot.create_text(400, 290, text="The graphic will be generate here")
#    text_image2 = can_plot.create_text(400, 310, text="please select files then click on Run (File->Run)")

