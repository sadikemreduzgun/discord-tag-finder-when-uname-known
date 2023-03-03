# import packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tkinter import *
import tkinter as tk
from selenium.webdriver.common.keys import Keys
import easygui

# assign variables for tkinter
root = Tk()
root.geometry("720x360")
root.minsize(600, 300)
root.config(background="#fff")
text_box = Text(root, height=15, width=50)
# assign input variables
start = []
end = []
nick = []
email = []
passwd = []


# assign functions to be used in tkinter
# start functio main function
def start_it():
    main_button.pack_forget()
    pick_start_button.pack()
    text_box.pack()


# first button function
def get_start():
    start1 = text_box.get(1.0,tk.END)
    start1 = start1[0:-1]
    start.append(start1)
    pick_start_button.pack_forget()
    pick_end_button.pack()
    text_box.pack_forget()
    text_box.pack()


# second button function
def get_end():
    end1 = text_box.get(1.0,tk.END)
    end1 = end1[0:-1]
    end.append(end1)
    pick_end_button.pack_forget()

    pick_nick_button.pack()
    text_box.pack_forget()
    text_box.pack()


# third button function to get nick
def get_nick():
    nick1 = text_box.get(1.0,tk.END)
    nick1 = nick1[0:-1]
    nick.append(nick1)
    pick_nick_button.pack_forget()

    pick_email_button.pack()
    text_box.pack_forget()
    text_box.pack()


# fourth button function to get your discord e-mail
def get_email():
    email1 = text_box.get(1.0,tk.END)
    email1 = email1[0:-1]
    email.append(email1)
    pick_email_button.pack_forget()

    pick_password_button.pack()
    text_box.pack_forget()
    text_box.pack()


# fifth button function to get discord password
def get_pass():
    passwd1 = text_box.get(1.0,tk.END)
    passwd1 = passwd1[0:-1]
    passwd.append(passwd1)
    pick_password_button.pack_forget()
    text_box.pack_forget()
    quit_button.pack()

    
# assign buttons of tkinter
main_button = Button(root, text="start", command=start_it, bg="#99d9ea", height=7, width=25)
main_button.pack()
pick_start_button = Button(root, text="enter the start range of interval and click me", command=get_start, bg="#99d9ea", height=7, width=25)
pick_end_button = Button(root, text="enter the end range of interval and click me", command=get_end, bg="#99d9ea", height=7, width=25)

pick_nick_button = Button(root, text="enter the discord searched nickname", command=get_nick, bg="#99d9ea", height=7, width=25)
pick_email_button = Button(root, text="enter your e mail and click", command=get_email, bg="#99d9ea", height=7, width=25)
pick_password_button = Button(root, text="enter your discord password and click", command=get_pass, bg="#99d9ea", height=7, width=25)

quit_button = Button(root, text="We are done start the bot by clicking me", command=root.destroy)


# a function to return nickname with tag
def give_back_str(num, nick):

    str_num = str(num)
    if len(str_num) == 1:
        str_num = "000" + str_num
    elif len(str_num) == 2:
        str_num = "00" + str_num
    elif len(str_num) == 3:
        str_num = "0" + str_num

    return nick + "#" + str_num


# start tkinter
root.mainloop()
# make sure everything is correct by showing again
print(start[0],end[0],email[0],passwd[0],nick[0])

# assign web driver (chrome makes problems firefox is better)
driver = webdriver.Firefox()
# open discord's web page
driver.get("https://discord.com/login")

# get back assignments
start = start[0]
end = end[0]
nick = nick[0]
start=int(start)
end = int(end)

# start Selenium bot
try:
    # type in e-mai
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.NAME, "email"))
    ).send_keys(email[0])
    # don't be so fast, we are not bot right?
    # wait for 2 seconds
    time.sleep(2)
    # type in password
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.NAME, "password"))
    ).send_keys(passwd[0])
    # wait for 2 seconds
    time.sleep(2)
    # click login button
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "button-1cRKG6"))
    ).click()
    # wait for discord's main page to open
    time.sleep(9)
    # click on friends
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "name-2m3Cms"))
    ).click()
    # wait for 2 seconds
    time.sleep(2)
    # click on add friend button
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "addFriend-emTWY1"))
    ).click()
    # wait for 2 seconds
    time.sleep(2)
    # while start is smaller than end tag do those
    while start <= end:
        
        try:
            # get nickname and tag
            name = give_back_str(start,nick)
            # we are in adding-friends part. Type in name and tag of person 
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "add-friend"))
            ).send_keys(name)
            # click "add friend" button
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "sizeSmall-3R2P2p"))
            ).click()
            # wait for 1 sec
            time.sleep(1)
            # if no one is found click the pop-up button
            try:
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "sizeXlarge-2GQ4VO"))
                ).click()
            # if found, create a messagebox
            except:
                easygui.msgbox(f"I found the chosen one: +{name}", title="Found!!")
            # wait for 2 seconds
            time.sleep(2)
            
            # chose written text and delete it by pressing ctrl+a then delete
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "add-friend"))
            ).send_keys(Keys.CONTROL, 'a')
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "add-friend"))
            ).send_keys(Keys.BACKSPACE)
            # wait for 2 sec
            time.sleep(2)
            # increase start index by one
            start += 1

        except:
            try:
                # wait for discord's main page to open
                time.sleep(9)
                # click on friends
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "name-2m3Cms"))
                ).click()
                # wait for 2 seconds
                time.sleep(2)
                # click on add friend button
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "addFriend-emTWY1"))
                ).click()
                # wait for 2 seconds
                time.sleep(2)
                # while start is smaller than end tag do those
            except:
                print("The is a problem! Where am I! ")

# quit at the end
finally:
    driver.quit()

