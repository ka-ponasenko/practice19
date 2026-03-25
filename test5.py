from tsk5 import Game

game_one = Game({'command1': 'Юта Джаз', 'command2': 'Майами Хит'})
game_one.ball_throw(1, 2)
game_one.ball_throw(1, 3)
game_one.ball_throw(2, 2)
game_one.ball_throw(1, 1)
print(game_one.get_score()) 
game_one.ball_throw(2, 3)
game_one.ball_throw(2, 2)
game_one.ball_throw(1, 2)
print(game_one.get_score()) 
print(game_one.get_winner())