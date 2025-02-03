# Put this in ~/.profile
# /home/pi/simpsons-box/bash.sh

echo "Running ~/simpsons-box/bash.sh"
ifconfig
sleep 2

cd /home/pi/simpsons-box/
echo "Updating..."
git pull
sleep 2

echo "Starting..."
sleep 2
python startup.py
