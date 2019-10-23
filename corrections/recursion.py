class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left  # Node
        self.right = right  # Node

    def __eq__(self, other):
        """On redéfinit la fonction d'égalité pour prendre en compte les arbres correctement."""
        return (
            self.value == other.value
            and self.left == other.left
            and self.right == other.right
        )

    def __str__(self):
        """Donne une représentation textuelle de votre arbre binaire."""
        if not self.left or not self.right:
            return str(self.value)
        else:
            return "( {} {} {} )".format(
                self.value,
                str(self.left),
                str(self.right)
            )


def invert(node):
    """Inverse un arbre binaire (renvoie un nouvel arbre binaire).
    
    Parameters
    ----------
    node : Node
        le noeud à inverser
    
    Returns
    -------
    Node
        le noeud inversé.
    """
    inverted = Node(node.value)
    if node.left and node.right:
        inverted.left = invert(node.right)
        inverted.right = invert(node.left)
    return inverted


def parse_node(s):
    """Lit un arbre binaire complet et renvoie un `Node`.

    Pour lire l'arbre binaire suivant :
    ( 1 ( 2 4 5 ) ( 3 6 7 ) )
    On voit assez clairement des tokens (séparés par des espaces) :
    ['(', '1', '(', '2', '4', '5', ')', '(', '3', '6', '7', ')', ')']
    L'idée de cet algorithme va être de lire progressivement les noeuds
    en consommant petit à petit les tokens de cette chaîne.

    Parameters
    ----------
    s : str
        la chaine de caractère à parser.
    
    Returns
    -------
    Node
        l'arbre binaire parsé depuis s.
    """
    tokens = s.split()
    # la liste de tokens. Elle sera lue et modifiée petit à petit.
    def parse_node_with_children():
        """Renvoie un Noeud ayant deux fils. Cette fonction implémente le cas 1.
        décrit dans la fonction `parse_aux`. On aura cependant déjà consommé un
        token, cette fonction sera donc appelée aux positions suivantes :
        ( 1 ( 2 4 5 ) ( 3 6 7 ) )
          ^   ^         ^
          a   b         c
        On remarque que si on compare les positions ici à celles données dans
        la documentation de `parse_aux`, les flèches menent vers soit le cas 1.
        soit le cas 2.

        À cet instant, nous savons que nous devons parser deux noeuds, nous
        appelons donc 2 fois la fonction `parse_aux` qui permet de parser un
        noeud ayant ou non des fils (une fois pour le fils gauche, et une fois
        pour le fils droit).

        À la fin de la lecture des fils, nous serons systématiquement à une
        ')', comme illustré :
        ( 1 ( 2 4 5 ) ( 3 6 7 ) )
                    ^         ^ ^
                    b         c a
        Nous savons donc que nous devons donc consommer un symbole ')'
        spécifiquement.

        Returns
        -------
        Node
            un noeud ayant deux fils
        """
        value = tokens.pop(0)
        node = Node(int(value))
        # dans cette question, on ne gère que les arbres complets,
        # un noeud a donc soit 0 soit 2 fils. On a écrit cette fonction
        # de façon à être sûr(e) qu'on était dans la cas d'un noeud qui
        # avait des fils (donc 2).
        # On peut donc appeler, pour chaque noeud fils (gauche et droit),
        # la fonction `parse_aux` qui va créer des nouveaux noeuds.
        node.left = parse_aux()
        node.right = parse_aux()
        # ou sinon, on peut faire plus court :
        # node = Node(int(value), parse_aux(), parse_aux())
        token = tokens.pop(0)
        assert token == ")"  # un noeud avec 2 fils aura toujours une ')' après
        return node

    def parse_aux():
        """La fonction auxilliaire pour renvoyer un Node.

        Cette fonction va être appelée lorsque nous sommes sur un nouveau
        noeud (on l'appelle au début de la lecture). Il faudra donc gérer
        le cas où nous sommes sur une parenthèse ouvrante (qui indique un
        noeud qui aura des fils)

        Vu que nous sommes dans un arbre binaire complet, nous avons deux cas
        possibles:
        1. nous sommes à un noeud ayant des noeuds fils (cas récursif)
        2. nous sommes à une feuille (cas d'arrêt, on renvoie juste un noeud)

        Le cas 1. va correspondre aux cas suivants :
        ( 1 ( 2 4 5 ) ( 3 6 7 ) )
        ^   ^         ^
        Tandis que le cas 2. va correspondre aux cas suivants :
        ( 1 ( 2 4 5 ) ( 3 6 7 ) )
                ^ ^       ^ ^

        Returns
        -------
        Node
            Le noeud qui correspond à la chaine de caractères.
        """
        token = tokens.pop(0)  # on consomme le 1er token
        if token == "(":  # le cas 1.
            return parse_node_with_children()
        else:  # le cas 2.
            return Node(int(token))

    return parse_aux()


assert invert(Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))) == Node(
    1, Node(3, Node(7), Node(6)), Node(2, Node(5), Node(4))
)
assert str(Node(1, Node(2), Node(3))) == "( 1 2 3 )"
assert (
    str(Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7))))
    == "( 1 ( 2 4 5 ) ( 3 6 7 ) )"
)
assert parse_node("( 1 2 3 )") == Node(1, Node(2), Node(3))
assert parse_node("( 1 ( 2 4 5 ) ( 3 6 7 ) )") == Node(
    1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7))
)
print("tout est ok")
