from random import choice

def ncaa_assignments():
    ballers = ['Zack', 'Ryan', 'James', 'Behnke', 'RyanK', 'Derek', 'Raymond', 'Tyler']
    teams = ['Villanova', 'Texas Tech', 'Kansas', 'Duke', 'Kansas State', 'Loyola', 'Florida State', 'Michigan']

    assignments = {}

    for big_boi in ballers:
        team = choice(teams)
        assignments[big_boi] = team
        teams.remove(team)

    for big_boi, team in assignments.items():
        print(big_boi + ': ' + team)

    print('Good luck, nerds.')

ncaa_assignments()
