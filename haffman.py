from collections import defaultdict
import heapq
import struct

class Node:
    def __init__(self, symbol=None, counter=None, left=None, right=None):
        self.symbol = symbol
        self.counter = counter
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.counter < other.counter

def build_tree(text):
    symbols = defaultdict(int)
    for byte in text:
        symbols[byte] += 1

    heap = []
    for byte, freq in symbols.items():
        node = Node(symbol=byte, counter=freq)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(counter=left.counter + right.counter, left=left, right=right)
        heapq.heappush(heap, parent)

    return heapq.heappop(heap)

def generate_codes(node, code="", code_dict=None):
    if code_dict is None:
        code_dict = {}

    if node is not None:
        if node.symbol is not None:
            code_dict[node.symbol] = code
        generate_codes(node.left, code + "0", code_dict)
        generate_codes(node.right, code + "1", code_dict)

    return code_dict

def serialize_tree(node):
    """Сериализация дерева Хаффмана в байты."""
    if node is None:
        return b""

    if node.symbol is not None:
        return b"\x01" + bytes([node.symbol])

    return b"\x00" + serialize_tree(node.left) + serialize_tree(node.right)

def deserialize_tree(data):
    """Десериализация дерева Хаффмана из байтов."""
    def helper():
        nonlocal index
        if index >= len(data):
            return None

        flag = data[index]
        index += 1

        if flag == 1:
            symbol = data[index]
            index += 1
            return Node(symbol=symbol)
        elif flag == 0:
            left = helper()
            right = helper()
            return Node(left=left, right=right)

    index = 0
    return helper()

def compress(text):
    if not text:
        return b""
    root = build_tree(text)

    codes = generate_codes(root)

    encoded_bits = "".join([codes[byte] for byte in text])

    padding = 8 - len(encoded_bits) % 8
    encoded_bits += "0" * padding  
    encoded_bytes = bytearray()
    for i in range(0, len(encoded_bits), 8):
        byte = encoded_bits[i:i+8]
        encoded_bytes.append(int(byte, 2))

    tree_bytes = serialize_tree(root)


    packed_data = (bytes([padding]) + struct.pack(">I", len(tree_bytes)) + tree_bytes + encoded_bytes )

    return packed_data

def decompress(packed_data):
    if not packed_data:
        return b""

    padding = packed_data[0]
    tree_length = struct.unpack(">I", packed_data[1:5])[0]

    tree_bytes = packed_data[5:5 + tree_length]
    root = deserialize_tree(tree_bytes)

    encoded_bytes = packed_data[5 + tree_length:]

    encoded_bits = "".join(f"{byte:08b}" for byte in encoded_bytes)
    encoded_bits = encoded_bits[:-padding]

    decoded_text = bytearray()
    current_node = root
    for bit in encoded_bits:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.symbol is not None:
            decoded_text.append(current_node.symbol)
            current_node = root

    return bytes(decoded_text)
