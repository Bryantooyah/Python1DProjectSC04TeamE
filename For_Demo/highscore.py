from datetime import datetime
import csv
import os

class High_Score:
    def __init__(self, file="high_score.csv"): 
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "high_score.csv")
        self.file = file_path

    def save_score(self, username, score, time_taken, mode, condition):
        # Save a new high score to the CSV file with specific details
        time_taken = round(time_taken)
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.file, 'a') as file:
            file.write(f"{username}, {score}, {time_taken}, {date_time}, {mode}, {condition}\n")
    
    def load_high_score(self):
    # Load high scores from the CSV file and append the best records for each user to a list
        high_scores = []
        try:
            with open(self.file, 'r') as file:
                converted_file = csv.reader(file)
                for line in converted_file:
                    line = [data.strip() for data in line]
                    if len(line) >= 6 and line[5] == "Win":
                        username = line[0]
                        score = int(line[1])
                        time_taken = int(line[2])
                        existing_record = next((record for record in high_scores if record['username'] == username), None)

                        if existing_record:
                            existing_score = int(existing_record['score'])
                            existing_time = int(existing_record['time_taken'])

                            if (
                                score > existing_score or
                                (score == existing_score and time_taken < existing_time)
                            ):
                                existing_record.update({
                                    "score": str(score),
                                    "time_taken": str(time_taken),
                                    "date_time": line[3],
                                    "mode": line[4]
                                })
                        else:
                            high_scores.append({
                                "username": username,
                                "score": str(score), 
                                "time_taken": str(time_taken),
                                "date_time": line[3],
                                "mode": line[4]
                            })
        except FileNotFoundError:
            pass
        return high_scores

    def sort_high_scores(self):
        # Sort high scores for single-player mode by score (descending) and time taken (ascending).
        # Return the top 10 scores in a list. 
        high_score_list = self.load_high_score()
        singleplayer_scores = [data for data in high_score_list if data['mode'] == "singleplayer"]
        sorted_scores = sorted(singleplayer_scores, key=lambda x: (
            -int(x['score']) if x['score'].lstrip('-').isdigit() else float('-inf'),
            int(x['time_taken']) if x['time_taken'].isdigit() else float('inf')
        ))
        return sorted_scores[:10]
    
    def display_high_score(self):
        # Display the top 10 high scores for single-player mode.
        top_scores = self.sort_high_scores()
        print("Top 10 High Scores (Singleplayer): ")
        for i, data in enumerate(top_scores, 1):
            print(f"{i}. {data['username']} - {data['score']} points (Time: {data['time_taken']} seconds, Played on: {data['date_time']})")

class HistoryLog:
    def __init__(self, file="high_score.csv"):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "high_score.csv")
        self.file = file_path

    def load_history(self):
        # Loads the game history from the highscore.csv.
        game_history = []
        try:
             with open(self.file, 'r') as file:
                converted_file = csv.reader(file)
                for line in converted_file:
                    if line == []:
                        continue
                    game_history.append({
                        "username": line[0], 
                        "score": line[1], 
                        "time_taken": line[2],
                        "date_time": line[3],
                        "mode": line[4],
                        "win_loss": line[5]})
        except FileNotFoundError:
            print("No game history found. Play a game first!")
        return game_history

    def display_history(self, name):
        # Displays the game history.
        history = self.load_history()
        user_history = [entry for entry in history if entry['username'] == name]

        if not user_history:
            print(f"No game history found for user: {name}")
            return
        
        print(f"\n=== Game History Log for {name} ===")
        for entry in user_history:
            print(f"Player: {entry['username']}, Score: {entry['score']}, Time: {entry['time_taken']}s, Date: {entry['date_time']}, Mode: {entry['mode']}, Result: {entry['win_loss']}")
        print("========================")