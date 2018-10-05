import subprocess
import os
from mutagen.easymp4 import EasyMP4


#directory to download files to
dlDir = os.getcwd() + '\\dl\\'

#delete files in the dlDir
if os.path.exists(dlDir):
    if len(os.listdir(dlDir)) != 0:
        print("Deleting dl folder contents: ")
        for file in os.listdir(dlDir):
            print(file)
            os.unlink(dlDir + file)

# url of playlist to download
url = "https://www.youtube.com/watch?v=u6zWRAxPVU0&list=PLVQk7v-6PrEH2_4sxegSVGsFPi8y7X4r9"

# powershell command to be later executed
power = "$Playlist = ((Invoke-WebRequest \"" + url + """\").Links | Where {$_.class -match "playlist-video"}).href

ForEach ($Video in $Playlist) {
$s ="https://www.youtube.com" + $Video
$s =$s.Substring(0, $s.IndexOf('&'))
    Write-Output ($s)
}"""

# deletes file contents
s = open("out.txt", 'a')
s.seek(0)
s.truncate()
s.close()

# execute the powershell script to grab the video urls
t = subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", power], stdout=open("out.txt", "w+"))

# reopen our file to read from
s = open("out.txt", "r")

#iterate urls in file
for sUrl in s:
    #download 128k audio m4a of file
    #subprocess.call(["youtube-dl.exe", "--extract-audio", "--audio-format", "mp3", "-o", dlDir + "%(title)s.%(ext)s", sUrl])
    subprocess.call(["youtube-dl.exe", "-f", "140", "-o", dlDir + "%(title)s.%(ext)s", sUrl])


band = input("The Band Name: ")
album = input("The Album Name: ")


for file in os.listdir(dlDir):
    print("File Name: ", file)
    metatag = EasyMP4(dlDir + file)
    metatag['artist'] = band
    metatag['album'] = album
    metatag['title'] = input("Track Title?   ")
    metatag['tracknumber'] = input("Track Number?    ")
    metatag.save()

