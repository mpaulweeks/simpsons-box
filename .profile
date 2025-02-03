# ln -s /home/pi/simpsons-box/.profile /home/pi/.profile

echo "Running ~/simpsons-box/.profile"
ifconfig
sleep 2

cd /home/pi/simpsons-box/
echo "Updating..."
git pull
sleep 2

echo "Starting..."
sleep 2
sudo python startup.py
