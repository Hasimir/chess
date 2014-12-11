#!/usr/bin/env python3

# Used for the first 30 games

player = input("Enter the name of the player: ")
Rc = int(input("Enter the current rating: "))
games = input("Enter the number of games: ")
wins = input("Enter the number of wins: ")
draws = input("Enter the number of draws: ")
rsum = input("Enter sum of all opponents' ratings: ")

g = float(games)
w = float(wins)
d = float(draws)
p = (w + d) / g
# Dp = ?
# Fp = ?

Rc = float(rsum) / g
#Rn = Rc + Dp * Fp

print("The new rating for {0} is: {1}".format(player, str(Rn)))
