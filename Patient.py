class Patient():

    def __init__(self, name):
        self.name = name
        self.heartrates = []
        self.threshold = 120

    def add_heartrate_data(self, heartrates):
        self.heartrates.append(heartrates)

    def heartrates_above_threshold(self, idx=-1):
        if idx >= len(self.heartrates):
            return False, "Index out of range"
        above_threshold = []
        for i in range(50):
            above_threshold.append(self.heartrates[idx][i] > self.threshold)
        return sum(above_threshold), "Success"
