#Calculate Team Rating

def get_real_rating(position, player) :
    pass

def calculate_rating(team) :
    return int(sum([get_real_rating(player, team[player]) for key in team])/11)

def test_rating(team, expected_rating) :
    return calculate_rating(team) == expected_rating

