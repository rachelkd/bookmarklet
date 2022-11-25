# TO RUN on MACOS:
# Open Terminal and type:
# python3
# Space after python3, then drag .py file onto Terminal
# Press enter
# To re-run, use "up arrow" key and press enter

# TO RUN on WINDOWS:
# Double-click .py file

# Mac Installation:
# Download Python 3 @ python.org
# Run the cmd in Terminal: pip3 install pyperclip

# Windows Installation:
# Install Python 3
# Do cmd: pip install pyperclip
#   Make sure to install in Scripts directory using cmd:
#   cd C:\Users\<username>\AppData\Local\Programs\Python\Python39\Scripts

import pyperclip
import os
import platform

def clear():
    plt = platform.system()
    if plt == "Windows" or plt == "win32":
        os.system('cls') #on Windows System
    elif plt == "Linux":
        os.system('clear') #Linux and Mac
    elif plt == "Darwin":
        os.system('clear') #Linux and Mac
    else:
        i = 0
        while i < 10:
            print("\n")
            i += 1

def repeat(): #Declare now, pass
    pass




def writehtml():
    f = open("importbookmarks.html", "w")

    f.write("<!DOCTYPE NETSCAPE-Bookmark-file-1>\n\
    <!-- This is an automatically generated file.\n\
    \tDO NOT EDIT! -->\n")
    
    f.write("<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html; charset=UTF-8\">\n\
    <TITLE>Bookmarks<TITLE>\n\
    <H1>Bookmarks</H1>\n\
    <DL><p>\n\t")

    f.write("<DT><H3 ADD_DATE=\"0\" LAST_MODIFIED=\"0\" PERSONAL_TOOLBAR_FOLDER=\"true\">Bookmarklet</H3>\n\
    <DL><p>\n\n")

    f.close()

def addBookmark():
    # print("This is when the program will f.write the bookmark\n")
    #  print(pyperclip.paste())

    f = open("importbookmarks.html", "a")

    paste = pyperclip.paste()
    javacode = paste.replace("\"", "&quot;")

    bookmarkName = input("What's the bookmark title? \n")


    f.write("\t\t<DT><A HREF=\"" + javacode + "\"" + " ADD_DATE=\"0\">" + bookmarkName + "</A>\n\n")

    f.close()


def endHTML():
    f = open("importbookmarks.html", "a")
    
    f.write("\n\t</DL><p>\n\
    </DL><p>")
    
    f.close()




def bookmarklet():
    text = input("What do you want to copy?\n")
    quotechar = "\""
    apostrophechar = "\'"
    leftbracketchar = "("
    rightbracketchar = ")"
    atsignchar = "@"


    if quotechar in text:
        text = text.replace("\"", "\\\"")
   
    if apostrophechar in text:
        text = text.replace("\'", "\\\'")

    if leftbracketchar in text:
        text = text.replace("(", "\(")

    if rightbracketchar in text:
        text = text.replace(")", "\)")
        
    if atsignchar in text:
        text = text.replace("@", "\@")
   


    pyperclip.copy("javascript:!function(a){var b=document.createElement(\"textarea\"),c=document.getSelection();b.textContent=a,document.body.appendChild(b),c.removeAllRanges(),b.select(),document.execCommand(\"copy\"),c.removeAllRanges(),document.body.removeChild(b)}(\"%s\");" % (text) )

    print(" ")
    print("Your clipboard is now: \n")
    print(pyperclip.paste())
    paste = pyperclip.paste()

    print("\nDone! Your text is copied\n")

    addBookmark()
    repeat()


def repeat():
    again = input("Another? (Type anything but 0 unless you want to quit): ")

    if again.lower().strip() != "0":
        clear()
        bookmarklet()
    else:
        return 0


clear()

writehtml() #Creates html file in cd and writes beginning
bookmarklet()
endHTML()


input("Press ENTER to exit")
clear()
