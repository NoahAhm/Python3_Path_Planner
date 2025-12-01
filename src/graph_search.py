import numpy as np
from collections import deque
from .graph import Cell
from .utils import trace_path

"""
General graph search instructions:

First, define the correct data type to keep track of your visited cells
and add the start cell to it. If you need to initialize any properties
of the start cell, do that too.

Next, implement the graph search function. When you find a path, use the
trace_path() function to return a path given the goal cell and the graph. You
must have kept track of the parent of each node correctly and have implemented
the graph.get_parent() function for this to work. If you do not find a path,
return an empty list.

To visualize which cells are visited in the navigation webapp, save each
visited cell in the list in the graph class as follows:
     graph.visited_cells.append(Cell(cell_i, cell_j))
where cell_i and cell_j are the cell indices of the visited cell you want to
visualize.
"""


def depth_first_search(graph, start, goal):
    """Depth First Search (DFS) algorithm. This algorithm is optional for P3.
    Args:
        graph: The graph class.
        start: Start cell as a Cell object.
        goal: Goal cell as a Cell object.
    """
    graph.init_graph()  # Make sure all the node values are reset.

    """TODO (P3): Implement DFS (optional)."""

    # If no path was found, return an empty list.
    return []


def breadth_first_search(graph, start, goal):
    """Breadth First Search (BFS) algorithm.
    Args:
        graph: The graph class.
        start: Start cell as a Cell object.
        goal: Goal cell as a Cell object.
    """
    graph.init_graph()  # Make sure all the node values are reset.

    # Reject immediately if start or goal are in collision.
    if graph.check_collision(start.i, start.j) or graph.check_collision(goal.i, goal.j):
        return []

    frontier = deque()
    frontier.append(start)
    graph.visited[start.j, start.i] = True
    graph.distance[start.j, start.i] = 0.0
    graph.visited_cells.append(Cell(start.i, start.j))

    while frontier:
        cell = frontier.popleft()
        if cell.i == goal.i and cell.j == goal.j:
            return trace_path(cell, graph)

        for ni, nj in graph.find_neighbors(cell.i, cell.j):
            if graph.visited[nj, ni] or graph.check_collision(ni, nj):
                continue
            graph.visited[nj, ni] = True
            graph.distance[nj, ni] = graph.distance[cell.j, cell.i] + 1
            graph.parent_i[nj, ni] = cell.i
            graph.parent_j[nj, ni] = cell.j
            next_cell = Cell(ni, nj)
            graph.visited_cells.append(next_cell)
            frontier.append(next_cell)

    # If no path was found, return an empty list.
    return []


def a_star_search(graph, start, goal):
    """A* Search (BFS) algorithm.
    Args:
        graph: The graph class.
        start: Start cell as a Cell object.
        goal: Goal cell as a Cell object.
    """
    graph.init_graph()  # Make sure all the node values are reset.

    """TODO (P3): Implement A*."""

    # If no path was found, return an empty list.
    return []
