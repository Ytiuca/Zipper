from node import Node
from tkinter import filedialog
import os

le_fichier_a_compresser: str = filedialog.askopenfilename(
    filetypes=[("All files", "*")]
)
le_dossier: str = os.path.split(le_fichier_a_compresser)[0]
le_fichier: str = os.path.split(le_fichier_a_compresser)[1]

# STEP 1 : compter les occurences de chaque caractère et les mettre dans un dico

data: str = None

with open(le_fichier_a_compresser, "r") as f:

    data = f.read()

occurence_dict: dict[str, int] = {}

for char in data:

    try:
        occurence_dict[char] += 1
    except KeyError:
        occurence_dict[char] = 1

# STEP 2 : on crée des noeuds à partir du dict et on trie du plus grand au plus petit

nodes: list[Node] = []

for key, value in occurence_dict.items():

    node: Node = Node(key, value, None, None)
    nodes.append(node)

while len(nodes) != 1:

    node1: Node = nodes.pop()
    node2: Node = nodes.pop()

    node3: Node = node1 + node2

    nodes.append(node3)
    nodes = sorted(nodes, reverse=True)

# STEP 3 : on parcourt l'arbre pour trouver le nouvel encodage de chaque char


def encodage_recursif(node: Node, encodage_dict: dict[str, str], encodage: str) -> None:

    if len(node.str) == 1:
        encodage_dict[node.str] = encodage
        return

    if node.filsG != None:
        encodage_recursif(node.filsG, encodage_dict, encodage + "0")

    if node.filsD != None:
        encodage_recursif(node.filsD, encodage_dict, encodage + "1")


encodage_dict: dict[str, str] = {}

encodage_recursif(nodes[0], encodage_dict, "")

# STEP 4 : convertir la string en byte et écrire le nouveau fichier

to_write: str = ""

for char in data:
    to_write += encodage_dict[char]

with open(le_dossier + "/" + le_fichier + ".zipper", "wb") as f:

    buffer: str = ""

    for bit in to_write:

        buffer += bit

        if len(buffer) >= 8:

            byte = int(buffer[:8], 2)

            f.write(byte.to_bytes(1, byteorder="big"))

            buffer = buffer[8:]

    if len(buffer) > 0:

        byte = int(buffer.ljust(8, "0"), 2)
        f.write(byte.to_bytes(1, byteorder="big"))
