from .. problem import Problem
from .. datastructures.priority_queue import PriorityQueue


def get_solver_mapping():
    return dict(ucs=UCS)


class UCS(object):
    # TODO, excercise 2:
    # - implement Uniform Cost Search (UCS), a variant of Dijkstra's Graph Search
    # - use the provided PriorityQueue where appropriate
    # - to put items into the PriorityQueue, use 'pq.put(<priority>, <item>)'
    # - to get items out of the PriorityQueue, use 'pq.get()'
    # - store visited nodes in a 'set()'
    def solve(self, problem: Problem):

        current_node = problem.get_start_node()

        visited_nodes = set()
        queue = PriorityQueue()

        queue.put(current_node.cost, current_node)

        while not problem.is_end(current_node): # Running the loop until current node is not the same as end node.

            if not queue.has_elements(): # Check if queue has any more elements, if not break out of loop
                break

            current_node = queue.get() # Assign new node to the current_node variable

            for n in problem.successors(current_node): # Loop through successor nodes, because we get them in a list
                if n not in visited_nodes: # Check if node is already visisted, if its not we add them to the queue.
                    visited_nodes.add(n)
                    queue.put(n.cost, n)

        return current_node

        # Pretty much same solution as seen in my bfs.py with addition to setting cost of node when adding to queue

