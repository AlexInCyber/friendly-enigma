ports = [10069, 10067, 10083]  # paste your ports here
offset = 10000

flag = ''.join(chr(p - offset) for p in ports)
print(flag)
