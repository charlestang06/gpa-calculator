
class gpaScale:
    def __init__(self, name):
        print('Please input your unweighted GPA Scale: (Out of 4.0)')
        self.scale = {
            'A+' : 0,
            'A': 0,
            'A-': 0,
            'B+': 0,
            'B' : 0,
            'B-' : 0,
            'C+' : 0,
            'C' : 0,
            'C-' : 0,
            'D+' : 0,
            'D' : 0,
            'D-' : 0,
            'F' : 0
        }
        for key in self.scale:
            print(key)
            self.scale[key] = float(input())

        print('Please input your weighted GPA scale: (ex. Out of 1.0)')
        self.weighted_scale = {
            'AP' : 0,
            'Honors' : 0,
            'CP' : 0,
        }
        for key in self.weighted_scale:
            print(key)
            self.weighted_scale[key] = float(input())


