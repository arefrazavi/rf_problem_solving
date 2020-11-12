# https://www.hackerrank.com/challenges/tree-huffman-decoding/problem
import queue as Queue
from pprint import pprint

cntr = 0


class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1

    # Defines the behaviour of the less-than operator <.
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count


def huffman_hidden():  # builds the tree and returns root
    q = Queue.PriorityQueue()

    for key in freq:
        q.put((freq[key], key, Node(freq[key], key)))

    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))

    root = q.get()
    root = root[2]  # contains root object
    return root


def dfs_hidden(obj, already):
    if (obj == None):
        return
    elif (obj.data != '\0'):
        code_hidden[obj.data] = already

    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")


# Decode huffman code into a string.
def decodeHuff(root: Node, code):
    decodedString = ""
    while code:
        (decodedChar, code) = decodeNextChar(root, code)
        decodedString += decodedChar

    print(decodedString)


def decodeNextChar(root: Node, code):
    while code and root:
        if not root.left and not root.right:
            return root.data, code
        bit = code[0]
        # Move to the left child with removing the current bit (first bit) from code.
        if bit == "0":
            root = root.left
            code = code[1:]
        elif bit == "1":
            root = root.right
            code = code[1:]

    return root.data, code


ip = input()
freq = {}  # maps each character to its frequency

cntr = 0

for ch in ip:
    if (freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch] += 1
pprint(freq)

root = huffman_hidden()  # contains root of huffman tree

code_hidden = {}  # contains code for each object

dfs_hidden(root, "")

if len(code_hidden) == 1:  # if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
    toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)
