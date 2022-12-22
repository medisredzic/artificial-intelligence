from .. problem import Problem
from .. datastructures.queue import Queue


# please ignore this
def get_solver_mapping():
    return dict(bfs=BFS)


class BFS(object):
    # TODO, exercise 1:
    # - implement Breadth First Search (BFS)
    # - use 'problem.get_start_node()' to get the node with the start state
    # - use 'problem.is_end(node)' to check whether 'node' is the node with the end state
    # - use a set() to store already visited nodes
    # - use the 'queue' datastructure that is already imported as the 'fringe'/ the 'frontier'
    # - use 'problem.successors(node)' to get a list of nodes containing successor states

    def solve(self, problem: Problem):
        current_node = problem.get_start_node()

        visited_nodes = set()
        next_nodes = Queue()

        next_nodes.put(current_node)

        while not problem.is_end(current_node):  # Running the loop until current node is not the same as end node.

            if not next_nodes.has_elements():  # Check if queue has any more elements, if not break out of loop
                break

            current_node = next_nodes.get()  # Assign new node to the current_node variable

            for n in problem.successors(current_node):  # Loop through successor nodes, because we get them in a list
                if n not in visited_nodes:  # Check if node is already visisted, if its not we add them to the queue.
                    visited_nodes.add(n)
                    next_nodes.put(n)

        return current_node
