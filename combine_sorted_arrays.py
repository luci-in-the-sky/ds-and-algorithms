# Example 3: Given two sorted integer arrays arr1 and arr2,
# return a new array that combines both of them and is also sorted.

def combine_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    max_length = max(len(arr1), len(arr2))
    combined_array = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            combined_array.append(arr1[i])
            i += 1
        else:
            combined_array.append(arr2[j])
            j += 1

    while i < len(arr1):
        combined_array.append(arr1[i])
        i += 1

    while j < len(arr2):
        combined_array.append(arr2[j])
        j += 1
    return combined_array

if __name__ == '__main__':
    print(combine_arrays([1,10], [1,4,5,20]))