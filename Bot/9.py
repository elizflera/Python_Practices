class Miles_FSM():

    def __init__(self):
        self.state = "A"

    def roam(self):
        if self.state == "A":
            self.state = "B"
            return 0
        elif self.state == "B":
            self.state = "C"
            return 1
        elif self.state == "C":
            self.state = "E"
            return 3
        elif self.state == "D":
            self.state = "F"
            return 6
        elif self.state == "E":
            self.state = "F"
            return 8
        else:
            raise KeyError

    def put(self):
        if self.state == "C":
            self.state = "A"
            return 4
        elif self.state == "D":
            self.state = "E"
            return 5
        else:
            raise KeyError

    def clone(self):
        if self.state == "C":
            self.state = "D"
            return 2
        elif self.state == "D":
            self.state = "B"
            return 7
        else:
            raise KeyError


def main():
    obj = Miles_FSM()
    return obj


o = main()
print(o.roam())  # 0
print(o.roam())  # 1
print(o.put())  # 4
print(o.roam())  # 0
print(o.roam())  # 1
print(o.clone())  # 2
print(o.clone())  # 7
print(o.roam())  # 1
print(o.clone())  # 2
print(o.put())  # 5
print(o.put())  # KeyError
print(o.roam())  # 8
