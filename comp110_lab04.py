"""
Module: comp110_lab04

Practice with writing functions, sounds, conditionals, and functional
composition.
"""
import sound


def get_max_in_range(my_sound, start, end):
    """
    Returns the maximum left channel value between the start and end indices.
    The end index is non-inclusive (just like the range function).

    Note that this maximum is the absolute value maximum, so -10 is consider
    larger than 6.

    Parameters:
    my_sound (type: Sound): A sound object we will inspect.
    start (type: int): The starting index for the range of samples.
    end (type: int): The ending index for the range of samples. This is non-inclusive.

    Returns:
    (type: int) The maximum left channel value in samples between the start
    and end indices.
    """

    # initialize max value to left channel value in the first sample in the range
    first = my_sound[start]
    max_val = abs(first.left)

    # loop through all other samples in the range and keep track of the
    # largest left channel sample value.
    for i in range(start+1, end):
        sample = my_sound[i]
        left_val = abs(sample.left)
        if (left_val > max_val):
             max_val = left_val

    return max_val


# To Do: Define your set_extremes function below this line.
def set_extremes(original_sound):
    """
    Applies a filter to the sound based on extreme left channel values.

    Parameters:
        original_sound (Sound): The original sound to be filtered.

    Returns:
        Sound: The filtered sound.
    """

    # Step 1: Create a copy of the parameter sound
    filtered_sound = original_sound.copy()

    # Step 2: Compute the maximum left channel value
    max_left_value = get_max_in_range(filtered_sound, 0, len(filtered_sound))

    # Step 3: Loop through all indices and apply filtering rules
    for i in range(len(filtered_sound)):
        sample = filtered_sound[i]

        # Set the right channel value to 0
        sample.right = 0

        # Apply left channel value conditions
        if abs(sample.left) > 3000:
            sample.left = max_left_value // 4
        elif abs(sample.left) < -3000:
            sample.left = -max_left_value // 4

    # Step 4: Return the modified sound
    return filtered_sound


jolly = sound.load_sound("jolly.wav")
jolly.play()
sound.wait_until_played()  # waits until jolly is done playing
jolly.display()


# To Do: Add new test code after this line.
# Call the set_extremes function and assign the result to extreme_laugh
extreme_laugh = set_extremes(jolly)

# Play the modified sound
extreme_laugh.play()
sound.wait_until_played()  # waits until extreme_laugh is done playing

# Display the waveform of the modified sound
extreme_laugh.display()
