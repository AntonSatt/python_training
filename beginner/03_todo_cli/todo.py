import os

def clear_terminal():
   os.system('cls' if os.name == 'nt' else 'clear')
      

def show_menu():
   print(" [1] View tasks\n",
   "[2] Add task\n",
   "[3] Mark task complete\n",
   "[4] Delete task\n",
   "[5] Quit\n")

def main():
   #Load json here
   clear_terminal()
   show_menu()





if __name__ == "__main__":
   main()
