
def Big():
    pw = input("Password?" + "\r\n")
    if pw == "purplerain":

        print("Welcome!")
        fileName = open("nameText.txt", "a+")
        fileUser = open("userText.txt", "a+")

        indexName = []
                
        loop = False
        def read():
            fileName = open("nameText.txt", "r")
            print("\r\n" + fileName.read())


        def add():
            fileName = open("nameText.txt", "a+")
            fileUser = open("userText.txt", "a+")
            x = input("To which site does this Password belong to?" + "\r\n")
            #break-if
            if x == "exit":
                loop = True
            else:
                x = x + "\n"
                fileName.write(x)
                y = input("Type in your username" + "\r\n")
                w = input("Type in your password" + "\r\n")
                
                if x == "exit":
                    loop = True
                else:
                    y = y + "\n"
                    w = w + "\n"
                    fileUser.write(y)
                    fileUser.write(w)
                    print("finished")


        def call():
            fileName = open("nameText.txt", "r")
            fileUser = open("userText.txt", "r")
            for line in fileName.readlines():
                indexName.append(line.strip())
            z = input("For which password are you looking for?" + "\r\n")
            t = indexName.index(z)
            ui = fileUser.readlines()
            
            t = t * 2
            print ("Username: " + ui[t])
            tplus = t + 1
            print("Password: " + ui[tplus])



        while loop == False:
            
            inputMenue = input("mainmenue" + "\r\n")
            #break-if
            if inputMenue == "call":
                call()
            elif inputMenue == "add":
                add()
            elif inputMenue == "end":
                loop = True
            elif inputMenue == "reset":
                sure = input("Reset all?" + "\r\n") 
                if sure == "yes" or sure == "ja":
                    fileName = open("nameText.txt", "w")
                    fileUser = open("userText.txt", "w")
                    fileName.write("")
                    fileUser.write("")
                elif sure == "no" or sure == "nein":
                    print("okay")
                elif sure == "end":
                    loop = True
            elif inputMenue == "show":
                read()
            else:
                print("invalid Input")

        fileUser.close()
        fileName.close()
    elif pw == "end":
        exit()
    else:
        print("wrong password. please try again")
        Big()
Big()
