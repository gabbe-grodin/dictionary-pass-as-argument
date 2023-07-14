# Given a list of dictionaries, update the constructor method to accept a dictionary with a single instance's attributes instead of individual arguments for the attributes.
# In other words, put each team into a list of Player object instances:
players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },  
    {  
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard",  
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

# Original constructor:
# ! class Player:
# !     def __init__(self, name, age, position, team):
# !         self.name = name
# !         self.age = age
# !         self.position = position
# !         self.team = team

# * CHALLENGE 1 - Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes:

class Player:
    def __init__(self, player_dict):
        for key in player_dict:
            print(f"{key}: {player_dict[key]}")

# Testing:
# player_1 = Player(players[0])
# player_2 = Player(players[1])
# players[0] = Player(players[0])
# players[6] = Player(players[6]) # expected output: out of range error

# * CHALLENGE 2 - Given these variables create player instances for the following dictionaries:

kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}
# player instances:
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# # * CHALLENGE 3 - Make a list of Player instances from a list of dictionaries:

# first name each dictionary
new_team = []
for idx in range(len(players)):
    new_team.append(players[idx]["name"])
print(f"The New Team is: {new_team}")
