# CARON Samuel
# 2021-05-06
# Version 3.0 / Plusieurs versions car beaucoup de problèmes

from typing_extensions import Self

class Huffman:
    class HuffmanTree:
        def __init__(self : Self, char : str | None, freq : int, left : Self | None = None, right : Self | None = None):
            """
                constructeur de l'arbre binaire Huffman

                @Args:
                    char (str|None) : caractère
                    freq (int) : fréquence d'apparition du caractère
                    left (HuffmanTree) : branche de gauche
                    right (HuffmanTree) : branche de droite
             """
            self.char  = char
            self.freq  = freq
            self.left  = left
            self.right = right

        def isLeaf(self : Self) -> bool:
            """ 
            Vérifie si l'arbre est une feuille

            Args:
                self (Self): l'arbre

            Returns:
                bool: True si l'arbre est une feuille, False sinon
            """
            return self.left == None and self.right == None

        def __repr__(self : Self) -> str:
            """
            Permet d'afficher l'arbre

            Args:
                self (Self): l'arbre

            Returns:
                str: l'arbre sous forme de chaîne de caractères
            """
            left  : str = ""
            right : str = ""
            (left := 'None') if self.left == None else (left := str(self.left))
            (right := 'None') if self.right == None else (right := str(self.right))
            return '(char : \'' + self.char + '\', freq : ' + str(self.freq) + ', nodes : ' + '{ ' + left + ', ' + right + ' })'

    @staticmethod
    def buildFreqTable(text : str) -> dict[str, int]:
        """
        Créer la table de fréquence

        Args:
            text (str): le texte à coder

        Returns:
            dict[str, int]: la table de fréquence
        """
        freq = {}
        for chr in text:
            if chr not in freq:
                freq[chr] = 1
            else:
                freq[chr] += 1
        freq = dict(sorted(freq.items(), key = lambda item : item[1], reverse = True))
        return freq
    
    @staticmethod
    def insert_tree_list(tree: HuffmanTree, tree_list: list) -> list:
        """
        Permet d'ajouter un arbre dans la liste d'arbre

        Args:
            tree (HuffmanTree): l'arbre à ajouter
            tree_list (list): la liste d'arbre

        Returns:
            list: la liste d'arbre avec l'arbre ajouté
        """
        for i in range(len(tree_list)):
            if tree_list[i].freq >= tree.freq:
                tree_list.insert(i, tree)
                break
        if tree not in tree_list:
            tree_list.append(tree)
        return tree_list
    
    @staticmethod
    def build_tree_list(freq: dict) -> list:
        """
        Créer une liste d'arbre à partir d'une table de fréquence

        Args:
            freq (dict): la table de fréquence

        Returns:
            list: la liste d'arbre
        """
        tree_list = []
        for key in freq.keys():
            Huffman.insert_tree_list(Huffman.HuffmanTree(key, freq[key]), tree_list)
        return tree_list
    
    @staticmethod
    def build_huffman_tree(freq: dict) -> HuffmanTree:
        """
        Créer l'arbre binaire de Huffman

        Args:
            freq (dict): la table de fréquence

        Returns:
            HuffmanTree: l'arbre binaire de Huffman
        """
        tree_list = Huffman.build_tree_list(freq)
        while len(tree_list) != 1:
            first_branch = tree_list.pop(0)
            second_branch = tree_list.pop(0)
            tere_branch = Huffman.HuffmanTree(None, first_branch.freq + second_branch.freq, first_branch, second_branch)
            Huffman.insert_tree_list(tere_branch, tree_list)
        return tree_list[0]
    
    @staticmethod
    def getCodingTable(tree : HuffmanTree, path : str = '', res : dict[str, str] = {}) -> dict[str, str]:
        """Renvoie la table de codage à partir de l'arbre binaire de Huffman

        Args:
            tree (HuffmanTree): l'arbre binaire de Huffman
            path (str, optional): la chaine de caractère. Defaults to ''.
            res (dict[str, str], optional): le résultat. Defaults to {}.

        Returns:
            dict[str, str]: la table de codage
        """
        if tree.isLeaf():
            res[tree.char] = path
        else:
            Huffman.getCodingTable(tree.left, path + '1', res)
            Huffman.getCodingTable(tree.right, path + '0', res)
        return res
    
    @staticmethod
    def decodeHuffOne(coded_text: str, i: int, huff: HuffmanTree) -> tuple[int, str or None]:
        """ 
        Décoder un caractère à partir d'un texte codé et d'un arbre binaire de Huffman

        Args:
            coded_text (str): le texte codé
            i (int): l'index du caractère à décoder
            huff (HuffmanTree): l'arbre binaire de Huffman

        Returns:
            tuple[int, str or None]: l'index du caractère suivant et le caractère décoder
        """
        end = False
        tree = huff
        index = i

        while not end:
            if tree.isLeaf() or index >= len(coded_text):
                end = True
            else:
                tree = tree.left if coded_text[index] == '1' else tree.right
                index += 1

        coding_table = Huffman.getCodingTable(huff)
        for key in coding_table.keys():
            if coding_table[key] == coded_text[i:index]:
                return (index, str(key))
        return (index, None)
    
    @staticmethod
    def decodeHuff(coded_text: str, huff: HuffmanTree) -> str:
        """ 
        Décode un texte à partir d'un arbre binaire de Huffman

        Args:
            coded_text (str): le texte codé
            huff (HuffmanTree): l'arbre binaire de Huffman

        Returns:
            str: le texte décodé
        """
        decoded_text = ""
        index = 0
        while index < len(coded_text):
            character = Huffman.decodeHuffOne(coded_text, index, huff)
            index = character[0]
            decoded_text += character[1]
        return decoded_text

    @staticmethod
    def decodeHuffman(text: str, occurrences : dict[str, int]) -> str:
        """
        Décode un texte à partir d'une table de fréquence

        Args:
            text (str): le texte codé
            occurrences (dict[str, int]): la table de fréquence

        Returns:
            str: le texte décodé
        """
        return Huffman.decodeHuff(text, Huffman.build_huffman_tree(occurrences))
    
    @staticmethod
    def encodeHuffman(text : str) -> str:
        """
        Encode un texte à partir de l'arbre binaire de Huffman

        Args:
            text (str): le texte à encoder

        Returns:
            str: le texte encodé
        """
        occurrences  : dict[str, int] = Huffman.buildFreqTable(text)
        coding_table : dict[str, str] = Huffman.getCodingTable(Huffman.build_huffman_tree(occurrences))
        encoded_text : str            = ""
        for character in text:
            encoded_text += coding_table[character]
        return encoded_text
    
    
# MAIN    

if __name__ == '__main__':
    text = "je test huffman"
    occurrences = Huffman.buildFreqTable(text)                             
    encoded = Huffman.encodeHuffman(text)
    decoded = Huffman.decodeHuffman(encoded, occurrences)

    print(text)
    print(occurrences)
    print(encoded)
    print(decoded)