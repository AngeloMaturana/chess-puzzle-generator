import pygame
import chess

class EventHandler:
    def __init__(self, game):
        self.game = game
    
    def handle_quit(self):
        pygame.quit()
        exit()
    
    def handle_mouse_button_down(self):
        pos = pygame.mouse.get_pos()
        square = self.game.get_square_from_mouse(pos)

        if self.game.selected_square is None:
            self.select_piece(square)
        else:
            piece = self.game.board.get_piece_at(self.game.selected_square)
            if piece and piece.piece_type == chess.PAWN and (square // 8 == 0 or square // 8 == 7):
                promotion = self.game.board.promote_pawn()
                self.game.board.push_move(self.game.selected_square, square, promotion)
            else:
                self.move_piece(square)

    def select_piece(self, square):
        piece = self.game.board.get_piece_at(square)
        if piece:
            self.game.selected_square = square
            self.game.legal_moves = self.game.board.get_legal_moves(square)

    def move_piece(self, square):
        if self.game.board.push_move(self.game.selected_square, square):
            if self.game.board.is_game_over():
                print("End Game!")
            self.game.selected_square = None
            self.game.legal_moves = []
        else:
            print("Illegal Movel!")
            self.game.selected_square = None
            self.game.legal_moves = []

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.handle_quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_button_down()
