# list of points
# returns number of times the max and min point records are broken

def breakingRecords(scores):
    max = scores[0]
    times_max = 0
    min = scores[0]
    times_min = 0
    result = []
    for item in scores:
        if item > max:
            max = item
            times_max += 1
        if item < min:
            min = item
            times_min += 1
    result.append(times_max)
    result.append(times_min)
    return result

if __name__ == '__main__':
    print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])) # 2, 4