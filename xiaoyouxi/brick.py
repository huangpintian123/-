import turtle

# main window
wn = turtle.Screen()
wn.title("看谁牛逼")
wn.bgpic("brick_bg.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

turtle.register_shape("ball.gif")
turtle.register_shape("paddle.gif")

#set score
score_a = 0
score_b = 0



# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("paddle.gif")
paddle_a.penup()
paddle_a.goto(-350,0)


# paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("paddle.gif")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=4, stretch_len=0.6)
paddle_b.penup()
paddle_b.goto(350,0)

#ball, define 20 height and 20 widght
ball = turtle.Turtle()
ball.speed(0)
ball.shape("ball.gif")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 3 #ball move 4 pixels very time on y
ball.dy = 3 #ball move 4 pixels very time on y


#score
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Score:  0 : 0",align="center", font=("Arial", 30, "normal"))




#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")


#main loop
while True:
    wn.update()


    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #boeder check
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1 #reverse the direction when ball to the border

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1   #up and down border

    if ball.xcor() >390 :
        ball.goto(0, 0)
        ball.dx *= -1  #ball go to right side,A get score
        score_a +=1
        score.clear()
        score.write("Score:  {} : {}".format(score_a, score_b), align="center", font=("Arial", 30, "normal"))

    if ball.xcor() < -390 :
        ball.goto(0, 0)
        ball.dx *= -1   #ball go to left side, B get score
        score_b +=1
        score.clear()
        score.write("Score:  {} : {}".format(score_a, score_b), align="center", font=("Arial", 30, "normal"))

    #paddle and ball collision
    if (ball.xcor()  >  330 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor()-50):
        ball.setx(330)
        ball.dx  *= -1

    if (ball.xcor()  <  -330 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +50 and ball.ycor() > paddle_a.ycor()-50):
        ball.setx(-330)
        ball.dx  *= -1



