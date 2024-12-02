class TennisGame:
    # score constant
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    MIN_SCORE_TO_WIN = 4
    
    POINT_NAMES = {
        LOVE: "Love",
        FIFTEEN: "Fifteen",
        THIRTY: "Thirty",
        FORTY: "Forty"
    }

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0 # change the name
        self.player2_score = 0 # change the name

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self._get_tied_score()
        elif self.player1_score >= self.MIN_SCORE_TO_WIN or self.player2_score >= self.MIN_SCORE_TO_WIN:
            return self._get_advantage_or_win_score()
        else:
            return self._get_regular_score()

    def _get_tied_score(self):
        if self.player1_score == self.LOVE:
            return "Love-All"
        elif self.player1_score == self.FIFTEEN:
            return "Fifteen-All"
        elif self.player1_score == self.THIRTY:
            return "Thirty-All"
        else:
            return "Deuce"    
        
    def _get_advantage_or_win_score(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
        
    def _get_regular_score(self):
        score1 = self.POINT_NAMES[self.player1_score]
        score2 = self.POINT_NAMES[self.player2_score]
        return f"{score1}-{score2}"