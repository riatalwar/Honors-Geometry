def calculate_wins_losses(homeTeamRuns, opponentRuns):
    winsLosses = {'wins': 0, 'losses': 0, 'ties': 0}
    for run in range(len(homeTeamRuns)):
        if homeTeamRuns[run] > opponentRuns[run]:
            winsLosses['wins'] += 1
        elif homeTeamRuns[run] < opponentRuns[run]:
            winsLosses['losses'] += 1
        else:
            winsLosses['ties'] += 1
    return winsLosses

def run():
    marinerRuns = [10, 7, 8, 2, 3, 3, 5, 0, 6, 1]
    opponentRuns = [3, 5, 2, 3, 1, 6, 3, 2, 4, 3]
    winsLosses = calculate_wins_losses(marinerRuns, opponentRuns)
    print("The mariners had...")
    for key, value in winsLosses.items():
        print(value, key)

run()
