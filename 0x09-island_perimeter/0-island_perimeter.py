#!/usr/bin/python3
'''
is island perimeter
'''

def island_perimeter(grid):
	'''
	is island
	'''
	new_grid = grid[1:]
	pos = []
	for idx, row in enumerate(new_grid):
		state = False
		for idx2, col in enumerate(row):
			if col:
				pos = [idx + 1, idx2]
				state = True
				break
		if state:
			break
	if len(pos) < 1:
		return 0
	if not grid[pos[0]][pos[1] + 1]:
		height = 0
		h = pos[0]
		while grid[h][pos[1]]:
			h += 1
			height += 1
		width = 0
		for i in grid[height + pos[0] - 1]:
			if i:
				width += 1
	else:
		width = 0
		w = pos[1]
		while grid[pos[0]][w]:
			w += 1
			width += 1
		height = 0
		h = pos[0]
		while grid[h][width]:
			h += 1
			height += 1
	return 2 * (height + width)
