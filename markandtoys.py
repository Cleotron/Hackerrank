#max number of toys that can be purchased for a k price

import itertools

def maximumToys(prices, k):
    '''
    available_items = []
    for item in prices:
        if item <= k:
            available_items.append(item)
    
    for i in range(len(available_items), 1, -1):
        for x in list(itertools.combinations(available_items, i)):
            print(x)
            print(sum(x))
            if (sum(x)) <= k:
                return len(x)
    '''
    sum = 0
    num_items = 0
    sorted_prices = sorted(prices)
    for item in sorted_prices:
        if sum + item <= k:
            sum = sum + item
            num_items += 1
        else:
            return num_items


if __name__ == '__main__':
    print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50)) # 4   
    print(maximumToys([1, 2, 3, 4], 7)) # 3