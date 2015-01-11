#!/usr/bin/env python3

# Used for the first 30 games

player = input("Enter the name of the player: ")
Rc = int(input("Enter the current rating: "))
games = input("Enter the number of games: ")
wins = input("Enter the number of wins: ")
draws = input("Enter the number of draws: ")

g = int(games)
w = float(wins)
d = float(draws)
p = (w + d) / g

a = []

for i in range(g):
    r = int(input("Enter the opponent's rating for game {0}: ".format(i + 1)))
    a.insert(0, r)

rsum = sum(a)

# Fp = ?

if 0.99 <= p <= 1:
    Dp = 677
elif 0.98 <= p < 0.99:
    Dp = 589
elif 0.97 <= p < 0.98:
    Dp = 538
elif 0.96 <= p < 0.97:
    Dp = 501

Rc = float(rsum) / g
#Rn = Rc + Dp * Fp

print("The new rating for {0} is: {1}".format(player, str(Rn)))
