#! /bin/python3

import cmath


def solve_quadratic_equation(a, b, c):
    """This function solves a quadratic equation of the form:
    ax^2 + bx + c = 0
    """
    d = (b**2) - (4*a*c)
    sol1 = (-b - cmath.sqrt(d)) / (2*a)
    sol2 = (-b + cmath.sqrt(d)) / (2*a)
    return sol1, sol2


if __name__ == '__main__':
    # Example usage
    a = 1
    b = 5
    c = 6

    solutions = solve_quadratic_equation(a, b, c)
    print('The results are {0} and {1}'.format(solutions[0], solutions[1]))
