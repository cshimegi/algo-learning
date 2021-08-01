from sys import stdin, stdout

def swap(_list: list, idx1: int, idx2: int) -> None:
    ''' Swap 2 numbers

    Args:
        _list (list): unordered list
        idx1 (int): position of target number 1
        idx2 (int): position of target number 2
    '''
    _list[idx1], _list[idx2] = _list[idx2], _list[idx1]

def bubbleSort(_list: list) -> list:
    ''' Bubble sort algorithm

    Args:
        _list (list): unordered list like [4, 5, 1, 3, 7, 1, 10, 2, 3]

    Returns:
        Sorted list
    '''
    L = len(_list)
    for i in range(L):
        for j in range(i+1, L):
            if _list[i] > _list[j]:
                # if >, sorted list will be in ASC order;
                # if <, sorted list will be in DESC order
                swap(_list, i, j)
    return _list

if __name__ == '__main__':
    stdout.writelines('Input should be several numbers separated by space like: 4 5 1 3 7 1 10 2 3\n')
    unorderList = list(map(int, stdin.readline().strip().split(' ')))
    sortedRes = bubbleSort(unorderList)
    stdout.writelines("Result of BubbleSort is: %s\n" % sortedRes)