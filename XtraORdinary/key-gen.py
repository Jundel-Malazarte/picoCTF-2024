import secrets

def generate_secret_key(length):
    """
    Generate a secret key of specified length using random bytes.

    Args:
    - length: The length of the secret key to generate.

    Returns:
    - key: The generated secret key.
    """
    if length < 8:
        raise ValueError("Key length must be at least 12 characters")

    key = secrets.token_bytes(length)
    
    key_hex = key.hex()

    return key_hex

# Example usage:
key_length = 8
secret_key = generate_secret_key(key_length)
print("Generated Secret Key:", secret_key)
