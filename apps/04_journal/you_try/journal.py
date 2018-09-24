def load():
    journalfile = open("journalfile","r")
    journal = []
    for str in journalfile.readlines():
        journal.append(str.rstrip())
    journalfile.close()
    return journal
def save(journal):
    open("journalfile","w").close()
    journalfile = open("journalfile","w")
    for item in journal:
        journalfile.write(item+"\n")
    journalfile.close()