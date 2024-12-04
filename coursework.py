def encode_message_in_bmp(image_path, message, output_path):
# Open the BMP file
    with open(image_path, 'rb') as bmp_file:
        bmp_data = bytearray(bmp_file.read())
    if not image_path.lower().endswith(".bmp"):
        raise ValueError("Error: file is not in bmp format please input the image path again")

# BMP header is typically 54 bytes
    pixel_data = bmp_data[54:]

#function of null characters to determine the end of a message
    message += '\0' 
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    data_index = 0
    for i in range(len(pixel_data)):
        if data_index < len(binary_message):

# Modify the least significant bit of the current byte
            pixel_data[i] = (pixel_data[i] & ~1) | int(binary_message[data_index])
            data_index += 1
        else:
            break

# Write the modified pixel data back to a new BMP file
    with open(output_path, 'wb') as bmp_file:
        bmp_file.write(bmp_data[:54])  # Write the header
        bmp_file.write(pixel_data)  # Write the modified pixel data
    print(f"Message hidden in {output_path}")
def read_message_from_bmp(image_path):

# Open the BMP file in binary mode
    with open(image_path, 'rb') as bmp_file:
        bmp_data = bytearray(bmp_file.read())

#skip bmp header which is usually 54 bits
    pixel_data = bmp_data[54:]

#get the hidden message using the least amount of bits possible 
    message_bits = []
    for byte in pixel_data:

#find the least amount of bits needed
        message_bits.append(byte & 0x01)

#bits to character conversion
    message = ''
    for i in range(0, len(message_bits), 8):
        byte = message_bits[i:i+8]
        if len(byte) < 8:
            break
        char = chr(int(''.join(str(bit) for bit in byte), 2))

#stop at null character
        if char == '\0':  
            break
        message += char

    return message

# Example usage
if __name__ == "__main__":
    image_path = input("Please enter the path of the image to hide the message in: ")
    hidden_message = input("Please enter your message to hide: ")

#path of the image after message is encoded
    output_image_path = "steganography.bmp"

#insert the message in the image
    encode_message_in_bmp(image_path, hidden_message, output_image_path)

#grab the message from the image
    retrieved_message = read_message_from_bmp(output_image_path)
    print("Retrieved hidden message:", retrieved_message)