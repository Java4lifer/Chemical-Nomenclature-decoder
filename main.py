import time
def esx():
    time.sleep(2)
    exit()

choice = str(input("Name to Structure(1)/Structure to Name(2): "))
if choice == 1:
    print("Okay, lol")
elif choice == 2:
    print("Second option ain't done and will probably never be, lol")
    esx()
else:
    print("No, lol")
    esx()
#______________________________________________________________________________________________

while(True):
    nomen = str(input("Input your nomenclature: "))
    nomen = nomen.replace(" ","")
    nomen = nomen.replace("-", " ")
    nomen = nomen.replace(" an", " an ")
    nomen = nomen.replace(" en", " en ")
    nomen = nomen.replace(" in", " in ")
    nomen = nomen.upper()

    structure:list = []
    qtcarbon:list = ["MET", "ET", "PROP", "BUT", "PENT", "HEX", "HEPT", "OCT", "NON", "DEC"]
    qt:list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    qtf = 0
    name = nomen.split(" ")
    
    if name.len() < 3 or name.len() > 4:
        print("Invalid nomenclature.")
        continue
    
    connections = name[1].split(",")
    concount = connections.len()
    
    if name[0] in qtcarbon == True:
        qtf = qt[qtcarbon.index(name[0])]
    else:
        print("Invalid nomenclature prefix.")
        continue
    
