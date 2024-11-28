def read_message_from_bmp(image_path):
    # Open the BMP file in binary mode
    with open(image_path, 'rb') as bmp_file:
        bmp_data = bytearray(bmp_file.read())

#bmp header (54 bits)
        pixel_data = bmp_data[54:]

#Extract the hidden message from the least significant bits
        message_bits = []
        for byte in bmp_data:
            message_bits.append(byte & 0x01)

#Convert the bits to characters
        message = ''
        for i in range(0, len(message_bits), 8):
            byte = message_bits[i:i+8]
            if len(byte) < 8:
                break
            char = chr(int(''.join(str(bit) for bit in byte), 2))
            if char == '\0':  # Stop at null character
                break
            message += char

        return message

#Example usage
image_path = input("please enter image path:")
hidden_message= input("please enter your message:")
print("Hidden message:", hidden_message)