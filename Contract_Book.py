contract = {}

def showcontract():
    print("Name \t Number")
    for x in contract:
        print("{} \t {}".format(x, contract.get(x)))

try:
    while True:
        print("**************\n"
              "**          **\n"
              "** Contract **\n"
              "**          **\n"
              "**************")
        choice = int(input("1. Add new contract \n"
                           "2. Search the contract \n"
                           "3. Display the contract \n"
                           "4. Edit the contract \n"
                           "5. Delete the contract \n"
                           "6. Exit \n"
                           "Please write a number between 1-6: "))

        if choice == 1:
            name = input("Add contract name: ")
            phone = input("Add phone number: ")
            contract[name] = phone

        elif choice == 2:
            cntrct_src = input("Search the contract: ")
            if cntrct_src in contract:
                print(cntrct_src, "Contract number is:", contract[cntrct_src])
            else:
                print("Contract not found.")

        elif choice == 3:
            if not contract:
                print("Contract book is empty.")
            else:
                showcontract()

        elif choice == 4:
            edit_contract = input("Enter contract name: ")
            if edit_contract in contract:
                phone = input("Change contract number: ")
                contract[edit_contract] = phone
                print("Contract updated successfully.")
            else:
                print("Name is not found.")

        elif choice == 5:
            delete_contract = input("Which contract do you want to delete?: ")
            if delete_contract in contract:
                deleteconfirm = input("Do you want to delete? (Y/n): ")
                if deleteconfirm == "y" or deleteconfirm == "Y":
                    contract.pop(delete_contract)
                    print("Deleted successfully.")
                    showcontract()
                elif deleteconfirm == "n" or deleteconfirm == "N":
                    print("Delete canceled.")
                else:
                    print("Unvalid input")
            else:
                print("Contract not found.")

        elif choice == 6:
            print("Exit the program.")
            break

        else:
            print("Only input number between 1 to 6.")

except ValueError:
    print("Please type an integer (1-6 only).")
