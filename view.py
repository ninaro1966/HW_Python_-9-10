
players = 0
total_candies = 150
max_take = 28
player_take = 0


def get_player() -> int:
    global total_candies
    return total_candies

def set_player(player):
    global players
    players = player


def get_total_candies() -> int:
    global total_candies
    return total_candies

def set_total_candies(new_value: int):
    global total_candies
    total_candies = new_value

def get_max_take():
    global max_take
    return max_take

def set_max_take(new_value: int):
    global max_take
    max_take = new_value

def get_player_take():
    global player_take
    return player_take

def set_player_take(new_value: int):
    global player_take
    player_take = new_value

def check_win(count: int):
    if count > 0:
        return False
    else:
        return True