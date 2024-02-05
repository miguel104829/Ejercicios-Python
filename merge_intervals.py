def merge_intervals(intervals):
    # Sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If the merged list is empty or the current interval does not overlap with the previous one
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            # Merge the current interval with the previous one
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

merged_intervals = merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
print(merged_intervals)  