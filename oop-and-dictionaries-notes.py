# MAKE OBJECT INSTANCE FROM DICTIONARY DATA:

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# * make object instance from dictionary data:
# * instead of setting instance attributes to values this way:
# ! class Player:
# !     def __init__(self, name, age, position, team):
# !         self.name = name
# !         self.age = age
# !         self.position = position
# !         self.team = team
# player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
# * and testing this way:
# print(player_kevin.name) # Kevin Durant
# print(player_kevin.age) # 34
# print(player_kevin.position) # small forward
# * set instance attributes to values this way:
class Player:
    def __init__(self,dict):
        for key in dict:
            print("key:", key, ",", "value:", dict[key])

# * and test this way:
player_kevin = Player(kevin)