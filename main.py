import pandas as pd

print ('Read file')
games_stats = pd.read_csv('20082015games.csv')
print games_stats

print ('Calculate Results')
games_goals = games_stats.GoalsA.values + games_stats.GoalsB.values
games_goals_score = (games_goals <= 2) * 1 + (games_goals > 3) * 3
games_goals_score = (games_goals_score == 0) * 2 + (games_goals_score != 0) * games_goals_score
games_win_score = (games_stats.GoalsA.values > games_stats.GoalsB.values) * 1 + \
                  (games_stats.GoalsA.values < games_stats.GoalsB.values) * 2
games_win_score_A_adv = ((games_stats.GoalsA.values + 1) > games_stats.GoalsB.values) * 1 + \
                        ((games_stats.GoalsA.values + 1) < games_stats.GoalsB.values) * 2
games_win_score_B_adv = (games_stats.GoalsA.values > (games_stats.GoalsB.values + 1)) * 1 + \
                        (games_stats.GoalsA.values < (games_stats.GoalsB.values + 1)) * 2
TeamAnames = games_stats.TeamA.values
TeamBnames = games_stats.TeamB.values
print (TeamAnames, TeamBnames)
