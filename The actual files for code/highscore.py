class High_Score:
    def __init__(self, file_name="high_score"):
        self.file_name = file_name
    
    # Sample usage:
    # object.save_high_score(160)

    def save_high_score(self, score):
        file = open(self.file_name, 'a')
        file.write(f"{score}")
        file.close()
    
    def load_high_score(self, score):
        high_scores = []
        try:
            file = open(self.file_name, 'r')
            for line in file:
                high_scores.append({"score": int(score)})
        except FileNotFoundError:
            pass
        return high_scores
    
    def display_high_score(self):
        high_scores = self.load_high_score()
        top = 0
        for high_score in high_scores:
            if high_score > top:
                top = high_score
                return (f"High Score: {top}")