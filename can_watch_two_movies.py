def can_watch_two_movies(flight_length, movie_lengths):
    # Create a set to store the movie lengths we have seen so far
    seen_lengths = set()

    # Iterate through each movie length
    for length in movie_lengths:
        # Calculate the remaining time needed to complete the flight
        remaining_time = flight_length - length

        # Check if the remaining time is in the set of seen lengths
        if remaining_time in seen_lengths:
            return True

        # Add the current movie length to the set of seen lengths
        seen_lengths.add(length)

    # No two movies with matching lengths found
    return False

print (can_watch_two_movies(5, [2, 3, 4, 5, 6]))