# simpsons-box

Detailed instructions for creating a media randomizer on a Raspberry PI. Inspiration comes from these sources:

- https://stephencoyle.net/the-pi-zero-simpsons-shuffler
- https://www.reddit.com/r/3Dprinting/comments/p9lasb/i_designed_and_printed_a_working_simpsons_tv/

## set up the pi

Image the official Raspberry PI Lite image (no GUI required) on to a microSD card (the larger the better).

**NOTE: NEEDS TO BE DEBIAN BUSTER. OMXPLAYER DOES NOT WORK ON BULLSEYE**

First boot takes a while to setup and expand the filesystem. Default login credentials:

- pi
- raspberry

```bash
# Use the config GUI to enable auto-boot and ssh
sudo raspi-config

sudo apt update
sudo apt upgrade
sudo apt install omxplayer
```

## raspi-config

- System Options > Wireless LAN
- System Options > Boot / Auto Login > Console Autologin
- Interface Options > SSH > Enable
- Advanced Options > Expand Filesystem

## ssh in files

```bash
# determine ip address
ifconfig

# ssh and pull this repo to get the latest scripts and config
ssh pi@192.168.x.x
git clone https://github.com/mpaulweeks/simpsons-box.git

# copy bash_aliases
cp .bash_aliases /home/pi/
```

## copying media from usb

```bash
# create mount folder (only need to do this once)
sudo mkdir /mnt/usb
sudo chown -R pi:pi /mnt/usb

# find the name of your usb (probably /dev/sda1, but confirm)
sudo fdisk -l

# mount (replace /dev/sda1)
sudo mount /dev/sda1 /mnt/usb -o uid=pi,gid=pi

# copy files and folders into /home/pi/video (it searches recursively)
mkdir /home/pi/video

# unmount when you're done copying
sudo umount /mnt/usb
```

## (optional) increase font size

```bash
sudo vi /etc/default/console-setup

# update these two values
FONTFACE="Terminus"
FONTSIZE="16x32"

# reboot to see changes
```
