inputData = input().split()
n = int(inputData[0])
m = int(inputData[1])
startArray = []
global maxElement
global k
global f
for i in range(n):
	startArray.append([ j for j in input().split()])
maxElement = startArray[0][0]
k = 0
f = 0
for i in range(0,int(n)):
	for j in range(0,len(startArray[i])):
		if int(startArray[i][j]) > int(maxElement):
			maxElement = startArray[i][j]
			k = i
			f = j
print(maxElement)
print(k,f)