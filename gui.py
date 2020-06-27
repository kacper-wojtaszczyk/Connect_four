import pygame
import config


class Button(object):
    def __init__(self, x, y, width, height, text_color, background_color, text, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.font = pygame.font.SysFont('Comic Sans MS', font_size)
        self.text = text
        self.text_color = text_color
        self.text = self.font.render(text, True, text_color)
        self.text_rect = self.text.get_rect()
        self.background_color = background_color

    def draw(self, display):
        self.button = pygame.draw.rect(
            display, self.background_color, (self.rect), 0)
        display.blit(self.text, (self.rect.centerx - self.text_rect.width //
                                 2, self.rect.centery - self.text_rect.height//2))
        pygame.draw.rect(display, self.text_color, self.rect, 3)


class TextWindow(object):
    def __init__(self, x, y, width, height, text_color, text, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont('Comic Sans MS', font_size)
        self.text = text
        self.text_color = text_color
        self.text = self.font.render(text, True, text_color)
        self.text_rect = self.text.get_rect()

    def draw(self, display, align="center"):
        if align == "center":
            display.blit(self.text, (self.rect.centerx - self.text_rect.width//2,
                                     self.rect.centery - self.text_rect.height//2))
        elif align == "left":
            display.blit(
                self.text, (self.rect.x, self.rect.centery - self.text_rect.height//2))
        elif align == "right":
            display.blit(self.text, (self.rect.x + self.rect.width -
                                     self.text_rect.width, self.rect.centery - self.text_rect.height//2))


# Game screens

def start_screen(mouse_pos, click, game_display):
    button1 = Button(config.button1_x, config.button1_y, config.button1_w, config.button1_h,
                     config.BLACK, config.button_color, config.button1_text, config.button1_fontsize)
    text_window = TextWindow(config.text1_x, config.text1_y, config.text1_w, config.text1_h,
                             config.board_color, config.text1_text, config.text1_fontsize)
    if mouse_pos[0] in range(button1.x, button1.x + button1.w):
        if mouse_pos[1] in range(button1.y, button1.y + button1.h):
            button1.background_color = config.button_effect_color
            if click:
                return True
    else:
        button1.background_color = config.button_color
    game_display.fill(config.bg_color)
    button1.draw(game_display)
    text_window.draw(game_display)
    pygame.display.update()


def restart_screen(mouse_pos, click, game_display, winner):
    if winner == config.AI_mark:
        text = config.AI_win_text
    if winner == config.player_mark:
        text = config.player_win_text
    text_window = TextWindow(config.text2_x, config.text2_y, config.text2_w,
                             config.text2_h, config.board_color, text, config.text2_fontsize)
    button2 = Button(config.button2_x, config.button2_y, config.button2_w, config.button2_h,
                     config.BLACK, config.button_color, config.button2_text, config.button2_fontsize)
    button3 = Button(config.button3_x, config.button3_y, config.button3_w, config.button3_h,
                     config.BLACK, config.button_color, config.button3_text, config.button3_fontsize)
    if mouse_pos[0] in range(button2.x, button2.x + button2.w):
        if mouse_pos[1] in range(button2.y, button2.y + button2.h):
            button2.background_color = config.button_effect_color
            if click:
                return True
    elif mouse_pos[0] in range(button3.x, button3.x + button3.w):
        if mouse_pos[1] in range(button3.y, button3.y + button3.h):
            button3.background_color = config.button_effect_color
            if click:
                return False
    else:
        button2.background_color = config.button_color
        button3.background_color = config.button_color
    text_window.draw(game_display)
    button2.draw(game_display)
    button3.draw(game_display)
    pygame.display.update()
    return None


def difficulty_screen(mouse_pos, click, game_display):
    text1 = TextWindow(config.text3_x, config.text3_y, config.text3_w,
                       config.text3_h, config.board_color, config.text3_text, config.text3_fontsize)
    text2 = TextWindow(config.text4_x, config.text4_y, config.text4_w,
                       config.text4_h, config.board_color, config.text4_text, config.text4_fontsize)
    text3 = TextWindow(config.text5_x, config.text5_y, config.text5_w,
                       config.text5_h, config.board_color, config.text5_text, config.text5_fontsize)
    text4 = TextWindow(config.text6_x, config.text6_y, config.text6_w,
                       config.text6_h, config.board_color, config.text6_text, config.text6_fontsize)
    text5 = TextWindow(config.text7_x, config.text7_y, config.text7_w,
                       config.text7_h, config.board_color, config.text7_text, config.text7_fontsize)
    button1 = Button(config.button4_x, config.button4_y, config.button4_w, config.button4_h,
                     config.BLACK, config.button_color, config.button4_text, config.button4_fontsize)
    button2 = Button(config.button5_x, config.button5_y, config.button5_w, config.button5_h,
                     config.BLACK, config.button_color, config.button5_text, config.button5_fontsize)
    button3 = Button(config.button6_x, config.button6_y, config.button6_w, config.button6_h,
                     config.BLACK, config.button_color, config.button6_text, config.button6_fontsize)
    button4 = Button(config.button7_x, config.button7_y, config.button7_w, config.button7_h,
                     config.BLACK, config.button_color, config.button7_text, config.button7_fontsize)
    if mouse_pos[1] in range(button1.y, button1.y + button1.h):
        if mouse_pos[0] in range(button1.x, button1.x + button1.w):
            button1.background_color = config.button_effect_color
            if click:
                difficulty = 1
                return difficulty
    elif mouse_pos[1] in range(button2.y, button2.y + button2.h):
        if mouse_pos[0] in range(button2.x, button2.x + button2.w):
            button2.background_color = config.button_effect_color
            if click:
                difficulty = 2
                return difficulty
    elif mouse_pos[1] in range(button3.y, button3.y + button3.h):
        if mouse_pos[0] in range(button3.x, button3.x + button3.w):
            button3.background_color = config.button_effect_color
            if click:
                difficulty = 3
                return difficulty
    # elif mouse_pos[1] in range(button4.y, button4.y + button4.h):
    #     if mouse_pos[0] in range(button4.x, button4.x + button4.w):
    #         button4.background_color = config.button_effect_color
    #         if click:
    #             difficulty = 3
    #             return difficulty
    else:
        button1.background_color = config.button_color
        button2.background_color = config.button_color
        button3.background_color = config.button_color
        button4.background_color = config.button_color
    game_display.fill(config.bg_color)
    button1.draw(game_display)
    button2.draw(game_display)
    button3.draw(game_display)
    button4.draw(game_display)
    text1.draw(game_display,)
    text2.draw(game_display, 'left')
    text3.draw(game_display, 'left')
    text4.draw(game_display, 'left')
    text5.draw(game_display, 'left')
    pygame.display.update()
