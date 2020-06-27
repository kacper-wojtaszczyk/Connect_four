# Display
display_w = 700
display_h = 700
caption = "Connect Four"

# Start screen
button1_w = 140
button1_h = 100
button1_x = display_w//2 - button1_w//2
button1_y = 500
button1_text = "START!"
button1_fontsize = 40
text1_w = 600
text1_h = 200
text1_x = display_w//2 - text1_w//2
text1_y = 100
text1_text = "Connect four game"
text1_fontsize = 80

# Restart
text2_w = 600
text2_h = 50
text2_x = display_w//2 - text1_w//2
text2_y = 0
text2_fontsize = 40
button2_w = 100
button2_h = 30
button2_x = display_w//2 - button2_w*2
button2_y = 50
button2_text = "YES"
button2_fontsize = 20
button3_w = 100
button3_h = 30
button3_x = display_w//2 + button3_w
button3_y = 50
button3_text = "NO"
button3_fontsize = 20
player_win_text = "You won! Do you want to restart?"
AI_win_text = "AI won! Do you want to restart?"

# Difficulty screen
text3_w = 600
text3_h = 50
text3_x = display_w//2 - text3_w//2
text3_y = 30
text3_fontsize = 40
text3_text = "Choose difficulty"
text4_w = 300
text4_h = 50
text4_x = display_w//2 + display_w//8 - text4_w//2
text4_y = display_h//5
text4_fontsize = 25
text4_text = "Randomly generated AI output"
text5_w = 300
text5_h = 50
text5_x = display_w//2 + display_w//8 - text5_w//2
text5_y = 2*display_h//5
text5_fontsize = 25
text5_text = "One-step heuristic algorithm"
text6_w = 300
text6_h = 50
text6_x = display_w//2 + display_w//8 - text6_w//2
text6_y = 3*display_h//5
text6_fontsize = 25
text6_text = "N-step minimax algorithm"
text7_w = 300
text7_h = 50
text7_x = display_w//2 + display_w//8 - text7_w//2
text7_y = 4*display_h//5
text7_fontsize = 25
text7_text = "Reinforcement learned neural network ( not done yet)"
button4_w = 100
button4_h = 30
button4_x = button4_w
button4_y = display_h//5 + 10
button4_text = "EASY"
button4_fontsize = 22
button5_w = 100
button5_h = 30
button5_x = button5_w
button5_y = 2*display_h//5 + 10
button5_text = "MEDIUM"
button5_fontsize = 22
button6_w = 100
button6_h = 30
button6_x = button6_w
button6_y = 3*display_h//5 + 10
button6_text = "HARD"
button6_fontsize = 22
button7_w = 100
button7_h = 30
button7_x = button6_w
button7_y = 4*display_h//5 + 10
button7_text = "GOD"
button7_fontsize = 22
easy = 1
medium = 2
hard = 3
god = 4

# Board
columns = 7
rows = 6
inarow = 4
board_block_size = 100
board_circle_radius = 40

# Marks
player_mark = 1
AI_mark = 2
player_turn = 1
AI_turn = 0

# Colors
bg_color = (77, 86, 94)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
button_color = (200, 100, 100)
button_effect_color = (255, 100, 100)
text1_color = (255, 0, 255)
board_color = (95, 164, 237)
player_color = (20, 200, 13)
AI_color = (186, 45, 10)

# Heuristic wages
twos = 0.1
twos_opp = -0.2
threes = 1
threes_opp = -1e2
fours = 1e6

# Minmax
minimax_steps = 3
