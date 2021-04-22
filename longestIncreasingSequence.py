def longestSequence(string):
    numbers = string.split(" ")
    numbers = [int(x) for x in numbers]
    # return type(numbers[0])
    maxLength = 1
    maxStart = 0
    curStart = 0
    curLength = 1
    for i in range(1,len(numbers)):
        if numbers[i] <= numbers[i-1]:
            if curLength > maxLength:
                maxLength = curLength
                maxStart = curStart
            curStart = i
            curLength = 1
        else: 
            curLength += 1
    if curLength > maxLength:
        maxLength = curLength
        maxStart = curStart
    numbers = [str(x) for x in numbers]
    return " ".join(numbers[maxStart:maxStart+maxLength])