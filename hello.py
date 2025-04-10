import numpy as np  # Import NumPy

N = 3  # Define matrix size

# Generate a random invertible key matrix
def generate_key_matrix(N):
    while True:
        key_matrix = np.random.randint(0, 256, (N, N))  # Generate random values
        if np.linalg.det(key_matrix) % 256 != 0:  # Ensure invertibility
            return key_matrix

# Generate a 3×3 key matrix
key_matrix = generate_key_matrix(N)

# Example block for encryption
block = np.random.randint(0, 256, (N, N))

# Encrypt block (Example encryption step)
enc_block = (np.dot(key_matrix, block) + np.random.randint(0, 256, (N, N))) % 256

print("Encrypted Block:\n", enc_block)
