
journal = []  # Journal

def printheader():
    print('------ Journal App -------')

def listentries():
    for entry in journal:
        print (entry)

def addentry():
    entry = input ("What do you want to add to your journal? ")
    journal.append(entry)


def eventloop():
    while (True):
        print('What do you want to do?')
        cmd = input('(L)ist, (A)dd, E(x)it ? ')
        cmd = cmd.strip()
        cmd = cmd.lower()
        if (cmd == 'l'):
            listentries()
        elif (cmd == 'a'):
            addentry()
        elif (cmd == 'x'):
            print ('Thank you for using the Journal App!')
            break
        else:
            print("Sorry, didn't understand that")

def main():
    printheader()
    listentries()
    eventloop()

if __name__ == "__main__":
    main()