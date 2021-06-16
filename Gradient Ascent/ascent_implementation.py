import math
import matplotlib.pyplot as plt

"""The main advantage to use ascent is to find an absolute maximum or minimum.
    The main disadvantage it's greedy."""


def first_implementation():
    def revenue(tax):
        """This formula was taken from Dive into Algorithms book, It calculates the maximum tax rate with which
        it's possible to collect the maximum revenue"""
        return 100 * (math.log(tax + 1) - (tax - 0.2) ** 2 + 0.04)

    xs = [x/1000 for x in range(1001)]
    ys = [revenue(x) for x in xs]
    plt.plot(xs, ys)
    # to compare a current rate with a calculated one
    current_rate = 0.7
    plt.plot(current_rate, revenue(current_rate), 'ro')
    plt.title('Tax Rates and Revenues')
    plt.xlabel('Tax Rate')
    plt.ylabel('Revenue')
    plt.show()


if __name__ == '__main__':
    first_implementation()
