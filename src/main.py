import chess
import pygame
from board import Board
from event_handler import EventHandler
from pieces import Pieces

SCREEN_SIZE = 600
SQUARE_SIZE = SCREEN_SIZE // 8
WHITE = (240, 217, 181)
BLACK = (181, 136, 99)

class ChessGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption("Chess Puzzle Generator")

        self.board = Board()
        self.pieces = Pieces(SQUARE_SIZE)
        self.selected_square = None
        self.legal_moves = []

        self.event_handler = EventHandler(self)
    
    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(self.screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        
    
    def get_square_from_mouse(self, pos):
        col, row = pos[0] // SQUARE_SIZE, pos[1] // SQUARE_SIZE
        return chess.square(col, 7 - row)
    
    def highlight_moves(self, screen, moves):
        for move in moves:
            to_square = move.to_square
            row, col = divmod(to_square, 8)

            if self.board.get_piece_at(to_square):
                color = (255, 0, 0)
            else:
                color = (0, 255, 0)
            
            pygame.draw.circle(
                screen,
                color,
                (col * SQUARE_SIZE + SQUARE_SIZE // 2, (7 - row) * SQUARE_SIZE + SQUARE_SIZE // 2),
                SQUARE_SIZE // 5
            )
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                self.event_handler.handle_event(event)
            
            self.draw_board()

            if self.selected_square:
                self.highlight_moves(self.screen, self.legal_moves)

            self.pieces.draw_pieces(self.screen, self.board)
            pygame.display.flip()
        
        pygame.quit()

if __name__ == "__main__":
    game = ChessGame()
    game.run()
