from tkinter import Tk
from gui import VoteApp


def main():
    root = Tk()
    root.title("Voting Window")
    root.resizable(False, False)
    VoteApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
