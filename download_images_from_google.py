#!/usr/bin/env python3

import pdb
import sys, os
import uuid
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time  
import os
import argparse
import re
import imghdr


class PullImgs:
    def __init__(self, fold, proxy):
        self.fold = fold
        self.proxy = proxy

    def pullPage(self, key):
        options = webdriver.ChromeOptions()
        if self.proxy:
            options.add_argument('--proxy-server={}'.format(self.proxy))
        options.add_argument('--no-sandbox')
        options.add_argument("--headless")
        browser = webdriver.Chrome('chromedriver', chrome_options=options)

        browser.get('https://www.google.com/imghp?hl=en&tab=wi&ogbl')

        search = browser.find_element_by_name("q")
        search.clear()
        search.send_keys(key)
        search.send_keys(Keys.RETURN)
        time.sleep(2)
        elem =browser.find_element_by_tag_name('body')
        more = elem.find_element_by_class_name('mye4qd')
        end = elem.find_element_by_class_name('Yu2Dnd')
        while True:
            if end.is_displayed():
                elem.send_keys(Keys.END)
                time.sleep(1)
                print('end len: {}'.format(len(browser.page_source)))
                break
            if more.is_displayed():
                print('more len: {}'.format(len(browser.page_source)))
                more.click()
                time.sleep(5)
            elem.send_keys(Keys.END)
            time.sleep(2)
            print('len: {}'.format(len(browser.page_source)))
        content = browser.page_source
        browser.close()
        return content

    def downloadImg(self, url, dir):
        img = os.path.join(dir, str(uuid.uuid1()))
        proxies = None
        if self.proxy:
            proxies = {'http': self.proxy, 'https': self.proxy}
        try:
            data = requests.get(url, proxies=proxies).content
            if not data:
                return False
            try:
                if '.jpg' in url:
                    img += '.jpg'
                elif '.jpeg' in url:
                    img += '.jpeg'
                elif '.png' in url:
                    img += '.png'
                with open(img, 'wb') as fp:
                    fp.write(data)
                if '.' not in img:
                    suffix = imghdr.what(img)
                    os.rename(img, img+'.'+suffix)
            except:
                print("None, cannot save")
            ret = True
        except:
            print('cannot download {}'.format(url))
            ret = False
        return ret

    def parsePage(self, page,  dir_name):
        dir = os.path.join(self.fold, dir_name)
        print(dir)
        os.makedirs(dir, exist_ok = True)
        urllist = re.findall(r'(\["htt\S+",\d+,\d+\])', page)
        print(urllist)
        print(len(urllist))
        for url in urllist:
            url = url.split(',')[0][2:-1]
            self.downloadImg(url, dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('keys', help='searched keys,e.g."duck" or "ugly duck" or "ugly duck, beautiful girl"')
    parser.add_argument('--fold', help='fold where images exist', default='.')
    parser.add_argument('--proxy', help='proxy server. if http, "--proxy <ip>:<port>", if socks5, "--proxysocks5://<ip>:<port>"', default='')
    args = parser.parse_args()
    keys = args.keys
    fold = args.fold
    proxy = args.proxy

    if len(proxy) > 0  and 'sock' not in proxy:
        os.environ['http_proxy'] = proxy;
        os.environ['https_proxy'] = proxy;
        proxy = None

    pi = PullImgs(fold, proxy)
    keys = keys.split(',')
    for key in keys:
        key = key.strip()
        page = pi.pullPage(key)
        pi.parsePage(page, key)
