class Student(object):
    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        return self.name

    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]

    def getAverage(self):
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        return max(self.scores)

    def __str__(self):
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name

def main():
    student1 = Student('John', 5)
    student2 = Student('James', 5)

    print(f"{student1 == student2}: False")
    print(f"{student1 < student2}: True")
    print(f"{student1 >= student2}: False")

if __name__ == '__main__':
    main()
