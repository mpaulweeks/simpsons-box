#!/usr/bin/python

import random
import subprocess

def getFiles(path):
    files = []
    items = os.listdir(path)
    for itemName in items:
        itemPath = path + "/" + itemName
        if itemName.startswith("."):
            pass
        elif os.path.isdir(itemPath):
            subfiles = getFiles(itemPath)
            files.extend(subfiles)
        else:
            files.append(itemPath)
    return files

def shuffleEpisodes(files):
    shuffled = files[:]
    random.shuffle(shuffled)
    return shuffled

def playEpisode(episode):
    print("Starting " + episode.split("/").pop())
    cmd = ['cvlc', episode, 'vlc://quit']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    for line in p.stdout:
        print line
    p.wait()
    if p.returncode == 2:
        print("exiting")
        return False
    return True

def main():
    print("Listing files:")
    source = "/home/pi/video"
    files = getFiles(source)
    for f in files:
        print(f)

    shuffled = []
    playing = True

    while playing:
        if len(shuffled) == 0:
            # we have completed loop. reshuffle!
            shuffled = shuffleEpisodes(files)
        else:
            episode = shuffled.pop()
            playing = playEpisode(episode)

    print("All done playing")

main()
