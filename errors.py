def print_cheese():
    try:
        my_cheese = "pecorino"
        print(my_cheese[12])
    except IndexError:
        print("There was an index error when indexing this string")


def cheese():
    print_cheese()


def calc_square_root(n):
    if type(n) == str:
        raise TypeError("Cannot send string")
    if n < 0:
        raise ValueError("sqrt received a value of {} and cannot be negative".
                         format(n))
    """try:
        from my_calculator import sqrt
    except ModuleNotFoundError:
        print("The my_calculator module was not found."
              "Loading Python math library instead.")
        from math import sqrt"""
    from math import sqrt
    answer = sqrt(n)
    return answer


def sqrt():
    try:
        result = calc_square_root(4)
        print(result)
    except TypeError:
        print("You sent a string.")
    except ValueError:
        print("Don't send a negative number.")
    except Exception:  # captures every possible exception
        print("Something else happened.")
        # Would be good if you can print out what the exception was
    else:
        print("Everything successful!")
    finally:
        print("If there's an error, this still runs.")


if __name__ == "__main__":
    cheese()
    sqrt()
