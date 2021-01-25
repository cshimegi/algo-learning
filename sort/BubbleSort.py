from sys import stdin, stdout

def Swap(List: list, idx1: int, idx2: int) -> None:
    ''' Swap 2 numbers

    Args:
        List (list): unordered list
        idx1 (int): position of target number 1
        idx2 (int): position of target number 2
    '''
    List[idx1], List[idx2] = List[idx2], List[idx1]

def BubbleSort(List: list) -> list:
    ''' Bubble sort algorithm

    Args:
        List (list): unordered list like [4, 5, 1, 3, 7, 1, 10, 2, 3]

    Returns:
        Sorted list
    '''
    L = len(List)
    for i in range(L):
        for j in range(i+1, L):
            if List[i] > List[j]:
                # if >, sorted list will be in ASC order;
                # if <, sorted list will be in DESC order
                Swap(List, i, j)
    return List

if __name__ == '__main__':
    stdout.writelines('Input should be several numbers separated by space like: 4 5 1 3 7 1 10 2 3\n')
    unorderList = list(map(int, stdin.readline().strip().split(' ')))
    SortedRes = BubbleSort(unorderList)
    stdout.writelines("Result of BubbleSort is: %s\n" % SortedRes)