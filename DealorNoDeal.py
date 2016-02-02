import random
import time
import string

class game(object):
    def __init__(self):
        self.caseStr = "\n        21    22    23    24    25    26  \n       14    15    16    17    18    19    20 \n      7     8     9     10    11    12    13  \n     1     2     3     4     5     6 \n"
        self.board = "\n     $.01    |     $1,000     \n     $1      |     $5,000     \n     $5      |    $10,000     \n     $10     |    $25,000     \n     $25     |    $50,000     \n     $50     |    $75,000     \n     $75     |    $100,000    \n     $100    |    $200,000    \n     $200    |    $300,000    \n     $300    |    $400,000    \n     $400    |    $500,000    \n     $500    |    $750,000    \n     $750    |   $1,000,000  \n "
        self.selectedCases = []
        self.selectedValues = []
        self.turn = 0
        self.player = None
        self.currentSum = 3418416.01
        self.numCases = 26.0
        self.personalCase = None
        self.offer = None
        self.calls = []
        self.choices = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1, 7:1, 8:1, 9:1, 0:1}
        self.genCases()
        self.next_turn()
        
    def next_turn(self):
        if self.turn == 0:
            self.firstTurn()
        if self.turn == 10:
            self.finalTurn()
        self.prompt()
        self.displayBoard()
        self.banker()
        print 'The time has come to make a decision.'
        self.dealnodeal()
 
    def firstTurn(self):
        print
        print 'Welcome to Deal or No Deal!'
        self.pickPersonal()
        a = raw_input("Let's get the game started!")
        print
        self.turn += 1
        self.next_turn()

    def pickPersonal(self):
        self.displayCases()
        print "It's time to pick your first case. You want this case to be the million."
        self.personalCase = input('Which case has the million? - ')
        self.deleteCase(self.personalCase)
        print
        print 'Alright, we shall see. Keep in mind, from here on out, you want low values.'
        print
        

    def finalTurn(self):
        print
        a = raw_input('We are down to the final two cases.')
        items = self.finalCases()
        print 'We have your case, #' + str(self.personalCase) + ',', 'and #' + \
        str(items[0]), 'is on the stage.'
        print 'One of these cases contains', str(items[1][0]) + ', and the other contains', str(items[1][1]) + '.'
        ans = raw_input('Would you like to switch your case for the one onstage? Yes or no? - ').lower()
        if 'n' not in ans and 'y' not in ans:
            raise KeyError
        elif 'y' in ans:
            print "Let's switch the cases. This case contains..."
            time.sleep(.5)
            print '...'
            time.sleep(.6)
            print self.valueConvert(self.cases[items[0]]) + '!'
            self.mil_or_nil(self.cases[items[0]])
            a = raw_input('Thanks for playing!')
            assert False
        else:
            print "Let's see what's been in your case all along..."
            time.sleep(.5)
            print '...'
            time.sleep(.6)
            print self.valueConvert(self.cases[self.personalCase]) + '!'
            self.mil_or_nil(self.cases[self.personalCase])
            a = raw_input('Thanks for playing!')
            assert False
            
        
    def finalCases(self):
        case = None
        for i in range(27):
            if i not in self.selectedCases and i != self.personalCase:
                    case = i
        values = [self.cases[self.personalCase], self.cases[case]]
        for i in values:
            i = self.valueConvert(i)
        random.shuffle(values)
        return [case, values]
        
    def dealnodeal(self):
        ans = raw_input('Deal, or No Deal? - ').lower().strip(string.punctuation)
        if ans != 'deal' and ans != 'no deal':
            print 'I did not understand that. Please type "Deal" or "No Deal"'
            print
            self.dealnodeal()
        elif 'no' not in ans:
            self.takeDeal()
        else:
            print
            a = raw_input('No deal!')
            self.turn += 1
            self.next_turn()

    def takeDeal(self):
        print
        print "Congratulations! You're going home with " + str(self.valueConvert(self.offer)) + '!'
        ans = raw_input("Let's see what was in your case.")
        print 'Your case contained...'
        time.sleep(.6)
        print self.valueConvert(self.cases[self.personalCase]) + '!'
        self.mil_or_nil(self.cases[self.personalCase])
        a = raw_input('Thank you for playing!')
        assert False

    def reveal(self, case):
        print ''
        print "Case #" + str(case), 'contains...'
        time.sleep(.7)
        value = (self.valueConvert(self.cases[case]))
        a = raw_input(str(value) + '!')
        self.deleteValue(self.cases[case])
        self.numCases -= 1

    def prompt(self):
        self.displayCases()
        self.calls = []
        picks = self.choices[self.turn]
        print "I'll need you to pick " + str(picks), 'case(s) this turn.'
        while picks > 0:
            self.calls.append(input('Pick a case from the board. - '))
            if self.calls[-1] < 1 or self.calls[-1] > 26:
                print 'You need to pick a case between one and twenty-six.'
                self.calls.pop()
                picks += 1
            if self.calls[-1] in self.selectedCases:
                print "You've already picked that case."
                self.calls.pop()
                picks += 1
            picks -= 1
        for i in self.calls:
            self.selectedCases.append(i)
            self.deleteCase(i)
            self.reveal(i)

    def banker(self):
        for i in self.calls:
            self.currentSum -= self.cases[i]
        offer = self.currentSum/self.numCases
        if offer >= 10000:
            offer = (round(offer, -3))
        elif offer >= 1000:
            offer = (round(offer - 49, -2))
        elif offer >= 10:
            offer = (round(offer - 4.9, -1))
        self.offer = int(offer)
        print "The banker is calling in his offer..."
        time.sleep(.7)
        print '...'
        time.sleep(.5)
        print "The banker will buy your case for $" + str(self.offer)
        print

    def deleteCase(self, case):
        if len(str(case)) != 2:
            case = ' ' + str(case)
        self.caseStr = self.caseStr.replace(' '+str(case) + ' ', '    ')


    def deleteValue(self, value):
        value = self.valueConvert(value)
        value = value.center(10)
        self.board = self.board.replace(value, '          ')

    def displayCases(self):
        print self.caseStr

    def displayBoard(self):
        print self.board

    def valueConvert(self, value):
        if value < 1.0:
            return '$.01'
        elif value == 1000000.0:
            return '$1,000,000'
        value = '$' + str(int(value))
        if value.count('0') == 3:
            value = value.replace('000', ',000', 1)
        elif value.count('0') == 4:
            value = value.replace('0000', '0,000', 1)
        elif value.count('0') == 5:
            value = value.replace('00000', '00,000', 1)
        return value

    def genCases(self):
        self.cases = [.01, 1.0, 5.0, 10.0, 25.0, 50.0, 75.0, 100.0, 200.0, 300.0, 400.0,
                500.0, 750.0, 1000.0, 5000.0, 10000.0, 25000.0, 50000.0, 75000.0,
                100000.0, 200000.0, 300000.0, 400000.0, 500000.0, 750000.0, 1000000.0]
        random.shuffle(self.cases)
        self.cases.append(self.cases[0])
        self.cases[0] = 0.0

    def mil_or_nil(self, value):
        if type(value) == str:
            value = int(value.strip('$'))
        if value == 1000000:
            print 'Congratulations! You won the million!'
        elif value == 0:
            print 'Well, not many people win the penny. You can be proud of that at least...'
        elif value < 100:
            print "Not much, but enough for a bus ticket home."
        print

    ##def randomOffers(self, choices):
    ##    cases = genCases()
    ##    selectedValues, trialSet = [], []
    ##    for i in range(choices):
    ##        selectedValues.append(cases[i])
    ##        trialSet.append(genOffer(cases, selectedValues))
    ##    return trialSet
    ##        
    ##def compiler(self, trials):
    ##    masterSet = []
    ##    for i in range(25):
    ##        masterSet.append(0.0)
    ##    for i in range(trials):
    ##        trialSet = randomOffers(25)
    ##        for i in range(24):
    ##            masterSet[i] += trialSet[i]
    ##    for i in range(25):
    ##        masterSet[i] = masterSet[i] / float(trials)
    ##    print masterSet
