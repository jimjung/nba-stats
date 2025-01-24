from nba_api.stats.static import teams
import csv

def fetch_nba_teams():
    # Get all NBA teams
    nba_teams = teams.get_teams()

    # Extract relevant data
    teams_data = [{'name': team['full_name'], 'abbreviation': team['abbreviation']} for team in nba_teams]

    # Save to CSV
    with open('data/nba_teams.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'abbreviation']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for team in teams_data:
            writer.writerow(team)

if __name__ == '__main__':
    fetch_nba_teams() 