"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int) -> list[int]:
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """
    # Returns the concatenate rounds
    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """
    # Return a boolean value
    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    average = sum(hand) / len(hand)
    return average


def approx_average_is_average(hand: list[int]) -> bool:
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    # Check the size of the hand
    hand_size = len(hand)

    # Check the first_last index average
    first_last_hand_average = (hand[0] + hand[-1])/2

    # Check the median according to the middle index
    median = hand[int(hand_size / 2)]

    # Returns the real average hand
    average_hand = card_average(hand)
    
    # Returns a boolean value according to the condition
    return average_hand in (first_last_hand_average, median)


def average_even_is_average_odd(hand: list[int]) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand: The list of card values.

    Returns:
        bool: Are the even and odd averages equal?
    """

    # Calculate average using slicing list with step 2: hand[start:stop:step]
    even_average = sum(hand[::2]) / len(hand[::2])
    odd_average = sum(hand[1::2]) / len(hand[1::2])

    # Returns a boolean value
    return even_average == odd_average

def maybe_double_last(hand: list[int]) -> list[int]:
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """
    # Check if the last item corresponds to 11
    if hand[-1] == 11:
        # If the condition it's true, increments 11 to it's atual value
        hand[-1] += 11
    # Returns an int value 
    return hand