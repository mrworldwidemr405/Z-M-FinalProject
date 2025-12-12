from tkinter import Tk
from gui import VoteWindow
from logic import VoteStuff


class VoteApp:
    def __init__(self, root):
        self.model = VoteStuff()
        self.view = VoteWindow(root, self)

    def handle_vote(self):
        voterID = self.view.get_id()
        who = self.view.get_name()

        ok, msg = self.model.check_id(voterID)
        if not ok:
            self.view.show_msg(msg, "red")
            return

        if who == "":
            self.view.show_msg("Please pick a candidate", "red")
            return

        if self.model.seen(voterID):
            self.view.show_msg("Already Voted", "red")
            return

        self.model.save_vote(voterID, who)
        self.view.show_msg("", "white")

        txt = ""
        for name in ["Jane", "John", "Myles", "Zac"]:
            v = self.model.votes.get(name, 0)
            txt += name + ": " + str(v) + "\n"

        self.view.show_results_page(txt)


def main():
    root = Tk()
    root.title("Voting Window")
    root.resizable(False, False)
    VoteApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()