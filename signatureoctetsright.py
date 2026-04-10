def custom_to_big_endian(custom_endian_bytes):
    # Check if the length is multiple of 4
    if len(custom_endian_bytes) % 4 != 0:
        raise ValueError("Length of bytes should be multiple of 4")

    # Swap bytes in each 4-byte word to convert from custom-endian to big-endian
    big_endian_bytes = bytearray(len(custom_endian_bytes))
    for i in range(0, len(custom_endian_bytes), 4):
        big_endian_bytes[i] = custom_endian_bytes[i]
        big_endian_bytes[i+1] = custom_endian_bytes[i+2]
        big_endian_bytes[i+2] = custom_endian_bytes[i+3]
        big_endian_bytes[i+3] = custom_endian_bytes[i+1]

    return big_endian_bytes

def convert_png_byte_order(input_file, output_file):
    # Read the contents of the input file
    with open(input_file, 'rb') as f:
        png_data = bytearray(f.read())

    # Pad the data to ensure its length is a multiple of 4
    while len(png_data) % 4 != 0:
        png_data.append(0)  # Add zero padding if necessary

    # Convert the byte order from custom-endian to big-endian
    big_endian_data = custom_to_big_endian(png_data)

    # Write the modified data to the output file
    with open(output_file, 'wb') as f:
        f.write(big_endian_data)

# Usage example

input_filename = 'custom.png'
output_filename = 'output.png'
convert_png_byte_order(input_filename, output_filename)
