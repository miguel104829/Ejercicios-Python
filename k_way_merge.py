import heapq

def k_way_merge(*lists):
    merged = []
    heap = []

    # Initialize the heap with the first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    # Merge the lists using the heap
    while heap:
        val, list_index, element_index = heapq.heappop(heap)
        merged.append(val)

        # Move to the next element in the list
        element_index += 1
        if element_index < len(lists[list_index]):
            heapq.heappush(heap, (lists[list_index][element_index], list_index, element_index))

    return merged

# Example usage
list1 = [1, 4, 7]
list2 = [2, 5, 8]
list3 = [3, 6, 9]

merged_list = k_way_merge(list1, list2, list3)
print(merged_list)