# Christopher Oliveira
# Program to calculate and display your Deadlock(game) player statistics.

def calculate_kd(kills,deaths):
    if deaths == 0:
        return kills
    else:
        return kills / deaths
# FUNCTIONS FOR CALCULATING KD AND KDA
def calculate_kda(kills,assists,deaths):
    if deaths == 0:
        return kills + assists
    else:
        return (kills + assists) / deaths

# Determines your deadlock "rank" based on your performance score (KDA) Higher score = higher rank
def ranking(performance_score):
    if performance_score >= 25:
        return "Eternus"
    elif performance_score >= 16:
        return "Ascendant"
    elif performance_score >= 9:
        return "Phantom"
    elif performance_score >= 4:
        return "Archon"
    else:
        return "Initiate"
# To make sure user input is a number
def check_number(message):
    number = input(message)

    while not number.isdigit():
        print("Invalid! Please enter a number.")
        number = input(message)
    return int(number)

print("     DEADLOCK PLAYER STATS")
# Using * to repeat "-" to create a divider.
print("-" * 35)

username = input("Enter your username: ")
kills = check_number("Enter your kills: ")
deaths = check_number("Enter your deaths: ")
assists = check_number("Enter your assists: ")
souls = check_number("Enter your souls: ")
minutes = check_number("Enter length of match in minutes: ")
wins = check_number("Enter your wins: ")
losses = check_number("Enter your losses: ")
team_kills = kills #asks for the kills of your other teammates to get your kill participation in the game
for player in range(1,6):
    teammate_kills = check_number("Enter teammate " + str(player) + " kills: ")
    team_kills += teammate_kills


# Calculates total games
total_games = wins + losses
game_difference = wins - losses
# Calculate user KD
killratio = calculate_kd(kills,deaths)
#Calculate user KDA
kda = calculate_kda(kills,assists,deaths)
# Squares the KDA to make a personal custom performance score
performance_score = kda ** 2
player_rank = ranking(performance_score)
# Calculate winrate based on total games then convert into a percentage
if total_games == 0:
    winrate = 0
else:
    winrate = (wins / total_games) * 100
# Calculate souls earned per minute
if minutes == 0:
    souls_per_minute = 0
else:
    souls_per_minute = souls / minutes
# Calculate kill participation percentage with your contributed kills and assists
if team_kills == 0:
    kill_participation = 0
else:
    kill_participation = ((kills + assists) / team_kills) * 100
print()
print("-" * 10,"RESULTS", "-" * 10)
print("Username: " + username)
print("Kills:",kills)
print("Deaths:",deaths)
print("Assists:",assists)
# Using end= to keep KD ratio and KDA on the same line since they are similar stats
print("KD Ratio:", format(killratio, ".2f"), end=" | ")
print("KDA:",format(kda,".2f"))
print("Performance Score:", format(performance_score, ".0f"))
print("Player Rank:", player_rank)
if kills >= 15 and kda >= 3:
    print("Great performance! You got at least 15 kills!")
elif kills >= 10:
    print("Good game!")

if deaths > 10 or kills == 0:
    print("Tough match!")

print("-" * 10,"Soul Statistics", "-" * 10)
print("Souls:",souls)
print("Soul Per Minute:", format(souls_per_minute,".2f"))
print("Match Length:",minutes,"minutes")
print("-" * 10,"Win / Losses", "-" * 10)
print("Wins:",wins)
print("Losses:",losses)
print("Total Games:",total_games)
if total_games != 0:
    print("You have completed", total_games, "games!")
# Using sep="" lets me remove the extra space between winrate and the percent sign. Outputs as winrate%
print("Win Rate: ", format(winrate, ".2f"), "%", sep="")
print("Win/Loss Difference:", game_difference)
print("-" * 10, "TEAM CONTRIBUTION", "-" * 10)
print("Team Total Kills:", team_kills)
print("Kill Participation:", format(kill_participation, ".2f"), "%", sep="")



