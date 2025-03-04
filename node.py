class Node:

    def __init__(self, char : str, valeur : int, filsG : "Node", filsD : "Node") -> None:
        self.str = char
        self.valeur = valeur
        
        self.filsG = filsG
        self.filsD = filsD

    def __str__(self) -> str:
        return f"{self.str}{self.valeur}"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, other : "Node") -> bool:
        return (isinstance(other, Node)) and self.valeur == other.valeur
    
    def __gt__(self, other : "Node") -> bool:
        return self.valeur > other.valeur
    
    def __lt(self, other : "Node") -> bool:
        return self.valeur < other.valeur
    
    def __add__(self, other : "Node") -> "Node":
        return Node(self.str + other.str, self.valeur + other.valeur, self, other)