
import random
def generate_random_code():
    """
    Generate a random 8-digit code
    """
    return "".join(str(random.randint(0, 9)) for i in range(8))