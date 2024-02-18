def gradient_descent(learning_rate, num_epochs, initial_value):
    x = initial_value
    num_epochs = int(num_epochs)  # Convert num_epochs to an integer
    for epoch in range(num_epochs):
        gradient = 2 * x + 5
        x = x - learning_rate * gradient
    return x

learning_rate, num_epochs, initial_value = input().split()

optimal_value = gradient_descent(float(learning_rate), int(num_epochs), float(initial_value))

optimal_value = round(optimal_value, 6)

print(optimal_value, round(optimal_value**2 + 5*optimal_value + 6, 6))
