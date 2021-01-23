# Name: Elena Rangelov
# Date: 1.7.2021

import random


class RandomBot:
    def __init__(self):
        self.white = "O"
        self.black = "@"
        self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        self.opposite_color = {self.black: self.white, self.white: self.black}
        self.x_max = None
        self.y_max = None

    def best_strategy(self, board, color):
        # returns best move
        self.x_max = len(board)
        self.y_max = len(board[0])
        if color == "#000000":
            color = "@"
        else:
            color = "O"

        moves1 = self.find_moves(board, color)

        moves = []
        for m in moves1:
            x = m // 8
            y = m % 8
            moves += [[x, y]]

        x = random.randint(0, len(moves) - 1)
        best_move = moves[x]
        return best_move, 0

    def stones_left(self, board):
        count = 0
        for x in board:
            for y in board[x]:
                if board[x, y] == ".":
                    count += 1
        return count

    def find_moves(self, board, color):
        moves_found = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                flipped_stones = self.find_flipped(board, i, j, color)
                if len(flipped_stones) > 0:
                    moves_found.update({i * self.y_max + j: flipped_stones})
        return moves_found

    def find_flipped(self, board, x, y, color):
        if board[x][y] != ".":
            return []
        if color == self.black:
            my_color = "@"
        else:
            my_color = "O"
        flipped_stones = []
        for incr in self.directions:
            temp_flip = []
            x_pos = x + incr[0]
            y_pos = y + incr[1]
            while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
                if board[x_pos][y_pos] == ".":
                    break
                if board[x_pos][y_pos] == my_color:
                    flipped_stones += temp_flip
                    break
                temp_flip.append([x_pos, y_pos])
                x_pos += incr[0]
                y_pos += incr[1]
        return flipped_stones


class Best_AI_bot:

    def __init__(self):
        self.white = "o"
        self.black = "@"
        self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        self.opposite_color = {self.black: self.white, self.white: self.black}
        self.x_max = None
        self.y_max = None

    def best_strategy(self, board, color):
        # returns best move
        return self.alphabeta(board, color, 3, float("inf"), float("-inf"))

    def minimax(self, board, color, search_depth):
        # returns best "value"
        return 1

    def negamax(self, board, color, search_depth):
        # returns best "value"
        return 1

    def alphabeta(self, board, color, search_depth, alpha, beta):
        # returns best "value" while also pruning
        # v = self.max_value(board, color, alpha, beta)
        # for f in self.find_moves(board, color):
        #     n_board = self.make_move(f, board))
        #
        # return self.find_moves(board, color)[v]
        #
        self.x_max = len(board)
        self.y_max = len(board[0])

        if color == "#ffffff":
            m_color = self.white
        else:
            m_color = self.black
        moves = self.find_moves(board, m_color)
        print("heya", color, moves)
        value = -9999
        move = -1
        v = self.max_value(board, m_color, search_depth, alpha, beta)
        for m in moves:
            n_board = self.make_move(board, color, m)
            n_value = self.min_value(n_board, self.opposite_color[m_color], 2, alpha, beta)
            if n_value > value:
                value = n_value
                move = m
        return (move // self.y_max, move % self.y_max), value


    def max_value(self, board, color, search_depth, alpha, beta):
        # if self.stones_left(board) == 0:
        #     moves = self.find_moves(board, color)
        #     return self.evaluate(board, color, moves)
        # v = float("-inf")
        # for m in self.find_moves(board, color):
        #     v = max(v, self.min_value(self.make_move(m, board), alpha, beta))
        #     if v > beta:
        #         return v
        #     alpha = max(alpha, v)
        # return v

        moves = self.find_moves(board, color)
        if len(moves) == 0: return -1000
        if len(self.find_moves(board, self.opposite_color[color])) == 0: return 1000
        if search_depth == 1:
            return self.evaluate(board, color, moves)
        v = float("-inf")
        for m in moves:
            n_board = self.make_move(board, color, m)
            next = self.min_value(n_board, self.opposite_color[color], search_depth - 1, alpha, beta)
            if max(v, next) != v:
                v = next
            if v > beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(self, board, color, search_depth, alpha, beta):
        # if self.stones_left(board) == 0:
        #     return self.evaluate(board)
        # v = float("inf")
        # for m in self.find_moves(board, color):
        #     v = min(v, self.max_value(self.make_move(m, board), alpha, beta))
        #     if v < alpha:
        #         return v
        #     beta = min(beta, v)
        # return v
        moves = self.find_moves(board, color)
        if len(moves) == 0: return 1000
        if len(self.find_moves(board, self.opposite_color[color])) == 0: return -1000
        if search_depth == 1:
            return -self.evaluate(board, color, moves)
        v = float("inf")
        for m in moves:
            n_board = self.make_move(board, color, m)
            next = self.max_value(n_board, self.opposite_color[color], search_depth - 1, alpha, beta)
            if min(v, next) != v:
                v = next
            if v < alpha:
                return v
            beta = min(beta, v)
        return v

    def make_key(self, board, color):
        # hashes the board
        return 1


    def stones_left(self, board):
        count = 0
        for x in range(len(board)):
            if board[x] == ".":
                count += 1
        return count


    def make_move(self, board, color, move):
        n_board = [row[:] for row in board]
        if color == self.white:
            char = "O"
        else:
            char = "@"

        x = move // 8
        y = move % 8
        n_board[x][y] = char
        flip = self.find_flipped(board, x, y, color)
        for f in flip:
            x = f[0]
            y = f[1]
            n_board[x][y] = char

        return n_board


    def evaluate(self, board, color, possible_moves):
        # returns the utility value
        # if color == "#ffffff":
        #     m_color = self.white
        # else: m_color = self.black
        # return len(possible_moves) - len(self.find_moves(board, self.opposite_color[m_color]))
        mx = 0
        for m in possible_moves:
            mx = max(len(possible_moves[m]), mx)
        return mx


    def score(self, board, color):
        # returns the score of the board
        return 1


    def find_moves(self, board, color):
        moves_found = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                flipped_stones = self.find_flipped(board, i, j, color)
                if len(flipped_stones) > 0:
                    moves_found.update({i * self.y_max + j: flipped_stones})
        return moves_found


    def find_flipped(self, board, x, y, color):
        if board[x][y] != ".":
            return []
        if color == self.black:
            my_color = "@"
        else:
            my_color = "O"
        flipped_stones = []
        for incr in self.directions:
            temp_flip = []
            x_pos = x + incr[0]
            y_pos = y + incr[1]
            while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
                if board[x_pos][y_pos] == ".":
                    break
                if board[x_pos][y_pos] == my_color:
                    flipped_stones += temp_flip
                    break
                temp_flip.append([x_pos, y_pos])
                x_pos += incr[0]
                y_pos += incr[1]
        return flipped_stones
