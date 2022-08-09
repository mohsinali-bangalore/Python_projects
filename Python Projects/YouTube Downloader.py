from pytube import YouTube
from sys import argv

link = input('Paste the link here: ')
yt = YouTube(link)

print("Title:", yt.title)
print("Views:", yt.views)

yd = yt.streams.get_highest_resolution()
#Download path can be changed according to user needs
yd.download('/Users/mohsi/Desktop/Python Practice') 