from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tkinter import *
import tkinter as tk
from selenium.webdriver.common.keys import Keys
import easygui


root = Tk()
root.geometry("720x360")
root.minsize(600, 300)
root.config(background="#fff")
text_box = Text(root, height=15, width=50)

start = []
end = []
nick = []
email = []
passwd = []

def start_it():
    main_button.pack_forget()
    pick_start_button.pack()
    text_box.pack()


# main functions
def get_start():
    start1 = text_box.get(1.0,tk.END)
    start1 = start1[0:-1]
    start.append(start1)
    pick_start_button.pack_forget()
    pick_end_button.pack()
    text_box.pack_forget()
    text_box.pack()


def get_end():
    end1 = text_box.get(1.0,tk.END)
    end1 = end1[0:-1]
    end.append(end1)
    pick_end_button.pack_forget()

    pick_nick_button.pack()
    text_box.pack_forget()
    text_box.pack()


def get_nick():
    nick1 = text_box.get(1.0,tk.END)
    nick1 = nick1[0:-1]
    nick.append(nick1)
    pick_nick_button.pack_forget()

    pick_email_button.pack()
    text_box.pack_forget()
    text_box.pack()


def get_email():
    email1 = text_box.get(1.0,tk.END)
    email1 = email1[0:-1]
    email.append(email1)
    pick_email_button.pack_forget()

    pick_password_button.pack()
    text_box.pack_forget()
    text_box.pack()


def get_pass():
    passwd1 = text_box.get(1.0,tk.END)
    passwd1 = passwd1[0:-1]
    passwd.append(passwd1)
    pick_password_button.pack_forget()
    text_box.pack_forget()
    quit_button.pack()


main_button = Button(root, text="başla", command=start_it, bg="#99d9ea", height=7, width=25)
main_button.pack()
pick_start_button = Button(root, text="enter the start range of interval and click me", command=get_start, bg="#99d9ea", height=7, width=25)
pick_end_button = Button(root, text="enter the end range of interval and click me", command=get_end, bg="#99d9ea", height=7, width=25)

pick_nick_button = Button(root, text="enter the discord searched nickname", command=get_nick, bg="#99d9ea", height=7, width=25)
pick_email_button = Button(root, text="enter your e mail and click", command=get_email, bg="#99d9ea", height=7, width=25)
pick_password_button = Button(root, text="enter your discord password and click", command=get_pass, bg="#99d9ea", height=7, width=25)

quit_button = Button(root, text="We are done start the bot by clicking me", command=root.destroy)


def give_back_str(num, nick):

    str_num = str(num)
    if len(str_num) == 1:
        str_num = "000" + str_num
    elif len(str_num) == 2:
        str_num = "00" + str_num
    elif len(str_num) == 3:
        str_num = "0" + str_num

    return nick + "#" + str_num


root.mainloop()
print(start[0],end[0],email[0],passwd[0],nick[0])

driver = webdriver.Firefox()
driver.get("https://discord.com/login")


start = start[0]
end = end[0]
nick = nick[0]
start=int(start)
end = int(end)

try:
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.NAME, "email"))
    ).send_keys(email[0])
    time.sleep(2)
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.NAME, "password"))
    ).send_keys(passwd[0])
    time.sleep(2)
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "button-1cRKG6"))
    ).click()

    time.sleep(9)

    element4 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "name-2m3Cms"))
    ).click()

    time.sleep(2)
    element5 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "addFriend-emTWY1"))
    ).click()
    time.sleep(2)

    while start <= end:

        try:
            name = give_back_str(start,nick)

            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "add-friend"))
            ).send_keys(name)

            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "sizeSmall-3R2P2p"))
            ).click()

            time.sleep(1)
            try:
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "sizeXlarge-2GQ4VO"))
                ).click()

            except:
                easygui.msgbox("This is a message!", title="Buldum: "+name)

            time.sleep(2)

            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "add-friend"))
            ).send_keys(Keys.CONTROL, 'a')
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "add-friend"))
            ).send_keys(Keys.BACKSPACE)

            time.sleep(2)
            start += 1

        except:
            print("exceptteyim, eğer programı kapaattıyssan bi zahmet beni de kapatsana")
            time.sleep(603)

finally:
    driver.quit()

