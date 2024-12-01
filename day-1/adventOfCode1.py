left = []
right = []
with open("./lists.txt","r") as file:
    content = file.read()
    items=content.split()
    for index in range(len(items)):
        if index%2 !=0: #index is odd
            right.append(int(items[index]))
        else:
            left.append(int(items[index]))


left = sorted(left)
right = sorted(right)


diff=0
similarityScore = 0
for index in range(len(left)):
    currentDiff = abs(left[index] - right[index])
    diff = diff + currentDiff
    currentNumber = left[index]
    appearance = right.count(currentNumber)
    #print("Apperance: ", appearance)
    similarityScore = similarityScore + (appearance*currentNumber)

    
print("Total Diff: ", diff)
print("Similary Score: ", similarityScore)