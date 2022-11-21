#import library
from tkinter import* 

#initialize window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Shayaan Tanvir's Website Blocker")

#heading
Label(root, text = 'Shayaan Tanvir's Website Blocker' , font = 'arial 20 bold').pack()


#path of our host file ang ip adsdress 
host_path = 'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

#ENTER WEBSITE
Label(root, text= 'Enter Website :', font = 'arial 12 bold').place(x=5,y=60)
Websites = Text(root, font = 'arial 10', height ='2', width = '40', wrap = WORD,padx = 5, pady=5)
Websites.place(x = 140, y =60)

#block function
def Blocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                Label(root, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200)

block_btn = Button(root, text = 'BLOCK' , font = 'arial 12 bold', command = Blocker, width = 6 , bg = 'royal blue1', activebackground = 'sky blue')
block_btn.place(x = 230, y =150)

root.mainloop
