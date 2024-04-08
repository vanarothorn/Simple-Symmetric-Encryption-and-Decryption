from main import decrypted_message, encrypted_message

message = "This is a test message of the encrytion and decryption function"

#Test encryption function and return encrypted message string

encrypt_message = encrypted_message(message)
print("Encrypted Message: ", encrypt_message)
print()
#Test decrytion function and return decrypted message string

decrypt_message = decrypted_message(encrypt_message)
print("Decrypted Message: ", decrypt_message)
