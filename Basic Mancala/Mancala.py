
class Mancala:
    def __init__(self):
        """Initialize game"""
        self.board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
        # test whether the cells are printing in the correct order:
        # self.board = []
        # for i in range(14):
        #     self.board.append(i)
        
        self.p1_score = 0
        self.p2_score = 0
        
        self.winner = "TIE"
        self.p1view = None
        self.p2view = None
        self.p1name = None
        self.p2name = None

    def establish_winner(self):
        """Pick current winner based on status of game"""
        if self.board[6] == self.board[13]:
            self.winner = "TIE"
        elif self.board[6] > self.board[13]:
            self.winner = "P1"
        elif self.board[13] > self.board[6]:
            self.winner = "P2"


    def game_over(self):
        """Determine whether the game is over"""
        rval = False #Return Value (True = Game Over, False = Game Not Over)
        
        if self.board[6] + self.board[13] == 48:

            rval = True
        elif sum(self.board[0:6]) == 0:
            self.board[13] += sum(self.board[7:13])
            for i in range(7,13):
                self.board[i] = 0

            rval = True
        elif sum(self.board[7:13]) == 0:
            self.board[6] += sum(self.board[0:6])
            for i in range(0,6):
                self.board[i] = 0

            rval = True

        self.establish_winner()
        return rval

    def p2validmove(self, chosenCell):
        """"Check if player 2's entered move is valid"""
        if len(chosenCell) != 1:
            return -1
        if ord("0") <= ord(chosenCell) <= ord("9"):
            chosenCell = int(chosenCell)
        else:
            return -1
        if 1 <= chosenCell <= 6 and self.board[chosenCell+6] > 0:
            return chosenCell + 6
        else:
            return -1
   
    # def p2validmove(self, chosenCell):
    #     """"Check if player 2's entered move is valid"""
    #     if 7 <= chosenCell <= 12 and self.board[chosenCell] > 0:
    #         return True
    #     else:
    #         return False

    def p2play(self):
        move2 = input("Player2 move:\n")
        #check validity of move
        move2 = self.p2validmove(move2)
        while move2 == -1:
            move2 = input("Invalid input, Player 2 move:\n")
            move2 = self.p2validmove(move2)
        hand, self.board[move2] = self.board[move2], 0
        position = move2 + 1
        while hand != 0: #while hand is not empty
            #time.sleep(1)
            #drop pebbles into every cell except for p1's
            if position == 13:
                self.board[position] += 1
                hand -= 1
                #self.printboard()
                position = 0
            elif position == 6:
                position += 1
            else:
                self.board[position] += 1
                hand -= 1

                if hand == 0 and self.board[position] > 1: # doesn't include 0<=position<=12
                    #print("hand:", hand)
                    #print("position:", position)
                    hand, self.board[position] = self.board[position], 0
                    #print("picking up")
                #self.printboard()
                position += 1
        # return boolean
        if position == 0:
            return True # p2 plays again if the last pebble went into their hole
        return False


    def p1validmove(self, chosenCell):
        """"Check if player 1's entered move is valid"""
        if len(chosenCell) != 1:
            return -1
        if ord("0") <= ord(chosenCell) <= ord("9"):
            chosenCell = int(chosenCell)
        else:
            return -1
        if 1 <= chosenCell <= 6 and self.board[chosenCell-1] > 0:
            return chosenCell - 1
        else:
            return -1

    def p1play(self):
        move1 = input("Player1 move:\n")
        #check validity of move
        move1 = self.p1validmove(move1)
        while move1 == -1:
           move1 = input("Invalid input, Player 1 move:\n")
           move1 = self.p1validmove(move1)

        hand, self.board[move1] = self.board[move1], 0
        position = move1 + 1
        while hand != 0:
            #time.sleep(1)
            #game is currently not ending properly
            if not position == 13:
                self.board[position] += 1
                hand -= 1
                if hand == 0 and self.board[position] > 1 and 0 <= position <= 12 and position != 6:
                    #pick up everything in that cell if there are any other pieces and if it's within p1's range
                    hand, self.board[position] = self.board[position], 0
                    #print("picking up")
                #self.printboard()
                position += 1
            else:
                position = 0
        if position == 7:
            return True # p1 plays again if last cell captured
        return False

    def printWinner(self):
        if self.winner == "TIE":
            print("********  TIE!  ********")
        elif self.winner == "P1":
            print("******** Player 1 WINS! ********")
        elif self.winner == "P2":
            print("******** Player 2 WINS! ********")
    
    def run(self):
        while not self.game_over():
            self.printboard()
            #let p1 play as long as p1.play() returns True
            while not self.game_over() and self.p1play():
                if self.game_over(): # this logic is ugly, but works for now
                    break
                else:
                    self.printboard()
            self.p2_printboard() #show p2 their board before the play
            while not self.game_over() and self.p2play():
                if self.game_over():
                    break
                else:
                    self.p2_printboard()
            
        self.printboard()    
        self.printWinner()
            
                 







    
    def runOLD(self): #OLD FUNCTION 
        # need to fix game over scenario
        while not self.game_over():
            #start a new round
            # self.round_over = False
            # while not self.round_over:
            #call function to allow p1play
            while not self.game_over() and self.p1play(): # this logic is incorrect
                #return True if still playing, return False if p1 move is over
                #print("play continued")
                #self.printboard()
                self.printboard()
            self.establish_winner()
            self.p2_printboard()
            while not self.game_over() and self.p2play():
                #print("play continued")
                self.p2_printboard()
            self.establish_winner()
            self.printboard()
        print("WINNER:", self.winner)



        

    def setcolors(self):
        """Set colors of P1 and P2 to reflect current winner"""
        if self.winner == "TIE":
            #make both player's blue
            self.p1view = "\033[34;1;1m" + str(self.board[6]) + "\033[0m"
            self.p2view = "\033[34;1;1m" + str(self.board[13]) + "\033[0m"
            self.p1name = "\033[34;1;1mP1\033[0m"
            self.p2name = "\033[34;1;1mP2\033[0m"
        elif self.winner == "P1":
            #make P1 green, P2 red
            self.p1view = "\033[32;1;1m" + str(self.board[6]) + "\033[0m"
            self.p2view = "\033[31;1;1m" + str(self.board[13]) + "\033[0m"
            self.p1name = "\033[32;1;1mP1\033[0m"
            self.p2name = "\033[31;1;1mP2\033[0m"
        elif self.winner == "P2":
            #make P2 green, P1 red
            self.p1view = "\033[31;1;1m" + str(self.board[6]) + "\033[0m"
            self.p2view = "\033[32;1;1m" + str(self.board[13]) + "\033[0m"
            self.p1name = "\033[31;1;1mP1\033[0m"
            self.p2name = "\033[32;1;1mP2\033[0m"
    
    def printboard(self):
        """Print the state of the board in p1 view"""
        self.setcolors()
        print("------------------------------------------")
        print("\t|", end="")
        for i in self.board[12:6:-1]:
            if i < 10:
                print(" " + str(i) + " ", end="|")
            else:
                print(" " + str(i), end="|")
        print()
        
        print("   ",self.p2view, " ---------------------------  ", self.p1view)
        print("\t|", end="")
        for i in self.board[:6]:
            if i < 10:
                print(" " + str(i) + " ", end="|")
            else:
                print(" " + str(i), end="|")
        print() #("    " + p1name + "   ")
        print("------------------------------------------")
        print("    " + self.p2name + "  ", end="")
        for i in range(1,7):
            print(f"  {i} ", end="")
        print("     " + self.p1name + "   ")

    def p2_printboard(self):
        """Print the state of the board in p2 view"""
        self.setcolors()
        print("------------------------------------------")
        print("\t|", end="")
        for i in self.board[5::-1]:
            if i < 10:
                print(" " + str(i) + " ", end="|")
            else:
                print(" " + str(i), end="|")
        print()
        
        print("   ",self.p1view, " ---------------------------  ", self.p2view)
        print("\t|", end="")
        for i in self.board[7:13]:
            if i < 10:
                print(" " + str(i) + " ", end="|")
            else:
                print(" " + str(i), end="|")
        print() #("    " + p1name + "   ")
        print("------------------------------------------")
        print("    " + self.p1name + "  ", end="")
        for i in range(1,7):
            print(f"  {i} ", end="")
        print("     " + self.p2name + "   ")


    
    

game = Mancala()
#game.p2_printboard()
#game.printboard()
game.run()
#game.printboard()
