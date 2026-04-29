mkdir -p ~/cat_dog && cd ~/cat_dog
python3 -m venv ta --system-site-packages
source ta/bin/activate

pip install numpy==1.24.4
pip install tflite-runtime==2.14.0
pip install opencv-python==4.8.0.76
pip install pillow

sudo apt update
sudo apt install python3-picamera2 rpicam-apps -y


rpicam-hello

cd /home/raspi/cat_dog
python3 26122025.py

# To stop the script
Ctrl + C

# To leave the virtual environment
deactivate

# To re-enter the environment later
cd ~/cat_dog && source ta/bin/activate
