"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """
    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        bool: Do the coordinates match?
    """
    cordinate = azara_record[1]
    azara_coordinate = (cordinate[:-1], cordinate[-1])
    rui_coordinate = rui_record[1]
    
    return azara_coordinate == rui_coordinate
    

def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, coordinate, quadrant) trio.

    Returns:
        tuple or str: The combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    Parameters:
        combined_record_group (tuple): Everything from both participants.

    Returns:
        str: Everything "cleaned", excess coordinates and information are removed.

    Note:
        The return statement is a multi-lined string with items separated by newlines.
        (see HINTS.md for an example).

    """

    # Tem q remover as coordenadas NumeroLetra (4B, 7E, 6A) e usar só as q sao em tuplas
    # A formatação tem q ser: 'Nome 1: Tupla[0[0]]' + 'Nome 2: Tupla[0[2]]' + 'Coordenada: Tupla[0[3]]' + 'Cor: Tupla[0[4]]' +     caractere de quebra de linha.

    return "".join([f"{(record[0], record[2], record[3], record[4])}\n" for record in combined_record_group])
    
