# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, a


def quick_sort(sequence):
    length = len(sequence)
    if length  <= 1:
        return sequence
    else:
        pivot = sequence.pop()


        items_greater = []
        items_less = []

        for item in sequence:
            if item > pivot:
                items_greater.append(item)
            else: items_less.append(item)

        return quick_sort(items_less) + [pivot] + quick_sort(items_greater)


print(quick_sort([1,5,4,3,5,6,3,5]))


