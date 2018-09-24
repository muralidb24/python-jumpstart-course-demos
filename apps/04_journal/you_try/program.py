import journal

def printheader():
    print('------ Journal App -------')

def listentries(entries):
    entries.reverse()
    for (idx, entry) in enumerate(entries):
        print ("Entry {} is {}".format(idx+1,entry))

def addentry(journalM):
    entry = input ('what do you want to add to your journal? ')
    journalM.append(entry)


def eventloop():
    journalM = journal.load()
    while (True):
        print('What do you want to do?')
        cmd = input('(L)ist, (A)dd, E(x)it ? ')
        cmd = cmd.strip()
        cmd = cmd.lower()
        if (cmd == 'l'):
            listentries(journalM)
        elif (cmd == 'a'):
            addentry(journalM)
        elif (cmd == 'x'):
            print ('Thank you for using the Journal App!')
            break
        else:
            print("Sorry, didn't understand that")
    journal.save(journalM)
def main():
    printheader()
    eventloop()

if __name__ == "__main__":
    main()