import tkinter as tk
from functools import partial
import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text, ttk
import os
import yt_dlp
import urllib.request
import re




desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
desktop_loc = desktop+"/%(title)s.%(ext)s"



def search_youtube(vsearcher):

    vsearch= vsearcher.get()
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': desktop_loc,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    print(vsearch)

    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=%s" %vsearch)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print(video_ids)

    html1 = "https://www.youtube.com/watch?v=" + video_ids[0]
    html2 = "https://www.youtube.com/watch?v=" + video_ids[1]
    html3 = "https://www.youtube.com/watch?v=" + video_ids[2]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict1 = ydl.extract_info(html1, download=False)
        info_dict2 = ydl.extract_info(html2, download=False)
        info_dict3 = ydl.extract_info(html3, download=False)
        video_title1 = info_dict1.get('title', None)
        video_title2 = info_dict2.get('title', None)
        video_title3 = info_dict3.get('title', None)

    label2 = tk.Label(root, text=video_title1).grid(row=5, column=1)
    label3 = tk.Label(root, text=video_title2).grid(row=6, column=1)
    label4 = tk.Label(root, text=video_title3).grid(row=7, column=1)
    label5 = tk.Label(root, text="1.").grid(row=5, column=0)
    label6 = tk.Label(root, text="2.").grid(row=6, column=0)
    label7 = tk.Label(root, text="3.").grid(row=7, column=0)

    def insideDownload(video):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['https://www.youtube.com/watch?v=%s' % video])

    insideDownload1 = partial(insideDownload, video_ids[0])
    insideDownload2 = partial(insideDownload, video_ids[1])
    insideDownload3 = partial(insideDownload, video_ids[2])
    buttonCal2 = tk.Button(root, text="Download", command=insideDownload1).grid(row=5, column=2)
    buttonCal3 = tk.Button(root, text="Download", command=insideDownload2).grid(row=6, column=2)
    buttonCal4 = tk.Button(root, text="Download", command=insideDownload3).grid(row=7, column=2)



root = tk.Tk()
root.geometry('800x200+100+200')


label1 = tk.Label(root, text="Song Title").grid(row=1, column=0)

video_search = tk.StringVar()

entry1 = tk.Entry(root, textvariable=video_search).grid(row=1, column=2)


search_youtube = partial(search_youtube, video_search)

buttonCal = tk.Button(root, text="Search", command=search_youtube).grid(row=3, column=0)


root.mainloop()
