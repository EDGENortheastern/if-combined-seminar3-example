import random  # to generate random coefficients


def generate_equation(min_value=1, max_value=10):
    """
    Generates a linear equation of the form ax = b,
    where a and the solution are whole numbers.

    Returns:
        tuple[str, int]: equation as text and the integer solution.
    """
    solution = random.randint(min_value, max_value)
    coefficient = random.randint(min_value, max_value)
    result = coefficient * solution

    equation = f"{coefficient}x = {result}"
    return equation, solution
