from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()
#Cipher_suit is use to  encrypt and decrypt messages
cipher_suite = Fernet(key)


def encrypted_message(message):
  encrypt_message = cipher_suite.encrypt(message.encode())
  return encrypt_message


def decrypted_message(encrypt_message):
  decrypted_message = cipher_suite.decrypt(encrypt_message).decode()
  return decrypted_message
