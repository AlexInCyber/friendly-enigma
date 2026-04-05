# Citește lista de porturi dintr-un fișier (generat de tshark)
# Regula: pentru fiecare două valori (a, b):
#   dacă b == 1337 => low nibble = 0xb
#   altfel low nibble = b
# caracterul = chr(a * 16 + low_nibble)
# Apoi concatenăm pentru a obține flag-ul.

def decode_from_file(filename):
    with open(filename, 'r') as f:
        # citim toate liniile și eliminăm linii goale
        lines = [ln.strip() for ln in f if ln.strip() != ""]
    # convertim la int; dacă o linie nu e numerică, va arunca ValueError
    arr = [int(x) for x in lines]

    # verificare minimă
    if len(arr) % 2 != 0:
        raise ValueError("Număr impar de elemente în listă; se așteaptă perechi.")

    flag_chars = []
    i = 0
    while i < len(arr):
        a = arr[i]
        b = arr[i+1]
        # caz special: semnalizator folosit în captura originală
        if b == 1337:
            low = 0xb
        else:
            low = b
        val = a * 16 + low
        # clamp pentru siguranță (0-255), dar în mod normal val ar trebui să fie valid ASCII
        if not 0 <= val <= 0xFF:
            raise ValueError(f"Valoare octet nevalidă: {val} la index {i}")
        flag_chars.append(chr(val))
        i += 2

    return "".join(flag_chars)

if __name__ == "__main__":
    flag = decode_from_file("ports.txt")
    print(flag)
