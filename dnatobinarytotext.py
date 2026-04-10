dna_sequence = "CGATCTCACGCGCTGTCGACCGACATCAATGACGCAATCGATGCATCGATACCGCACGATCGATATATATCTATACATCTCGCGATGACGCCCGCGATCTCGACCGATATCCATGAATCGATCAATCGATCGCGCCATCCATACCGAGCGCGATGCCGACATCCCGAGATAAATACCGCAATCTCGCGATGCCGATATCAATACATACATCACGATCGAGCGAGCGCGCGACCGATATACATGCCGCGATACATAGATGCCGACCGACATACCTTC"

# Mapping of nucleotides to binary
nucleotide_to_binary = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}

# Function to convert a binary string to ASCII text
def binary_to_text(binary_str):
    text = ""
    for i in range(0, len(binary_str), 8): # ASCII characters are 8 bits
        byte = binary_str[i:i+8]
        text += chr(int(byte, 2))
    return text

# Convert the DNA sequence to a binary string
binary_sequence = ''.join([nucleotide_to_binary[n] for n in dna_sequence])

# Try to find the flag by decoding binary to text
flag_start = "ctf{"

for i in range(0, len(binary_sequence), 2): # Adjust step size as needed
    for j in range(i+8, len(binary_sequence)+1, 8): # Increment in 8 bit
        decoded_text = binary_to_text(binary_sequence[i:j])
        if decoded_text.startswith(flag_start):
            print(f"Possible flag found: {decoded_text}")
