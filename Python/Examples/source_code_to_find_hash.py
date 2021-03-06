# Python program to find the SHA-1 message digest of a file

# importing the hashlib module
import hashlib

def hash_file(filename):
    """ This function returns the SHA-1 hash of the file passed into it """
    # Make a hash object
    h = hashlib.sha1()

    # Open file for reading in binary mode
    with open(filename, 'rb') as file:

        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # Read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # Return the hex representation of digest
    return h.hexdigest()

message = hash_file("track1.mp3")
print(message)
