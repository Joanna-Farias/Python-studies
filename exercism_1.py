
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The elapsed bake time in the moment.
        EXPECTED_BAKE_TIME (int const): Constant that defines the expected bake time (40min)
        Returns:
            int: The remaining bake time (in minutes)
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
        Calculate the preparation time in minutes.

        Parameters:
            number_of_layers (int): The total number of the lasagna layers.

        Returns:
            int: Total time for preparation (in minutes).
    """
    return number_of_layers * 2
        
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
