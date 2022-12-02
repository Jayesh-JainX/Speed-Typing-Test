from time import *
import random
import datetime


def error_check(l, s):
    o = 0
    for i in range(max(len(l), len(s))):
        try:
            if(l[i] != s[i]):
                o += 1
        except:
            o += 1
    return o


f = open("typing_speed.txt", 'a')
f.write("\n\n--------------------------------------------------------------------------\n")
f.write("-------------------------- Typing Speed History --------------------------\n")
x = datetime.datetime.now()
f.write("- "+x.strftime("%c")+"\n\n")
f.close()

while(1):
    print("\n\n------------------------------------------------------------------------------\n")
    print("---------------------  Welcome To Typing Speed Testing  ----------------------\n\n")
    s = int(input("1: Start Speed Typing Testing\n2: See History\n3: Enter '0' to Exit\n\nEnter Your Choice: "))
    if(s == 0):
        print("\n\n------------------------- Thanks For Using Our Service -------------------------\n")
        print("--------------------------------------------------------------------------------\n\n")
        f = open("typing_speed.txt", 'a')
        f.write("\n-------------------- App Closed --------------------\n\n\n\n")
        f.close()
        break
    elif(s == 1):
        a = ["Raju", "Monica", "Liza", "Yash", "Jayesh"]
        b = ["is", "was", "in", "at", "or"]
        c = ["Working", "Playing", "Crying", "Eating", "Coding"]
        d = ["Hard", "Easy", "Card", "Berry", "Python"]
        e = ["Happy", "Sad", "Cool", "Good", "Better"]
        sent = random.choice(a)+' '+random.choice(b)+' ' + \
            random.choice(c)+' '+random.choice(d)+' '+random.choice(e)
        print("\n\n--------------------------------------------------------------------------------\n")
        print("\n--------------------------------- Your Sentence --------------------------------\n")
        t1 = time()
        print("\n\n ---> "+sent)
        ent = input("\nEnter the Above Sentence: ")
        t2 = time()
        print("\n\n------------------------------------ Result ------------------------------------\n")
        ei = error_check(sent, ent)
        p = sent.split(" ")
        print(" - Speed per Word: ", round(round((t2-t1), 2)/(len(p))), "Word/sec")
        print(" - Total Time Taken: ", round((t2-t1), 2), "Seconds")
        print(" - Total Errors : ", ei, "Caught")
        f = open("typing_speed.txt", 'a')
        f.write("\n- Given Sentence: "+sent+"\n- Input From User: "+ent+"\n- Speed per Word: "+str(round(round((t2-t1), 2)/(len(p)))
                                                                                                   )+" Word/sec"+"\n- Total Time Taken: "+str(round((t2-t1), 2))+" Seconds"+"\n- Total Error's: "+str(ei)+" Caught\n\n")
        f.close()
    elif(s == 2):
        f = open("typing_speed.txt", "r")
        for l in f:
            print(l, end='')
        f.close()
        print("\n------------------------ Speed Typing History Ends ------------------------\n\n")
    else:
        print("\n\nWrong Choice Try Again")
