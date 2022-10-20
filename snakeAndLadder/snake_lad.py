from random import randint


class Player:
    def __init__(self, player_name, grid_size):
        self.name = player_name
        self.dice_history = []
        self.position_history = []
        self.grid = grid_size
        self.winner = 0

    def roll(self, dice):
        self.dice_history.append(dice)
        if self.position_history:
            recent_position = self.position_history[-1]
            new_position = recent_position + dice
        else:
            recent_position = dice
            new_position = recent_position
        if new_position <= self.grid**2:
            self.position_history.append(new_position)
        else:
            self.position_history.append(recent_position)

    def __str__(self):
        return f"Player - {self.name}"


def play():
    grid_size = int(input("Enter the grid size : "))
    players = [
        Player("p1", grid_size),
        Player("p2", grid_size),
        Player("p3", grid_size),
        Player("p4", grid_size),
    ]
    play_on = True
    turns = 0
    while play_on:
        turns += 1
        for player in players:
            dice = randint(1, 6)
            player.roll(dice)
            if grid_size**2 in player.position_history:
                player.winner = 1
                play_on = False
                break

    for player in players:
        print(
            f"{player}  dice_history : {player.dice_history}  position_history : {player.position_history}  winner_status : {player.winner}"
        )


if __name__ == "__main__":
    print("-------------------Snake And Ladder---------------------")
    want_to_play = input("Shall we start ? : ")
    if want_to_play.lower() == "yes" or want_to_play.lower() == "y":
        play()
    else:
        print("Good Bye !")
