from ... game import Game


class AlphaBeta():
    def play(self, game: Game):
        start = game.get_start_node()

        alpha = float('-Inf')
        beta = float('Inf')

        # 'game.get_max_player()' asks the game how it identifies the MAX player internally.
        # this is just for the sake of generality, so games are free to encode
        # player's identities however they want.
        # (it just so happens to be '1' for MAX, and '-1' for MIN most of the times)
        value, terminal_node = self.alphabeta(game, start, alpha, beta, game.get_max_player())
        return terminal_node

    def alphabeta(self, game, node, alpha, beta, max_player):
        # here we check if the current node 'node' is a terminal node
        terminal, winner = game.outcome(node)

        # if it is a terminal node, determine who won, and return
        # a) the value (-1, 0, 1)
        # b) the terminal node itself, to determine the path of moves/plies
        #    that led to this terminal node
        if terminal:
            if winner is None:
                return 0, node
            elif winner == max_player:
                return 1, node
            else:
                return -1, node

        # TODO, Exercise 3: implement the minimax-with-alpha-beta-pruning algorithm
        if node.player == max_player:

            best_value = float('-Inf')
            best_node = None

            for i in game.successors(node):
                cur_val, cur_node = self.alphabeta(game, i, alpha, beta, max_player)

                if cur_val > best_value:
                    best_node = cur_node

                best_value = max(best_value, cur_val)
                alpha = max(alpha, best_value)

                if best_value >= beta:
                    break

            return best_value, best_node
        else:
            best_value = float('Inf')
            best_node = None

            for i in game.successors(node):
                cur_val, cur_node = self.alphabeta(game, i, alpha, beta, max_player)

                if cur_val < best_value:
                    best_node = cur_node

                best_value = min(best_value, cur_val)
                beta = min(beta, best_value)

                if best_value <= alpha:
                    break

            return best_value, best_node
