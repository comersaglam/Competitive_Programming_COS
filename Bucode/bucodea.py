def process_string(s):
    new_s = s.replace('BUCODE', '')

    if not new_s:
        return "UTKU"
    else:
        return new_s


s = input()
print(process_string(s))

