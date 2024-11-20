import chess


class Board:
    def __init__(self):
        self.board = chess.Board()

    def reset(self):
        self.board.reset()
    
    def get_legal_moves(self, from_square):
        return [move for move in self.board.legal_moves if move.from_square == from_square]
    
    def push_move(self, from_square, to_square, promotion=None):
        move = chess.Move(from_square, to_square, promotion)
        if move in self.board.legal_moves:
            self.board.push(move)
            return True
        return False
    
    def promote_pawn(self):
        promoted_piece = self.prompt_promotion()
        return promoted_piece

    def prompt_promotion(self):
        promotion_choice = input("Which one (1-Queen, 2-Rook, 3-Bishop, 4-Knight)")

        match promotion_choice:
            case '1':
                return chess.QUEEN
            case '2':
                return chess.ROOK
            case '3':
                return chess.BISHOP
            case '4':
                return chess.KNIGHT
            case _:
                return chess.QUEEN
    
    def get_piece_at(self, square):
        return self.board.piece_at(square)
    
    def is_game_over(self):
        return self.board.is_game_over()
        