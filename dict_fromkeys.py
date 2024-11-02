#dict.fromkeys()
fruits={
    "apple":"red",
    "banana":"yellow",
    "grape":"purple"
}
fruit_names=["apple","banana","grapes"]
fruit_dict=dict.fromkeys(fruit_names,"Unknown")
print(fruit_dict)

fruit_dict_default=dict.fromkeys(fruit_names)
print(fruit_dict_default)
#track scores for players in a game
players=["anna","boby","minu"]
scores=dict.fromkeys(players,0)
print(scores)
def update_score(player,points):
    if player in scores:
        scores[player]+=points
    else:
        print(f"{player} not found")
update_score("anna",10)
update_score("sam",10)
print(scores)