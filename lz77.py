def compress(data, window_size=1024, byte_count=2):
    if not data:
        return b""  # Возвращаем пустую байтовую строку, если данные пустые

    compressed_data = bytearray()
    i = 0

    while i < len(data):
        match_length = 0
        match_offset = 0

        # Поиск совпадений в пределах окна
        for j in range(max(0, i - window_size), i):
            current_length = 0
            while (i + current_length < len(data) and
                   j + current_length < i and
                   data[j + current_length] == data[i + current_length]):
                current_length += 1
            if current_length > match_length:
                match_length = current_length
                match_offset = i - j

        # Если найдено совпадение, добавляем (offset, length)
        if match_length > 0:
            compressed_data.extend(match_offset.to_bytes(byte_count, 'big'))
            compressed_data.extend(match_length.to_bytes(byte_count, 'big'))
            i += match_length
        else:
            # Если совпадение не найдено, добавляем (0, 0, byte)
            compressed_data.extend((0).to_bytes(byte_count, 'big'))
            compressed_data.extend((0).to_bytes(byte_count, 'big'))
            compressed_data.append(data[i])
            i += 1

    return bytes(compressed_data)

def decompress(compressed_data, window_size=1024, byte_count=2):
    if not compressed_data:
        return b""  # Возвращаем пустую байтовую строку, если данные пустые

    decompressed_data = bytearray()
    i = 0

    while i < len(compressed_data):
        # Чтение offset и length
        offset = int.from_bytes(compressed_data[i:i + byte_count], 'big')
        i += byte_count
        length = int.from_bytes(compressed_data[i:i + byte_count], 'big')
        i += byte_count

        if offset == 0 and length == 0:
            # Если offset и length равны 0, это одиночный байт
            if i < len(compressed_data):
                decompressed_data.append(compressed_data[i])
                i += 1
            else:
                break  # Защита от выхода за пределы массива
        else:
            # Копирование данных из предыдущих позиций
            for j in range(length):
                if len(decompressed_data) >= offset:
                    decompressed_data.append(decompressed_data[-offset])
                else:
                    break  # Защита от выхода за пределы массива
    return bytes(decompressed_data)