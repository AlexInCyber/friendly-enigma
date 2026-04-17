import base64
import pyshark
from collections import defaultdict

def extract_http_cookies(pcap_file):
    # Inițializează un dicționar pentru a stoca bucățile de cookie
    cookie_dict = defaultdict(str)
    # Deschide fișierul pcap și filtrează pachetele care conțin cookie-uri HTTP
    capture = pyshark.FileCapture(pcap_file, display_filter="http.cookie")
    
    for packet in capture:
        # Verifică dacă pachetul conține câmpul 'cookie'
        if 'cookie' in packet.http.field_names:
            cookies = packet.http.cookie
            cookie_parts = cookies.split(';')
            # Iterează prin fiecare parte a cookie-ului (ex: 'index=1', 'piece=...')
            for part in cookie_parts:
                if 'index' in part:
                    index = int(part.split('=')[1].strip())
                if 'piece' in part:
                    piece = part.split('=')[1].strip()
            # Stochează piesa folosind indexul ca cheie
            cookie_dict[index] = piece

    return cookie_dict

def reassemble_pieces(cookie_dict):
    # Sortează piesele pe baza cheilor (indexurilor) și le unește
    sorted_pieces = [cookie_dict[i] for i in sorted(cookie_dict.keys())]
    full_base64 = ''.join(sorted_pieces)
    return full_base64

def decode_base64(base64_data):
    # Decodifică datele Base64 și le afișează
    decoded_data = base64.b64decode(base64_data)
    print(f"Flag-ul recuperat: {decoded_data.decode('utf-8')}")

# Calea către fișierul de captură
pcap_file = 'task.pcap'
# Extrage cookie-urile
cookie_dict = extract_http_cookies(pcap_file)
# Reasamblează datele Base64
base64_data = reassemble_pieces(cookie_dict)
# Decodifică și afișează flag-ul
decode_base64(base64_data)
