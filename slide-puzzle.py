def possibleFollowingGridPatterns(gridPattern):
	return [gridPatternAfterSliding(slidingTile, gridPattern) for slidingTile in slidingTiles(gridPattern)]

def gridPatternAfterSliding(tileToSlide, gridPattern):
	return {(row, col): cellContentAfterSliding(tileToSlide, cellContent) for ((row, col), cellContent) in gridPattern.items()}

def cellContentAfterSliding(tileToSlide, cellContent):
	return tileToSlide if isEmpty(cellContent) else emptyCellContent() if tileToSlide == cellContent else cellContent

def slidingTiles(gridPattern):
	return [cellContent for ((row, col), cellContent) in gridPattern.items() if areAdjacentPositions((row, col), emptyCellPosition(gridPattern))]

def areAdjacentPositions(pos1, pos2):
	return (pos1[0]==pos2[0] and (pos1[1]+1==pos2[1] or pos1[1]-1==pos2[1])) or (pos1[1]==pos2[1] and (pos1[0]+1==pos2[0] or pos1[0]-1==pos2[0]))

def emptyCellPosition(gridPattern):
	return [(row, col) for ((row, col), cellContent) in gridPattern.items() if isEmpty(cellContent)][0]

def isEmpty(cellContent):
	return cellContent == emptyCellContent()

def emptyCellContent():
	return 0

def heuristic(gridPattern, targetGridPattern):
	return print([distance(pos1, pos2) for (pos1, pos2) in zip(gridPattern.keys(), targetGridPattern.keys())])

def distance(pos1, pos2):
	return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])



def printPossibleFollowingGridPatterns(gridPattern):
	for possibleFollowingGridPattern in possibleFollowingGridPatterns(gridPattern):
		print()
		printGridPattern(possibleFollowingGridPattern)

def printGridPattern(gridPattern):
	aux = ""
	for i in range(1,4):
		aux = "|"
		for j in range(1,4):
			aux+=str(gridPattern.get((i,j)))+"|"
		print(aux)

initialGrindPattern = {(1,1): 5, (1,2): 1, (1,3): 4, (2,1): 3, (2,2): emptyCellContent(), (2,3): 6, (3,1): 7, (3,2): 2, (3,3):8}
targetGrindPattern = {(1,1): 5, (1,2): 1, (1,3): 4, (2,1): 3, (2,2): 8, (2,3): 6, (3,1): 7, (3,2): 2, (3,3): emptyCellContent()}
heuristic(initialGrindPattern, targetGrindPattern)
print()
printGridPattern(initialGrindPattern)
print()
print("=======")
printPossibleFollowingGridPatterns(initialGrindPattern)
