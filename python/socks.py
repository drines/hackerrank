#!/bin/python3



# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = {}
    total_pairs = 0
    for sock in ar:
        if sock in pairs:
            pairs[sock] += 1
        else:
            pairs[sock] = 1
    for count in pairs:
        total_pairs += pairs[count] // 2

    return total_pairs


if __name__ == '__main__':
    print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
