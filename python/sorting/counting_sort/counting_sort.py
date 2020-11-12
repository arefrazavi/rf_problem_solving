
# Linear time complexity when the elements are in a small range of integers (or other types)
def counting_sort(elements: list):
    max_element = max(elements)
    counts = [0] * (max_element + 1)
    elements_len = len(elements)
    for element in range(elements_len):
        counts[elements[element]] += 1
    elements = []
    for element in range(max_element + 1):
        if counts[element]:
            for i in range(counts[element]):
                elements.append(element)

    return elements

elements = list(map(int, input().rstrip().split()))

elements = counting_sort(elements)

print(*elements, sep=' ')

