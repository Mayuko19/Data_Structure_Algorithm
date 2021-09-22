from typing import List

def selectction_sort (numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        temp = i
        for j in range(i+1, len_numbers):
            if numbers[temp] > numbers[j]:
                temp = j
        numbers[i], numbers[temp] = numbers[temp], numbers[i]
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(1, 1000) for i in range(10)]
    print(selectction_sort(nums))
