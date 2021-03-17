class classes:
    def __init__(self, name):
        print('How many classes are you taking?')
        self.num_classes = int(input())
        self.grades = {}
        self.credits = {}
        self.level = {}
        for x in range(self.num_classes):
            print(f'What is your #{x+1} input class?')
            temp = input()
            print(f'What is the level of {temp}? AP - 1, Honors - 2, CP - 3')
            self.level[temp] = int(input())
            print(f'What is your letter grade in {temp}?')
            self.grades[temp] = input()
            print(f'How many credits is this class? (Out of 5)')
            self.credits[temp] = float(input())
