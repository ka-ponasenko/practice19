class Game:
    """A basketball game class that manages scores between two teams."""
    
    def __init__(self, teams: dict):
        """
        Initialize a new basketball game with two teams.
        
        Args:
            teams (dict): A dictionary containing team information with keys:
                - 'command1': name of the first team
                - 'command2': name of the second team
        """
        self.teams = {
            1: teams['command1'],
            2: teams['command2']
        }
        self.scores = {
            1: 0,
            2: 0
        }
    
    def ball_throw(self, command: int, points: int):
        """
        Add points to the specified team.
        
        Args:
            command (int): The team number (1 for first team, 2 for second team)
            points (int): The number of points scored
        """
        if command in self.scores:
            self.scores[command] += points
    
    def get_score(self) -> tuple:
        """
        Get the current score of the game.
        
        Returns:
            tuple: A tuple containing (score_team1, score_team2)
        """
        return (self.scores[1], self.scores[2])
    
    def get_winner(self) -> str:
        """
        Determine the winner of the game.
        
        Returns:
            str: The name of the winning team, or 'Ничья' if the game is tied
        """
        if self.scores[1] > self.scores[2]:
            return self.teams[1]
        elif self.scores[2] > self.scores[1]:
            return self.teams[2]
        else:
            return 'Ничья'

