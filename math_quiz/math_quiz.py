import random


def get_random_int(min_val, max_val) -> int:
    """
    Generates a random integer between the two numbers min_val and max_val.

    Parameters:
    min_val (int): The minimum value of the random integer.
    max_val (int): The maximum value of the random integer.

    Returns:
    int: A random integer between min_val and max_val.
    """

    try:
        # Ensure minimum is less than max
        if min_val > max_val:
            raise ValueError("the minimum value should not be greater than maximum value.")

        # Check if numbers are integers
        if not isinstance(min_val, int) or not isinstance(max_val, int):
            raise TypeError("Both the minimum and maximum value must be integers.")

        return random.randint(min_val, max_val)

    except ValueError as ve:
        print(f"ValueError: {ve}")
        # Provide a default range to avoid program interruption
        return random.randint(1, 10)

    except TypeError as te:
        print(f"TypeError: {te}")
        # Provide a default range to avoid program interruption
        return random.randint(1, 10)


def get_random_operator() -> str:
    """
    Select a random arithmetic operator from the list ['+', '-', '*'].

    Returns:
    str: A random operator, either '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def calculate_operation(number_1, number_2, operator) -> tuple:
    """
    Perform a calculation based on the given operator and two numbers.

    Parameters:
    number_1 (int or float): The first number.
    number_two (int or float): The second number.
    operator (str): The arithmetic operator, which can be '+', '-', or '*'.

    Returns:
    tuple: A tuple containing the operation as a string and the result of the operation.
    """
    # operation is a string, describing the calculation
    operation = f"{number_1} {operator} {number_2}"

    # differentiation between the given operator and the following calculation
    if operator == '-':
        result = number_1 - number_2
    elif operator == '+':
        result = number_1 + number_2
    else:
        result = number_1 * number_2
    return operation, result


def math_quiz() -> None:
    """
    Conducts a math quiz game where the user is presented with math problems and needs to provide the correct answers.
    The game consists of a fixed number of questions, and the user's score is displayed at the end.

    The function does not take any parameters and does not return any value.
    """
    score = 0
    num_questions = 3  # Number of questions in the quiz should be integer to be used as loop counter

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for counter in range(num_questions):
        number_1 = get_random_int(min_val=1, max_val=10)
        number_2 = get_random_int(min_val=1, max_val=5)  # random.randint takes only integer values
        operator = get_random_operator()

        question, answer = calculate_operation(number_1=number_1, number_2=number_2, operator=operator)
        print(f"\nQuestion: {question}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{num_questions}")


if __name__ == "__main__":
    math_quiz()
