class Solution:
    def __init__(self):
        self.color_red = 1
        self.color_blue = 2

    def find_color(self, graph, vertex, color_by_vertex, count, visited):
        adjacency_vertices = graph[vertex]
        # First check if any of the adjacency has color
        if len(adjacency_vertices) == 0:
            return self.color_blue, count
        for adjacency_vertex in adjacency_vertices:
            visited[adjacency_vertex] = True
            if adjacency_vertex in color_by_vertex:
                adjacency_color = color_by_vertex[adjacency_vertex]
                if adjacency_color == self.color_blue:
                    return self.color_red, count
                else:
                    return self.color_blue, count
            else:
                if adjacency_vertex in visited:
                    continue
                # find the number of hops where we can find the colored adjacency matrix
                color, count = self.find_color(graph, adjacency_vertex, color_by_vertex, count + 1, visited)
                if count % 2 == 0:
                    # At every 2 hop, the color will be same
                    return color
                else:
                    if color == self.color_red:
                        return self.color_blue
                    return self.color_red


    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        # Color the nodes, start from 0th node, color red,
        # and then color the all the adjacent nodes to be blue, if there are no two
        # adjacent node colors to be same, then the graph is bipartie
        color_by_vertex = {}
        # Start with BLUE

        for vertex in range(len(graph)):
            if len(graph[vertex]) == 0:
                # disjoint vertex does not make decision, so ignore them
                continue
            if len(color_by_vertex) == 0:
                # Start with BLUE
                color_by_vertex[vertex] = self.color_blue
            if vertex in color_by_vertex:
                # Already colored
                color = color_by_vertex[vertex]
            else:
                visited = {}
                color = self.find_color(graph, vertex, color_by_vertex, 0, visited)
                color_by_vertex[vertex] = color
            adjacent_color = self.color_blue
            if color == self.color_blue:
                adjacent_color = self.color_red
            # Now check if any of the adjacent is already colored and same color is there
            # if yes, then not a bipartie
            for adjacent_vertex in graph[vertex]:
                if adjacent_vertex in color_by_vertex:
                    if color_by_vertex[adjacent_vertex] == color:
                        return False
                else:
                    color_by_vertex[adjacent_vertex] = adjacent_color
        return True