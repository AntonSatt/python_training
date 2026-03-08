import os

def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_startup_menu():
    print("[1] View tasks\n"
        "[2] Add task\n"
        "[3] Mark task complete\n"
        "[4] Delete task\n"
        "[5] Quit\n")

def main():
    clean_terminal()
    print_startup_menu()




if __name__ == "__main__":
    main()
