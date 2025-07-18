# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        winner = 0
        if len(player1_word) > len(player2_word):
            winner = 1
        if len(player1_word) < len(player2_word):
            winner = 2
        return winner

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        winner = 0
        player1_count = self.vowel_counter(player1_word)
        player2_count = self.vowel_counter(player2_word)
        if player1_count > player2_count:
            winner = 1
        if player1_count < player2_count:
            winner = 2
        return winner
    
    def vowel_counter(self, word: str):
        vowels = "aeiou"
        count = 0
        for char in word:
            for vowel in vowels:
                if char == vowel:
                    count += 1
        return count

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        winner = 0
        # first check if their inputs are both valid
        eligibility1 = self.valid_input(player1_word)
        eligibility2 = self.valid_input(player2_word)
        if eligibility1 == True and eligibility2 == False:
            winner = 1
        elif eligibility1 == False and eligibility2 == True:
            winner = 2
        elif eligibility1 == False and eligibility2 == False:
            winner = 0
        # if both are valid, then check the results
        elif eligibility1 == True and eligibility2 == True:
            # same hands -> tie
            if player1_word == player2_word:
                winner = 0
            elif player1_word == "rock":
                if player2_word == "paper":
                    winner = 2
                elif player2_word == "scissors":
                    winner = 1
            elif player1_word == "paper":
                if player2_word == "rock":
                    winner = 1
                elif player2_word == "scissors":
                    winner = 2
            elif player1_word == "scissors":
                if player2_word == "rock":
                    winner = 2
                elif player2_word == "paper":
                    winner = 1
        return winner

    def valid_input(self, word):
        valid_list = ["rock", "paper", "scissors"]
        if word in valid_list:
            return True
        else:
            return False
    
    # 1 invalid input - that player loses
    # 2 invalid inputs - tie

if __name__ == "__main__":
    p = RockPaperScissors(4)
    p.play()
