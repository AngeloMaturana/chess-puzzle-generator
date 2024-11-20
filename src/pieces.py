import chess
import pygame
import os

class Pieces:
    PIECES_SYMBOLS = {
        'p': "bp.png", 'n': "bN.png", 'b': "bB.png", 'r': "bR.png", 'q': "bQ.png", 'k': "bK.png",
        'P': "wp.png", 'N': "wN.png", 'B': "wB.png", 'R': "wR.png", 'Q': "wQ.png", 'K': "wK.png"
    }

    def __init__(self, square_size, image_path="images"):
        self.square_size = square_size
        self.images = self._load_images(image_path)

    
    def _load_images(self, path):
        images = {}
        for symbol, file_name in self.PIECES_SYMBOLS.items():
            file_path = os.path.join(path, file_name)
            images[symbol] = pygame.transform.scale(pygame.image.load(file_path), (self.square_size, self.square_size))
        return images
    
    def draw_pieces(self, screen, board):
        for square in chess.SQUARES:
            piece = board.get_piece_at(square)
            if piece:
                row, col = divmod(square, 8)
                image = self.images[piece.symbol()]
                screen.blit(image, (col * self.square_size, (7 - row) * self.square_size))