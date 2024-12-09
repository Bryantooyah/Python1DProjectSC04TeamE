from datetime import datetime
import csv
import os

class High_Score:
    def __init__(self, context, file="high_score.csv"):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "high_score.csv")
        self.file = file_path
        self.__context = context

    def save_score(self, username, score, time_taken, mode):
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.file, 'a') as file:
            file.write(f"{username}, {score}, {time_taken}, {date_time}, {mode} \n")
    
    def load_high_score(self):
        high_scores = []
        try:
            with open(self.file, 'r') as file:
                converted_file = csv.reader(file)
                for line in converted_file:
                    high_scores.append({
                        "username": line[0], 
                        "score": line[1], 
                        "time_taken": line[2],
                        "date_time": line[3],
                        "mode": line[4]})
        except FileNotFoundError:
            pass
        return high_scores
    
    def evaluate_high_score(self, username, new_score):
        high_score_list = self.load_high_scores()
        updated = False

        for data in high_score_list:
            if data['username'] == username and data['mode'] == "singleplayer":
                if new_score > data['score']:
                    data['score'] = new_score
                    data['data_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    updated = True
        
        if updated:
            with open(self.file, 'w') as file:
                for data in high_score_list:
                    file.write(f"{data['username']},{data['score']},{data['time_taken']},{data['date_time']},{data['mode']}\n")

        return updated

    def sort_high_scores(self):
        high_score_list = self.load_high_scores()
        singleplayer_scores = [data for data in high_score_list if data['mode'] == "singleplayer"]
        sorted_scores = sorted(singleplayer_scores, key=lambda x: (-x['score'], x['time_taken']))
        return sorted_scores[:10]
    
    def display_high_score(self):
        top_scores = self.sort_high_scores()
        print("Top 10 High Scores (Singleplayer): ")
        for i, data in enumerate(top_scores, 1):
            print(f"{i}. {data['username']} - {data['score']} points (Time: {data['time_taken']} seconds, Played on: {data['date_time']})")


class HistoryLog:
    def __init__(self, context, file="high_score.csv"):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "high_score.csv")
        self.file = file_path
        self.__context = context

    def load_history(self):
        """Loads the game history from the CSV file."""
        game_history = []
        try:
             with open(self.file, 'r') as file:
                converted_file = csv.reader(file)
                for line in converted_file:
                    game_history.append({
                        "username": line[0], 
                        "score": line[1], 
                        "time_taken": line[2],
                        "date_time": line[3],
                        "mode": line[4]})
        except FileNotFoundError:
            print("No game history found. Play a game first!")
        return game_history

    def display_history(self, name):
        """Displays the game history in a readable format."""
        history = self.load_history()
        print(history)
        user_history = [entry for entry in history if entry['username'] == name]

        if not user_history:
            print(f"No game history found for user: {name}")
            return
        
        print(f"\n=== Game History Log for {name} ===")
        for entry in user_history:
            print(f"Player: {entry['username']}, Score: {entry['score']}, Time: {entry['time_taken']}s, Date: {entry['date_time']}, Mode: {entry['mode']}")
        print("========================")
