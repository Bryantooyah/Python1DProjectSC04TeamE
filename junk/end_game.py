class AfterGame:
    def __init__(self, player_scores, player_ships):
        self.player_scores = player_scores
        self.player_ships = player_ships

# Assuming that the list for "player_ships" will be as following format: 
# "Player 1" = [{"name": Destroyer, "destroyed": True, "hits": 4}]

    def check_game_over(self):
        for player, ships in self.player_ships.items():
            for ship in ships:
                if all(ships['destroyed']) == True:
                    return True, player
        return False
    
    def calculate_scores(self, game_time):
        for player, ships in self.player_ships.items():
            total_destroyed = 0
            total_hits = 0
            for ship in ships:
                if ship['destroyed'] == True:
                    total_destroyed += 1
                total_hits += ships['hits']

            self.player_scores[player] += total_destroyed * 20  
            self.player_scores[player] += total_hits * 5

            if game_time < 120:
                self.player_scores[player] += 40        

        return self.player_scores
    
    def return_to_title_screen():
    # IDK WHAT TO DO HERE THERE IS NO CODE YET JUST SUIT YOURSELF
        print("Returning to Title Screen...")

    def after_game_process(self, game_time):
        game_over, losing_player = self.check_game_over()
        if game_over:
            print(f"Game Over! {losing_player} lost all their ships.")
        
        for player in self.player_ships.item():
            if player == losing_player:
                return (f"{player}: 0 points, {player} Lose!")
            else:
                return (f"{player}: {self.calculate_scores(game_time)} points")
            
        self.return_to_title_screen()