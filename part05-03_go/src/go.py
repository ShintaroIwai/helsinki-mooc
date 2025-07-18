# Write your solution here
def who_won(game_board: list):
    player1_score = 0
    player2_score = 0
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                player1_score += 1
            if game_board[i][j] == 2:
                player2_score += 1
    
    if player1_score > player2_score:
        return 1
    elif player1_score < player2_score:
        return 2
    else:
        return 0
    
if __name__ == "__main__":
    test1 = who_won([[1, 2, 1], [0, 0, 1], [2, 1, 0]])
    test2 = who_won([[1, 0, 2, 2, 0, 2], [2, 1, 2, 0, 0, 2], [0, 1, 0, 2, 1, 2], [1, 2, 2, 0, 2, 0], [0, 0, 1, 0, 1, 1], [1, 0, 1, 1, 0, 1]])
    print(test1)
    print(test2)