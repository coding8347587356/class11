import pgzrun

WIDTH = 870
HEIGHT = 650
TITLE = "Quiz Master"

marquee_box = Rect(0, 0, 860, 80)
question_box = Rect(0, 0, 650, 150)
timer_box = Rect(0, 0, 150, 150)
answer_box1 = Rect(0, 0, 300, 150)
answer_box2 = Rect(0, 0, 300, 150)
answer_box3 = Rect(0, 0, 300, 150)
answer_box4 = Rect(0, 0, 300, 150)
skip_box = Rect(0, 0, 150, 330)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

def draw():
    screen.fill(color = "blue")
    screen.draw.filled_rect(marquee_box, "green")
    screen.draw.filled_rect(question_box, "navy blue")
    screen.draw.filled_rect(timer_box, "dark green")
    screen.draw.filled_rect(skip_box, "red")
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "dark orange")
    marquee_message = "welcome to Quiz Master"

    screen.draw.textbox(marquee_message, marquee_box, color = "white")


pgzrun.go()