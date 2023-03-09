#!/usr/bin/python3
"""
Module: Prime game
"""


def prime(n):
    """
    A game of choosing prime numbers

    Args:
        n (int): Upper boundary of the range of numbers
    Return:
        A list of prime numbers between 1 and n inlcusive
    """
    primeNumbers = []
    filtered = [True] * (n + 1)

    for primeNo in range(2, n + 1):
        if (filtered[primeNo]):
            primeNumbers.append(primeNo)

            for i in range(primeNo, n + 1, primeNo):
                filtered[i] = False

    return primeNumbers


def isWinner(x, nums):
    """
    Determines the winner of the prime game

    Args:
        x (int): Number of rounds in the game
        nums: An array of n numbers
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    Maria = Ben = 0

    for i in range(x):
        primeNumbers = prime(nums[i])

        if len(primeNumbers) % 2 == 0:
            Maria += 1
        else:
            Ben += 1

        if Ben > Maria:
            return 'Ben'
        elif Maria > Ben:
            return 'Maria'

        return None
