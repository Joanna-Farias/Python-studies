"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
FACE_CARDS = {'J', 'Q', 'K'}
FACE_CARD_VALUE = 10
ACE_LOW_VALUE = 1
ACE_HIGH_VALUE = 11
BLACKJACK_TOTAL = 21

def value_of_card(card) -> int | tuple[str, str]:
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """
    if card in FACE_CARDS:
        return FACE_CARD_VALUE
    if card == 'A':
        return ACE_LOW_VALUE
    return int(card)


def higher_card(card_one, card_two) -> str:
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    if value_one == value_two:
        return (card_one, card_two)
    if value_one > value_two:
        return card_one
    return card_two


def value_of_ace(card_one, card_two) -> int:
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """
    
    if 'A' in (card_one, card_two):
        return ACE_LOW_VALUE
    total = value_of_card(card_one) + value_of_card(card_two)
    if total + ACE_HIGH_VALUE <= BLACKJACK_TOTAL:
        return ACE_HIGH_VALUE
    return ACE_LOW_VALUE


def is_blackjack(card_one, card_two) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """
    has_ace = 'A' in (card_one, card_two)
    has_ten = FACE_CARD_VALUE in (value_of_card(card_one), value_of_card(card_two))
    
    return has_ace and has_ten


def can_split_pairs(card_one, card_two) -> bool:
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two) -> bool:
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    
    total = value_of_card(card_one) + value_of_card(card_two)
    return 9 <= total <= 11