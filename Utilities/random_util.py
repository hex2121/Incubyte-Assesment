"""
Utility module for generating random data.
Includes functions to create random strings, which are useful for generating unique emails.
"""

import random
import string

def random_string(length=8):
    """
    Generate a random string of lowercase letters.

    :param length: Length of the generated string (default is 8)
    :return: A random string of the specified length
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
