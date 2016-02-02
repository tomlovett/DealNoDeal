import random
import pylab

template = {1:'1-6', 2: '7-11', 3: '12-15', 4: '16-18', 5: '19-20', 6: '21', \
            7: '22', 8: '23', 9: '25', 10: 'personal', 11:'switch'}
def test(trials):
    aggregate = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    temp = []
    first, second, third, fourth, fifth, sixth, seventh, eighth = [],[],[],[],[],[],[],[]
    master = {0:aggregate, 1:first, 2:second, 3:third, 4:fourth, 5:fifth, \
              6:sixth, 7:seventh, 8:eighth, 9:game().cases}
    for i in range(trials):
         temp.append(game().trial())
    for l in temp:
        for i in range(10):
            aggregate[i] += l[i]
        first.append(l[0])
        second.append(l[1])
        third.append(l[2])
        fourth.append(l[3])
        fifth.append(l[4])
        sixth.append(l[5])
        seventh.append(l[6])
        eighth.append(l[7])
    for i in range(10):
        aggregate[i] = round(aggregate[i]/float(trials))
    return master

def compiler(lister):
    while len(lister) > 1:
        lister[0] = lister[0] + lister[1]
    return lister

class game(object):
    def __init__(self):
        self.sum = 3418416.01
        self.turns = {0:[1,7], 1:[7, 12], 2:[12,16], 3:[16,19], 4:[19, 21], 5:[21], 6:[22], \
                      7:[23], 8:[24]}
        self.numCases = {0:20, 1:15, 2:11, 3:8, 4:6, 21:5, 22:4, 23:3}
        self.cases = [.01, 1.0, 5.0, 10.0, 25.0, 50.0, 75.0, 100.0, 200.0, 300.0, 400.0,
                      500.0, 750.0, 1000.0, 5000.0, 10000.0, 25000.0, 50000.0, 75000.0,
                      100000.0, 200000.0, 300000.0, 400000.0, 500000.0, 750000.0, 1000000.0]
        random.shuffle(self.cases)
        self.offers = []


    def trial(self):
        for t in range(5):
            for c in range(self.turns[t][0], self.turns[t][1]):
                self.sum -= self.cases[c]
            self.offers.append(int(self.sum/self.numCases[t]))
        for c in range(21, 24):
            self.sum -= self.cases[c]
            self.offers.append(int(self.sum/self.numCases[c]))
        self.offers.append(self.cases[0])
        self.offers.append(self.cases[25])
        return self.offers

master = test(20000)

##    Set 1 : Median -  133107.0
##    StdDev -  28610.0639301
##
##    Set 2 : Median -  129433.5
##    StdDev -  43532.3770433
##
##    Set 3 : Median -  128469.0
##    StdDev -  59528.4896828
##
##    Set 4 : Median -  128247.0
##    StdDev -  75778.0476191
##
##    Set 5 : Median -  125092.5
##    StdDev -  92578.2253716
##
##    Set 6 : Median -  105180.0
##    StdDev -  103493.145333
##
##    Set 7 : Median -  100319.0
##    StdDev -  120527.339859
##
##    Set 8 : Median -  66908.0
##    StdDev -  144313.26998
##
##    Individual cases: Median - 875
##    StdDev - 253584.4722
