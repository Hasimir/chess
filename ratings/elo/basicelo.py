#!/usr/bin/env python3

# Rn = Ro + (K / 2) * (W - L + 0.5 * (Ds / C))

player = input("Enter the name of the player: ")
Ro = int(input("Enter the current rating: "))
score = float(input("Enter the (tournament) score (1 for win, 0.5 draw, 0 loss): "))
games = float(input("Enter the number of games: "))
diffs = float(input("Enter the sum of the difference in ratings: "))

loss = games - score
K = 20
C = 200

Rn = Ro + (K / 2) * (score - loss + 0.5 * (diffs / C))

print("The new rating for {0} is: {1}".format(player, str(Rn)))
