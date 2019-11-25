'''name=input("enter your name")
place=input("enter place")
if __name__ == '__main__':
   mobilenum="9865434535"
song="perfect"

name="barsha sunuwar"
address="itahari"
mobilenum="234234323"
song="perfect"

#Using DateTime and Time#
import datetime as dt
import time
print(dt.date.today())
print('Formatted Time: ', time.asctime())

#web browser#
import webbrowser
type=input("Search video")
print("Opening browser")
webbrowser.open_new_tab ('https://www.youtube.com/')

#color#
from termcolor import colored
print (colored('Welcome to my channel','red','on_yellow'))

#HW1//Using the OS Library change the name of a file.#
import os
os.rename(r'C:\Users\admin\PycharmProjects\untitled16\import st.py', r'C:\Users\admin\PycharmProjects\untitled16\import_st.py')



