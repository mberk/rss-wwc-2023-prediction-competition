import pandas as pd
from itertools import combinations

# Dictionary of teams and their groups
team_to_group = {
    'New Zealand': 'A',
    'Norway': 'A',
    'Philippines': 'A',
    'Switzerland': 'A',
    'Australia': 'B',
    'Republic of Ireland': 'B',
    'Nigeria': 'B',
    'Canada': 'B',
    'Spain': 'C',
    'Costa Rica': 'C',
    'Zambia': 'C',
    'Japan': 'C',
    'England': 'D',
    'Haiti': 'D',
    'Denmark': 'D',
    'China PR': 'D',
    'USA': 'E',
    'Vietnam': 'E',
    'Netherlands': 'E',
    'Portugal': 'E',
    'France': 'F',
    'Jamaica': 'F',
    'Brazil': 'F',
    'Panama': 'F',
    'Sweden': 'G',
    'South Africa': 'G',
    'Italy': 'G',
    'Argentina': 'G',
    'Germany': 'H',
    'Morocco': 'H',
    'Colombia': 'H',
    'Korea Republic': 'H'
}

# Create group stage DataFrame
df_group = pd.DataFrame(
    {
        'team1': team1,
        'team2': team2,
        'group': team_to_group[team1],
        'p_team1_win': None,
        'p_team2_win': None,
        'p_draw': None,
    }
    for team1, team2 in combinations(team_to_group.keys(), 2)
    if team_to_group[team1] == team_to_group[team2]
)

# Create knockout stage DataFrame
df_knockout = pd.DataFrame(
    {
        'team1': team1,
        'team2': team2,
        'group': 'Knockout',
        'p_team1_win': None,
        'p_team2_win': None,
        'p_draw': None,
    }
    for team1, team2 in combinations(team_to_group.keys(), 2)
)

df = pd.concat((df_group, df_knockout))
df.to_csv('submission-template.csv', index=False)
