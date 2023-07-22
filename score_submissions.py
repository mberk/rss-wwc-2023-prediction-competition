import argparse
import glob
import os

import numpy as np
import pandas as pd


def anonymise_name(name: str) -> str:
    return ''.join(token[0].upper() for token in name.split(' '))


def score_submissions(path_to_submissions_directory: str, path_to_match_results_file: str) -> pd.DataFrame:
    match_results = pd.read_csv(path_to_match_results_file)
    mirrored_match_results = pd.DataFrame(
        {
            'team1': match_results['team2'],
            'team2': match_results['team1'],
            'group': match_results['group'],
            'team1_win': match_results['team2_win'],
            'draw': match_results['draw'],
            'team2_win': match_results['team1_win']
        }
    )
    submissions = {
        os.path.basename(f).replace('.csv', ''): pd.read_csv(f)
        for f in glob.glob(f'{path_to_submissions_directory}/*.csv')
    }

    scores = []
    for name, submission in submissions.items():
        print(f'Scoring {name}')
        if name.startswith('!'):
            # Ignore malformed submission for now
            continue
        df = pd.concat(
            [
                match_results.merge(submission, on=['team1', 'team2', 'group']),
                mirrored_match_results.merge(submission, on=['team1', 'team2', 'group'])
            ]
        )
        assert len(df) == len(match_results)
        # Handle probabilities of 0
        df.loc[df['p_team1_win'] == 0, 'p_team1_win'] = 1e-12
        df.loc[df['p_team2_win'] == 0, 'p_team2_win'] = 1e-12
        df.loc[(df['p_draw'] == 0) & (df['group'] != 'Knockout'), 'p_draw'] = 1e-12
        # Normalise probabilities
        df.loc[df['group'] == 'Knockout', 'p_draw'] = 0
        df['p_team1_win'] = df['p_team1_win'] / df[['p_team1_win', 'p_team2_win', 'p_draw']].sum(axis=1)
        df['p_team2_win'] = df['p_team2_win'] / df[['p_team1_win', 'p_team2_win', 'p_draw']].sum(axis=1)
        df['p_draw'] = df['p_draw'] / df[['p_team1_win', 'p_team2_win', 'p_draw']].sum(axis=1)
        df_group = df[df['group'] != 'Knockout']
        df_ko = df[df['group'] == 'Knockout']
        score = -(np.log(df_group['p_team1_win']) * df_group['team1_win'] + np.log(df_group['p_draw']) * df_group['draw'] + np.log(df_group['p_team2_win']) * df_group['team2_win']).sum()
        score += -(np.log(df_ko['p_team1_win']) * df_ko['team1_win'] + np.log(df_ko['p_team2_win']) * df_ko['team2_win']).sum()
        scores.append({'submission': anonymise_name(name), 'score': score})

    scores = pd.DataFrame(scores).sort_values(['score'])
    return scores


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--submissions-directory',required=True)
    parser.add_argument('--match-results-file', required=True)
    parser.add_argument('--output-file', required=True)

    args = parser.parse_args()

    results = score_submissions(args.submissions_directory, args.match_results_file)
    results.to_csv(args.output_file, index=False)


if __name__ == '__main__':
    main()

