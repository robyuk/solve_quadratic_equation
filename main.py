from solve_quadratic_equation import solve_quadratic_equation

if __name__ == '__main__':
    # Example usage of the solve_quadratic_equation function
    a = 1
    b = 5
    c = 6

    solutions = solve_quadratic_equation(a, b, c)
    print('The results are {0} and {1}'.format(solutions[0], solutions[1]))
