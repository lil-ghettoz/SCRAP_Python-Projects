print("Wecome To Text File Handling!")

def menu():
    print("Type (1) To Create A File")
    print("Type (2) To Write Into File")
    print("Type (3) To View Into File")
    print("Type (4) To Exit")

def createfile():
    crtfile = input("Enter The Name Of File: ")
    insfile = input("Enter A Word To File: ")
    try:
        with open("Files.txt", "x") as folder:
            folder.write(insfile)    
    
    except FileExistsError:
        print("File Already Exists!")
    

def writingfile():
    try:
        fndfile = input("Enter The Name Of Your File: ")
        wrtfile = input("write To You File: ")
        with open(f"{fndfile}.txt", "w") as file:
            file.write(wrtfile)
    except FileNotFoundError:
        print("File Did Not Found!")
        
        
        
def viewfile():
    print("gqegewfdc")



 
 
while True:
    try:
        menu()
        users = int(input("Enter A Choice: "))
        match users:
            case 1:
                createfile()
            case 2:
                writingfile()
            case 3:
                viewfile()
            case 4:
                print("Thank You For Using Text-File Handling")
                break
            case _:
                print("Error, Pick A Number From 1 To 4!")
    except ValueError:
        print("Error, That's Invalid Choice!")
        
        
 