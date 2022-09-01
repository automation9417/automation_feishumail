from time import sleep
from clicknium import clicknium as cc, locator,UiElement
import subprocess
import csv
import pyperclip

def main():
    process = subprocess.Popen("C:\\Users\\kay\\AppData\\Local\\Feishu\\Feishu.exe")  #replace with your feishu.exe path
    cc.find_element(locator.feishu.mailbutton).click()
    f = open(r".\sample.txt")
    mailtxt = f.read()
    with open('user.csv') as f:
        f_csv = csv.DictReader(f)
        for u in f_csv:
            sendMai(u['email'],u['username'],mailtxt)

def sendMai(mail, name, text):
    username = getName(name)
    mailcontent = text.replace("{name}",username)
    print("email:",mail," name:",username)

    cc.find_element(locator.feishu.newmailbutton).click()
    sleep(3)
    cc.find_element(locator.feishu.edit_ia).set_text(mail, by='sendkey-after-click')
    
    cc.find_element(locator.feishu.title_text).set_text("Welcome to Clicknium", by='sendkey-after-click')
    
    paste_text(cc.find_element(locator.feishu.content_ia),mailcontent)
    cc.find_element(locator.feishu.send_button).click()
    sleep(2)


def getName(userName):
    return userName.split(",")[0].split("@")[0].split(" ")[0].split(".")[0].capitalize()

def paste_text(webEle:UiElement,text:str):
    webEle.send_hotkey('^a',preaction="click")
    webEle.send_hotkey('^x',preaction="click")
    pyperclip.copy(text)
    webEle.send_hotkey('^v',preaction="click")


if __name__ == "__main__":
    main()
