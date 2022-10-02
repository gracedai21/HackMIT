class Flashcard:
    def __init__(self, front, middle, back):
        self.front = front
        self.middle = middle
        self.back = back

    def __repr__(self):
        return self.front + " " + self.middle + " " + self.back
