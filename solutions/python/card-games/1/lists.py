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
    # Instance of list[int] which will start with the number passed as a parameter
    numbers_list = [number]

    # Loop for increments and appends numbers in the list
    for _ in range(2):
        numbers_list.append(numbers_list[-1]+1)
    return numbers_list


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    total = rounds_1 + rounds_2
    return total


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """
    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    average = 0.0
    hand_length = len(hand)
    
    for i in range(hand_length):
        average += hand[i]
    average = average / hand_length
    return average


def approx_average_is_average(hand: list[int]) -> bool:
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    #Check the size of the hand
    hand_size = len(hand)

    #Check the first_last index average
    first_last_hand_average = (hand[0] + hand[-1])/2

    #Check the median according to the middle index
    median = hand[int(hand_size / 2)]

    #Returns the real average hand
    average_hand = card_average(hand)
    
    # Checks if the first_last hand average equals to the average hand or if the actual median equals to average hand
    if (first_last_hand_average == average_hand) or (median == average_hand):
        return True
    return False


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
    if hand[-1] == 11:
        hand[-1] += 11
        return hand
    return hand