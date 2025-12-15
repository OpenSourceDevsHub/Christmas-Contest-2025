ciphertext = "2E3GX3C3U93E4JK545I35M69L6Q6N78F91PAF9D0CED0GEAF91GQHZRJ6K95LON1TN4QB2S0TMVVR"

# 1. Удаление каждого 5-го символа
cleaned = ''.join(char for i, char in enumerate(ciphertext, 1) if i % 5 != 0)

# 2. Разбиваем на пары и преобразуем из Base36
numbers = [int(cleaned[i:i+2], 36) for i in range(0, len(cleaned), 2)]

# 3. Применяем offset = (i+1)²
result_chars = []
for i, num in enumerate(numbers, 1):
    offset = (i + 1) ** 2
    decoded_val = num - offset
    result_chars.append(chr(decoded_val))

result = ''.join(result_chars)

# 4. Применяем сдвиг на -3
final = ''
for c in result:
    o = ord(c)
    if 33 <= o <= 126:
        shifted = o - 3
        final += chr(shifted)

print(final)
    
	