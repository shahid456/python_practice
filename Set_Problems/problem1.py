def average(array):
    # your code goes here
    d_heights=set(array)
    return sum(d_heights)/len(d_heights)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)