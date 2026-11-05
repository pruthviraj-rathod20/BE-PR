import heapq
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def generate_codes(root, code="", codes=None):
    if codes is None:
        codes = {}

    if root is None:
        return codes

    if root.char is not None:
        codes[root.char] = code
        return codes

    generate_codes(root.left, code + "0", codes)
    generate_codes(root.right, code + "1", codes)

    return codes


def huffman_encoding(text):
    frequency = Counter(text)
    heap = []

    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right

        heapq.heappush(heap, new_node)

    root = heap[0]
    codes = generate_codes(root)

    encoded_text = ""

    for char in text:
        encoded_text += codes[char]

    return frequency, codes, encoded_text


text = input("Enter text: ")

frequency, codes, encoded_text = huffman_encoding(text)

print("\nCharacter Frequencies:")
for char, freq in frequency.items():
    print(char, ":", freq)

print("\nHuffman Codes:")
for char, code in codes.items():
    print(char, ":", code)

print("\nOriginal Text:")
print(text)

print("\nEncoded Text:")
print(encoded_text)