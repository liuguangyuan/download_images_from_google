### Description Download images from google using chromedriver.

### Preparations

1. ubuntu

  sudo apt install chromium-chromedriver
  python3 -m pip install selenium

2. mac os x
  
3  windows
  win10's subsystem ubuntu is recommanded

### Usage

```
python3 download_image_from_google.py -help

e.g.
python3 download_images_from_google.py "bird"
python3 download_images_from_google.py "beautiful girl"
python3 download_images_from _google.py "handsome boy, beautiful girl"

want to use http(https) proxy:
e.g.
python3 download_images_from "duck" --proxy <ip>:<port>

want to use socks5 proxy:
e.g.
python3 download_images_from_google.py "duck" --proxy socks5://<ip>:<port>
```
