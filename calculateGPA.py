import json
from classes import classes
class calcGPA:
    def __init__(self, name):
        with open('unweightedscale.json', 'r') as f:
            info = json.load(f)
            self.un_cumulative = 0
            self.we_cumulative = 0
            self.num_creds = 0
            with open('grades.json', 'r') as a:
                grads = json.load(a)
                with open('credits.json', 'r') as b:
                    creds = json.load(b)
                    with open('level.json', 'r') as c:
                        with open('weightedscale.json', 'r') as d:
                            w_creds = json.load(d)
                            lvls = json.load(c)
                            for key in creds:
                                self.num_creds += creds[key]
                            for key in grads:
                                cred = creds[key]
                                self.un_cumulative += info[grads[key]]*cred
                                self.we_cumulative += (info[grads[key]]+ w_creds[lvls[key]]) * cred


        self.unweighted_gpa = self.un_cumulative/self.num_creds
        self.weighted_gpa = self.we_cumulative/self.num_creds

