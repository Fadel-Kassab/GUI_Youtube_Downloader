# GrapoLoader project
# By Fadel Kassab
# 30/3/2021


import os
from tkinter import *
from pytube import YouTube
from moviepy.editor import *
from tkinter import messagebox


root = Tk()
root.title("Grapo Loader\U0001F347")
root.configure(bg='purple4')

choice = IntVar()
choice.set("1")


def download(format):
    # Mp4 format
    if format == 1:
        try:
            url = url_field.get()
            download_path = directory_field.get()
            vid = YouTube(url)
            vid = vid.streams.get_highest_resolution()
            vid.download(download_path)
        
        except:
            messagebox.showerror("Error", "An error occurd please check the URL\nand the saving path or try again.")
    # Mp3 format
    else:
        #Getting input from user
        url = url_field.get()
        download_path = directory_field.get()
        
        #Getting video
        vid = YouTube(url)
        vid = vid.streams.get_lowest_resolution()
        
        #Creating build directory
        buildDir = download_path + "\\Mp3_Build_Rl"
        os.mkdir(buildDir, mode=0o666)
        
        #Downloading Mp4 file
        vid.download(buildDir)
        
        #Getting current MP4 file name
        myList = os.listdir(buildDir)
        vidName = myList[0]
        
        #Mp4 --> Mp3
        mp4_file = buildDir + '\\' + vidName

        if '.mp4' in vidName:               
            vidName = vidName.replace(".mp4", "")

        mp3_file = download_path + "\\" + vidName + ".mp3"
        videoClip = VideoFileClip(mp4_file)
        audioclip = videoClip.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoClip.close()

        os.remove(mp4_file)
        os.rmdir(buildDir)
        

#URL input & text
url_prompt = Label(root, text = "Enter video URL:", fg = "white", bg = "purple4")
url_prompt.config(font=("Times", 12))
url_prompt.grid(row = 0, column = 0, sticky = W)
url_field = Entry(root, width = 50, borderwidth = 10, fg = "purple4")
url_field.grid(row = 1, column = 0, columnspan = 3, sticky = W + E)

#Directory input & text
dir_prompt = Label(root, text = "Enter saving path:", fg = "white", bg = "purple4")
dir_prompt.config(font=("Times", 12))
dir_prompt.grid(row = 2, column = 0)
directory_field = Entry(root, width = 25, borderwidth = 10, fg = "purple4")
directory_field.grid(row = 2, column = 1, columnspan = 2) 

#Radio buttons & text
type_prompt = Label(root, text = "Save as:", fg = "white", bg = "purple4")
type_prompt.config(font=("Times", 12))
type_prompt.grid(row = 3, column = 1)
mp4_button = Radiobutton(root, text = "mp4 file", variable = choice, value = 1)
mp4_button.grid(row = 3, column = 2)
mp3_button = Radiobutton(root, text = "mp3 file", variable = choice, value = 0)
mp3_button.grid(row = 4, column = 2, pady = 3)

#Download Buttons
download_b = Button(root, text = "Download", command = lambda: download(choice.get()), padx = 50, pady = 7)
download_b.config(font=("Times", 12))
download_b.grid(row = 3, column = 0)

#Credits
logo = Label(root, text = "By Fadel Kassab", bg = "purple2", padx = 25)
logo.config(font=("Courier", 10))
logo.grid(row = 4, column = 0, sticky = W + S + N)

#Design
design = Label(root, text = "Stay juicy..!\U0001F347", bg = "purple2", padx = 5)
design.config(font=("Times", 10))
design.grid(row = 4, column = 1, sticky = S)

root.mainloop()
