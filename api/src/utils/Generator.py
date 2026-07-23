import secrets
import string


class Generator:
    def generate_random_digital_string(self, size):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(secrets.choice(characters) for _ in range(size))
        return random_string

    def generate_random_alphabetical_string(self, size):
        characters = string.ascii_letters
        random_string = ''.join(secrets.choice(characters) for _ in range(size))
        return random_string