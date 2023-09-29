class Node:
    def __init__(self, value):
        """Initialise un nouveau nœud."""
        self.value = value
        self.adjacent_nodes = []

    def add_adjacent(self, node):
        """Ajoute un nœud adjacent, garantissant qu'il n'est pas déjà connecté."""
        if node not in self.adjacent_nodes:
            self.adjacent_nodes.append(node)
            node.add_adjacent(self)  # Pour un graphe non orienté.

    def __repr__(self):
        """Représentation du nœud pour faciliter le débogage."""
        return f"Node({self.value})"


class Graph:
    def __init__(self):
        """Initialise un nouveau graphe."""
        self.nodes = []

    def add_node(self, value):
        """Ajoute un nœud au graphe."""
        # Vérifiez si le nœud existe déjà.
        for node in self.nodes:
            if node.value == value:
                return node
        
        new_node = Node(value)
        self.nodes.append(new_node)
        return new_node

    def add_edge(self, node1, node2):
        """Ajoute une arête entre les nœuds donnés."""
        node1.add_adjacent(node2)

    def dfs(self, start_node, visited=None):
        """Effectue un parcours en profondeur à partir du nœud de départ."""
        if visited is None:
            visited = set()

        visited.add(start_node)
        results = [start_node.value]  # Pour stocker les nœuds visités.

        for adjacent in start_node.adjacent_nodes:
            if adjacent not in visited:
                results.extend(self.dfs(adjacent, visited))

        return results