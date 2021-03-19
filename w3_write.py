#Write a Python program to read an entire text file
"""def file_read():
        txt = open("fname.txt","r")
        a=txt.read()
        print(a)
        txt.close()
file_read()"""

def file_read(n):
        #n=int(input(_))
        txt=open("fname.txt","r")
        a=txt.readlines(n)
        print(a)
        txt.close()
n=int(input("enter: "))
file_read(n)


