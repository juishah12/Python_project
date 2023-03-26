class points:
    team_name=None

def get_football_points(wins, draws, losses):
    wins = wins * 3
    draws = draws * 1
    losses = losses * 0
    points = (wins + draws + losses)
    return points