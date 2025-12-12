votes_file = "votes.txt"

class VoteStuff:
    def __init__(self, filename=votes_file):
        self.file = filename
        self.ids = set()
        self.votes = {}
        self.load()

    def load(self):
        try:
            f = open(self.file, "r")
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    voterID = parts[0]
                    name = parts[1]
                    self.ids.add(voterID)
                    self.votes[name] = self.votes.get(name, 0) + 1
            f.close()
        except FileNotFoundError:
            pass

    def check_id(self, voterID):
        if voterID == "":
            return False, "Please enter an ID"
        if not voterID.isdigit():
            return False, "ID must be numbers only"
        return True, ""

    def seen(self, voterID):
        return voterID in self.ids

    def save_vote(self, voterID, who):
        f = open(self.file, "a")
        f.write(voterID + "," + who + "\n")
        f.close()
        self.ids.add(voterID)
        self.votes[who] = self.votes.get(who, 0) + 1