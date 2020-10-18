### Description 
```
Download images from google using chromedriver.
```

### Preparations
1. python3(or python2) -m pip install selenium
2. install chromedriver(please search direction from google) 

   2.1 ubuntu
    ```
    sudo apt install chromium-chromedriver
    ```
   2.2 mac os x
  
   2.3 windows

### Usage

```
python3 download_image_from_google.py -help
```
  **Examples**
  1. convention
  ```
  python3 download_images_from_google.py "bird"
  python3 download_images_from_google.py "beautiful girl"
  python3 download_images_from _google.py "handsome boy, beautiful girl"
  ```
  2. using http(https) proxy:
  ```
  python3 download_images_from "duck" --proxy <ip>:<port>
  ```
  3. using socks5 proxy:
  ```
  python3 download_images_from_google.py "duck" --proxy socks5://<ip>:<port>
  ```
