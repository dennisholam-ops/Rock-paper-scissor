import random
from collections import Counter

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    else:
        opponent_history.clear()
    
    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])
    
    
    quincy_pattern = ["R", "R", "P", "P", "S"]
    if len(opponent_history) >= 5:
        is_quincy = True
        for i in range(min(10, len(opponent_history))):
            if opponent_history[i] != quincy_pattern[i % 5]:
                is_quincy = False
                break
        if is_quincy:
            next_move = quincy_pattern[len(opponent_history) % 5]
            if next_move == "R": return "P"
            if next_move == "P": return "S"
            if next_move == "S": return "R"
    
    
    for order in [3, 2]:
        if len(opponent_history) > order:
            pattern = tuple(opponent_history[-order:])
            next_moves = []
            for i in range(len(opponent_history) - order):
                if tuple(opponent_history[i:i+order]) == pattern:
                    next_moves.append(opponent_history[i + order])
            if next_moves:
                prediction = Counter(next_moves).most_common(1)[0][0]
                if prediction == "R": return "P"
                if prediction == "P": return "S"
                if prediction == "S": return "R"
    
    recent_moves = opponent_history[-10:] if len(opponent_history) >= 10 else opponent_history
    if recent_moves:
        most_common = Counter(recent_moves).most_common(1)[0][0]
        if most_common == "R": return "P"
        if most_common == "P": return "S"
        if most_common == "S": return "R"
    
    
    if opponent_history:
        last_move = opponent_history[-1]
        if last_move == "R": return "P"
        if last_move == "P": return "S"
        if last_move == "S": return "R"
    
    return random.choice(["R", "P", "S"])
