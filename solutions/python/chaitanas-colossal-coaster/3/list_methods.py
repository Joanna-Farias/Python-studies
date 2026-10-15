"""Functions to manage and organize queues at Chaitana's roller coaster."""

EXPRESS_TICKET = 1

def add_me_to_the_queue(express_queue: list[str], normal_queue: list[str], ticket_type: int, person_name: str) -> list[str]:
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    Parameters:
        express_queue: The names in the Fast-track queue.
        normal_queue: The names in the normal queue.
        ticket_type: Type of ticket. 1 = express, 0 = normal.
        person_name: The name of person to add to a queue.

    Returns:
        list: The (updated) queue the name was added to.
    """
    if ticket_type == EXPRESS_TICKET:
        express_queue.append(person_name)
        return express_queue
    normal_queue.append(person_name)
    return normal_queue


def find_my_friend(queue: list[str], friend_name: str) -> int | None:
    """Search the queue for a name and return their queue position (index).

    Parameters:
        queue: The names in the queue.
        friend_name: The name of friend to find.

    Returns:
        int: The index at which the friends name was found.
    """
    if friend_name in queue:
        return queue.index(friend_name)
    return None


def add_me_with_my_friends(queue: list[str], index: int, person_name: str) -> list[str]:
    """Insert the late arrival's name at a specific index of the queue.

    Parameters:
        queue: The names in the queue.
        index: The index at which to add the new name.
        person_name: The name to add.

    Returns:
        list: The queue updated with new name.
    """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list[str], person_name: str) -> list[str] | None:
    """Remove the mean person from the queue by the provided name.

    Parameters:
        queue: The names in the queue.
        person_name: The name of mean person.

    Returns:
        list: The queue updated with the mean persons name removed.
    """
    if person_name in queue:
        queue.remove(person_name)
        return queue
    return None


def how_many_namefellows(queue: list[str], person_name: str) -> int:
    """Count how many times the provided name appears in the queue.

    Parameters:
        queue: The names in the queue.
        person_name: The name you wish to count or track.

    Returns:
        int: The number of times the name appears in the queue.
    """
    return queue.count(person_name)


def remove_the_last_person(queue: list[str]) -> str:
    """Remove the person in the last index from the queue and return their name.

    Parameters:
        queue: The names in the queue.

    Returns:
        str: The name that has been removed from the end of the queue.
    """
    return queue.pop()


def sorted_names(queue: list[str]) -> list[str]:
    """Sort the names in the queue in alphabetical order and return the result.

    Parameters:
        queue: The names in the queue.

    Returns:
        list: A copy of the queue in alphabetical order.
    """
    return sorted(queue)