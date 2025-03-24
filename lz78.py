def compress(data):
    dictionary = {b'': 0}  # Инициализация словаря с пустой строкой
    current_string = b''
    compressed_data = bytearray()
    dict_size = 1

    for byte in data:
        byte = bytes([byte])  # Преобразуем байт в байтовую строку
        combined_string = current_string + byte
        if combined_string in dictionary:
            current_string = combined_string
        else:
            # Добавляем индекс и байт в сжатые данные
            index = dictionary[current_string]
            compressed_data.extend(index.to_bytes(2, 'big'))  # Индекс (2 байта)
            compressed_data.extend(byte)  # Байт (1 байт)
            # Добавляем новую строку в словарь
            dictionary[combined_string] = dict_size
            dict_size += 1
            current_string = b''

    # Добавляем последнюю строку, если она есть
    if current_string:
        index = dictionary[current_string]
        compressed_data.extend(index.to_bytes(2, 'big'))  # Индекс (2 байта)
        compressed_data.extend(b'')  # Пустой байт для завершения

    return bytes(compressed_data)

def decompress(compressed_data):
    dictionary = {0: b''}  # Инициализация словаря
    dict_size = 1
    decompressed_data = bytearray()
    i = 0

    while i < len(compressed_data):
        # Чтение индекса (2 байта)
        index = int.from_bytes(compressed_data[i:i + 2], 'big')
        i += 2
        # Чтение байта (1 байт)
        if i < len(compressed_data):
            byte = compressed_data[i:i + 1]
            i += 1
        else:
            byte = b''

        if index not in dictionary:
            raise ValueError("Invalid compressed data: index not in dictionary")
        
        # Получаем строку из словаря
        entry = dictionary[index]
        # Добавляем новый символ к строке
        new_entry = entry + byte
        # Добавляем новую строку в словарь
        dictionary[dict_size] = new_entry
        dict_size += 1
        # Добавляем строку в распакованные данные
        decompressed_data.extend(new_entry)

    return bytes(decompressed_data)
