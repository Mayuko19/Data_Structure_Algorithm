from typing import List

def InsertionSort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i-1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
            numbers[j+1] = temp
    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(1, 1000) for i in range(10)]
    print(InsertionSort(nums))
