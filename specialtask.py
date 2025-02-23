import random
import string
import numpy as np

class CustomEncryptor:
    def __init__(self):
        self.substitution_map, self.reverse_map = self.generate_substitution_cipher()
        self.matrix_key = self.generate_matrix_key()
    
    def generate_substitution_cipher(self):
        letters = string.ascii_letters + string.digits + string.punctuation + ' '
        shuffled = list(letters)
        random.shuffle(shuffled)
        return dict(zip(letters, shuffled)), dict(zip(shuffled, letters))
    
    def generate_matrix_key(self, size=3):
        key = np.random.randint(1, 10, (size, size))
        while np.linalg.det(key) == 0:  # Ensure the matrix is invertible
            key = np.random.randint(1, 10, (size, size))
        return key
    
    def substitution_encrypt(self, message):
        return ''.join(self.substitution_map.get(char, char) for char in message)
    
    def substitution_decrypt(self, encrypted_message):
        return ''.join(self.reverse_map.get(char, char) for char in encrypted_message)
    
    def matrix_encrypt(self, text):
        text_numbers = [ord(c) for c in text]
        size = self.matrix_key.shape[0]
        
        while len(text_numbers) % size != 0:
            text_numbers.append(0)  # Padding with zeros
        
        matrix = np.array(text_numbers).reshape(-1, size)
        encrypted_matrix = matrix @ self.matrix_key
        return encrypted_matrix.flatten().tolist()
    
    def matrix_decrypt(self, encrypted_list):
        size = self.matrix_key.shape[0]
        matrix = np.array(encrypted_list).reshape(-1, size)
        inverse_key = np.linalg.inv(self.matrix_key)
        decrypted_matrix = np.round(matrix @ inverse_key).astype(int)
        return ''.join(chr(c) for c in decrypted_matrix.flatten() if c != 0)
    
    def encrypt(self, message):
        sub_encrypted = self.substitution_encrypt(message)
        return self.matrix_encrypt(sub_encrypted)
    
    def decrypt(self, encrypted_list):
        matrix_decrypted = self.matrix_decrypt(encrypted_list)
        return self.substitution_decrypt(matrix_decrypted)

if __name__ == "__main__":
    encryptor = CustomEncryptor()
    
    message = "Hello, World!123"
    print("Original Message:", message)
    
    encrypted_data = encryptor.encrypt(message)
    print("Encrypted Data:", encrypted_data)
    
    decrypted_message = encryptor.decrypt(encrypted_data)
    print("Decrypted Message:", decrypted_message)