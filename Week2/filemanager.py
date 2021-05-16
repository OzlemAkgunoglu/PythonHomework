#this code will clean up the numerical and other special characters
#then writes only the alphabetical characters to new file

file=open("odev.txt","r",encoding="utf-8")
clean=open("clean.txt","a")
list=file.readlines()
for line in list:
    line=''.join([i for i in line if i.isalpha()])+"\n"
    clean.write(line)
file.close()
clear.close()
