# Ria T., Honors Geometry, 1/20/21
# Mariners Challenge Problem
# Count the number of wins vs the number of losses based on Mariners data

def calculate_wins_losses(homeTeamRuns, opponentRuns):
    '''calculate_wins_losses() -> dict
    containing the number of wins/losses/ties'''
    winsLosses = {'wins': 0, 'losses': 0, 'ties': 0} # init dict to track wins, losses, and ties
    for run in range(len(homeTeamRuns)):
        if homeTeamRuns[run] > opponentRuns[run]:
            winsLosses['wins'] += 1
        elif homeTeamRuns[run] < opponentRuns[run]:
            winsLosses['losses'] += 1
        else:
            winsLosses['ties'] += 1
    return winsLosses

def run():
    ''''run() -> analyze mariners
    data and print the results'''
    marinerRuns = [10, 7, 8, 2, 3, 3, 5, 0, 6, 1]
    opponentRuns = [3, 5, 2, 3, 1, 6, 3, 2, 4, 3]
    winsLosses = calculate_wins_losses(marinerRuns, opponentRuns)
    print("The mariners had...")
    for key, value in winsLosses.items():
        print(value, key)

run()
