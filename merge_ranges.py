def merge_ranges(meetings):
    # Sort the meetings by start time
    sorted_meetings = sorted(meetings, key=lambda x: x[0])

    # Initialize the merged_meetings list with the first meeting
    merged_meetings = [sorted_meetings[0]]

    # Iterate through the sorted meetings
    for current_start, current_end in sorted_meetings[1:]:
        # Get the last merged meeting
        previous_start, previous_end = merged_meetings[-1]

        # If the current meeting overlaps with the previous one, merge them
        if current_start <= previous_end:
            merged_meetings[-1] = (previous_start, max(previous_end, current_end))
        else:
            # If there is no overlap, add the current meeting to the merged list
            merged_meetings.append((current_start, current_end))

    return merged_meetings

print(merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]))
