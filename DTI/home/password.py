import random
import string

def generate_password(name):
    # Select a random special character
    special_character = random.choice(string.punctuation)
    
    # Generate a sequence of 3 to 5 random digits
    num_digits = random.randint(1, 4)
    random_digits = ''.join(str(random.randint(0, 9)) for _ in range(num_digits))
    
    # Combine the name, special character, and random digits to create the password
    password = name + special_character + random_digits
    
    return password

