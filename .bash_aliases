# ln -s /home/pi/simpsons-box/.bash_aliases /home/pi/.bash_aliases

echo "Running ~/simpsons-box/.bash_aliases"
ifconfig
sleep 5
cd /home/pi/simpsons-box/
echo "Updating..."
git pull
echo "Starting..."
sudo python startup.py
