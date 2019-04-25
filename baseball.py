# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import sys, os
import re

if(len(sys.argv) < 2):
	sys.exit("Usage: %s filename" % sys.argv[0])

filename = sys.argv[1]

if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % filename)

f = open(filename, "r")

records = {}

for line in f:
	pattern = '(?P<name>[\w\s]+)\sbatted\s(?P<bats>\d)[\w\s]+with\s(?P<hits>\d)'
	match = re.match(pattern, line)

	if match:
		name = match.group('name')
		bat = int(match.group('bats'))
		hit = int(match.group('hits'))

		if name in records:
			records[name][1] += bat
			records[name][2] += hit
		else: 
			records[name] = [name, bat, hit]
f.close()

leaderboard = []
for player in records:
	avg = float(records[player][2]) / float(records[player][1])
	leaderboard.append((player, avg))

leaderboard = sorted(leaderboard, reverse=True, key=lambda player: player[1])

for player in leaderboard:
	print (player[0], ": ", "%.3f" % player[1],sep="")
