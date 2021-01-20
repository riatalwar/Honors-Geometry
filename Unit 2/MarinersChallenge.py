def calculate_wins_losses(homeTeamRuns, opponentRuns)
    winsLosses = {'wins': 0, 'losses': 0, 'ties': 0}
    for run in range(len(homeTeamRuns)):
        if homeTeamRuns[run] > opponentRuns[run]:
            winsLosses['wins'] += 1
        elif homeTeamRuns[run] < opponentRuns[run]:
            winsLosses['losses'] += 1
        else:
            winsLosses['ties'] += 1
    return winsLosses
