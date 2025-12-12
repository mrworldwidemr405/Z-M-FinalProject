from tkinter import *


class VoteWindow:
    def __init__(self, root, boss):
        self.boss = boss
        self.root = root

        root.geometry("390x420")

        self.main_page = Frame(root, bg="black")
        self.result_page = Frame(root, bg="black")

        self.make_main_page()
        self.make_result_page()

        self.main_page.pack(fill="both", expand=True)

    def make_main_page(self):
        box = self.main_page

        lbl = Label(box, text="VOTING APPLICATION", bg="black", fg="white")
        lbl.pack(pady=20)

        id_lbl = Label(box, text="ID", bg="black", fg="white")
        id_lbl.pack()
        self.id_entry = Entry(box, width=20, bg="gray", fg="white")
        self.id_entry.pack(pady=5)

        self.pick = StringVar()

        for name in ["Jane", "John", "Myles", "Zac"]:
            rb = Radiobutton(box, text=name, value=name, variable=self.pick,
                             bg="black", fg="white", selectcolor="red",
                             activebackground="black", activeforeground="white")
            rb.pack()

        self.vote_btn = Button(box, text="VOTE", bg="red", fg="white",
                               command=self.send_vote)
        self.vote_btn.pack(pady=20)

        self.msg = Label(box, text="", bg="black", fg="red")
        self.msg.pack()

    def make_result_page(self):
        box = self.result_page

        self.res_lbl = Label(box, text="", bg="black", fg="white")
        self.res_lbl.pack(pady=20)

        back_btn = Button(box, text="BACK", command=self.go_back,
                          bg="gray", fg="white")
        back_btn.pack()

    def send_vote(self):
        self.boss.handle_vote()

    def get_id(self):
        return self.id_entry.get().strip()

    def get_name(self):
        return self.pick.get()

    def show_msg(self, text, color):
        self.msg.config(text=text, fg=color)

    def show_results_page(self, text):
        self.res_lbl.config(text=text)
        self.main_page.pack_forget()
        self.result_page.pack(fill="both", expand=True)

    def go_back(self):
        self.result_page.pack_forget()
        self.main_page.pack(fill="both", expand=True)
        self.msg.config(text="")
        self.id_entry.delete(0, END)
        self.pick.set("")