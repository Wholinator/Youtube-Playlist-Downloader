import subprocess

# url of playlist to download
url = "https://www.youtube.com/watch?v=tRhTe8rZHQc&list=PLQiJ2_8qupzdyUj7ZX7ujDNtFrbfwXKLR"

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
    subprocess.call(["youtube-dl.exe", "-f", "140", sUrl])
