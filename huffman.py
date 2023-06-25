import heapq
from collections import defaultdict


class Node:
    def __init__(self, frequency, symbol=None, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_frequency_table(data):
    frequency_table = defaultdict(int)
    for char in data:
        frequency_table[char] += 1
    return frequency_table


def build_huffman_tree(frequency_table):
    heap = [Node(frequency, symbol) for symbol, frequency in frequency_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(node1.frequency + node2.frequency, left=node1, right=node2)
        heapq.heappush(heap, merged)

    return heapq.heappop(heap)


def build_codewords_mapping(root):
    codewords_mapping = {}
    build_codewords_mapping_helper(root, "", codewords_mapping)
    return codewords_mapping


def build_codewords_mapping_helper(node, current_code, codewords_mapping):
    if node.symbol:
        codewords_mapping[node.symbol] = current_code
    else:
        build_codewords_mapping_helper(node.left, current_code + "0", codewords_mapping)
        build_codewords_mapping_helper(node.right, current_code + "1", codewords_mapping)


def encode_text(data, codewords_mapping):
    encoded_text = ""
    for char in data:
        encoded_text += codewords_mapping[char]
    return encoded_text


def decode_text(encoded_text, root):
    decoded_text = ""
    current_node = root
    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.symbol:
            decoded_text += current_node.symbol
            current_node = root

    return decoded_text


# Demonstration of Huffman coding
if __name__ == "__main__":
    data = input("Enter the data to be encoded: ")

    frequency_table = build_frequency_table(data)
    huffman_tree_root = build_huffman_tree(frequency_table)
    codewords_mapping = build_codewords_mapping(huffman_tree_root)

    encoded_text = encode_text(data, codewords_mapping)
    decoded_text = decode_text(encoded_text, huffman_tree_root)

    print("Encoded text:", encoded_text)
    print("Decoded text:", decoded_text)
