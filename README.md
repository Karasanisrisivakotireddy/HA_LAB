# HA_LAB
raspi@raspberrypi:~ $ mkdir cat_dog
cd cat_dog
raspi@raspberrypi:~/cat_dog $ python3 -m venv ta --system-site-packages
raspi@raspberrypi:~/cat_dog $ source ta/bin/activate
(ta) raspi@raspberrypi:~/cat_dog $ pip install numpy==1.24.4
pip install tflite-runtime==2.14.0
pip install opencv-python==4.8.0.76
pip install pillow
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting numpy==1.24.4
  Using cached numpy-1.24.4-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (14.0 MB)
Installing collected packages: numpy
  Attempting uninstall: numpy
    Found existing installation: numpy 1.24.2
    Not uninstalling numpy at /usr/lib/python3/dist-packages, outside environment /home/raspi/cat_dog/ta
    Can't uninstall 'numpy'. No files were found to uninstall.
Successfully installed numpy-1.24.4
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting tflite-runtime==2.14.0
  Using cached tflite_runtime-2.14.0-cp311-cp311-manylinux_2_34_aarch64.whl (2.3 MB)
Requirement already satisfied: numpy>=1.23.2 in ./ta/lib/python3.11/site-packages (from tflite-runtime==2.14.0) (1.24.4)
Installing collected packages: tflite-runtime
Successfully installed tflite-runtime-2.14.0
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting opencv-python==4.8.0.76
  Using cached opencv_python-4.8.0.76-cp37-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (41.0 MB)
Requirement already satisfied: numpy>=1.21.2 in ./ta/lib/python3.11/site-packages (from opencv-python==4.8.0.76) (1.24.4)
Installing collected packages: opencv-python
Successfully installed opencv-python-4.8.0.76
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Requirement already satisfied: pillow in /usr/lib/python3/dist-packages (9.4.0)
(ta) raspi@raspberrypi:~/cat_dog $ sudo apt update
sudo apt install python3-picamera2 rpicam-apps -y
Hit:1 http://archive.raspberrypi.com/debian bookworm InRelease
Hit:2 http://deb.debian.org/debian bookworm InRelease
Hit:3 http://deb.debian.org/debian-security bookworm-security InRelease
Hit:4 http://deb.debian.org/debian bookworm-updates InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
154 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3-picamera2 is already the newest version (0.3.31-1).
rpicam-apps is already the newest version (1.9.0-1~bpo12+1).
0 upgraded, 0 newly installed, 0 to remove and 154 not upgraded.
(ta) raspi@raspberrypi:~/cat_dog $ rpicam-hello
[0:35:31.032728775] [5215]  INFO Camera camera_manager.cpp:330 libcamera v0.5.2+99-bfd68f78
[0:35:31.075812936] [5218]  INFO IPAProxy ipa_proxy.cpp:180 Using tuning file /usr/share/libcamera/ipa/rpi/vc4/ov5647.json
[0:35:31.084971378] [5218]  INFO Camera camera_manager.cpp:220 Adding camera '/base/soc/i2c0mux/i2c@1/ov5647@36' for pipeline handler rpi/vc4
[0:35:31.085039544] [5218]  INFO RPI vc4.cpp:440 Registered camera /base/soc/i2c0mux/i2c@1/ov5647@36 to Unicam device /dev/media1 and ISP device /dev/media2
[0:35:31.085078451] [5218]  INFO RPI pipeline_base.cpp:1107 Using configuration file '/usr/share/libcamera/pipeline/rpi/vc4/rpi_apps.yaml'
Made X/EGL preview window
Mode selection for 1296:972:12:P
    SGBRG10_CSI2P,640x480/0 - Score: 3296
    SGBRG10_CSI2P,1296x972/0 - Score: 1000
    SGBRG10_CSI2P,1920x1080/0 - Score: 1349.67
    SGBRG10_CSI2P,2592x1944/0 - Score: 1567
Stream configuration adjusted
[0:35:32.134143954] [5215]  INFO Camera camera.cpp:1215 configuring streams: (0) 1296x972-YUV420/sYCC (1) 1296x972-SGBRG10_CSI2P/RAW
[0:35:32.134588727] [5218]  INFO RPI vc4.cpp:615 Sensor: /base/soc/i2c0mux/i2c@1/ov5647@36 - Selected sensor format: 1296x972-SGBRG10_1X10/RAW - Selected unicam format: 1296x972-pGAA/RAW
(ta) raspi@raspberrypi:~/cat_dog $ python3 26122025.py
python3: can't open file '/home/raspi/cat_dog/26122025.py': [Errno 2] No such file or directory
(ta) raspi@raspberrypi:~/cat_dog $ cd /home/raspi/cat_dog/ta
(ta) raspi@raspberrypi:~/cat_dog/ta $ python3 26122025.py
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
[0:38:23.449280227] [5303]  INFO Camera camera_manager.cpp:330 libcamera v0.5.2+99-bfd68f78
[0:38:23.473172102] [5313]  INFO IPAProxy ipa_proxy.cpp:180 Using tuning file /usr/share/libcamera/ipa/rpi/vc4/ov5647.json
[0:38:23.479409345] [5313]  INFO Camera camera_manager.cpp:220 Adding camera '/base/soc/i2c0mux/i2c@1/ov5647@36' for pipeline handler rpi/vc4
[0:38:23.479513417] [5313]  INFO RPI vc4.cpp:440 Registered camera /base/soc/i2c0mux/i2c@1/ov5647@36 to Unicam device /dev/media1 and ISP device /dev/media2
[0:38:23.479553583] [5313]  INFO RPI pipeline_base.cpp:1107 Using configuration file '/usr/share/libcamera/pipeline/rpi/vc4/rpi_apps.yaml'
[0:38:23.486349244] [5303]  INFO Camera camera.cpp:1215 configuring streams: (0) 640x480-XBGR8888/sRGB (1) 640x480-SGBRG10_CSI2P/RAW
[0:38:23.487804297] [5313]  INFO RPI vc4.cpp:615 Sensor: /base/soc/i2c0mux/i2c@1/ov5647@36 - Selected sensor format: 640x480-SGBRG10_1X10/RAW - Selected unicam format: 640x480-pGAA/RAW
Running... Press q to ex
