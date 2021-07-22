import turtle
import winsound


#game screen

wn = turtle.Screen()
wn.title('Pong game by sajjad')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)



#game paddle_left

paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('white')
paddle_left.shapesize(stretch_len=1,stretch_wid=5)
paddle_left.penup()
paddle_left.goto(-350,0)



#game paddle right

paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.color('white')
paddle_right.shape('square')
paddle_right.penup()
paddle_right.shapesize(stretch_len=1,stretch_wid=5)
paddle_right.goto(350,0)





#game scoreboard

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.color('white')
pen.goto(0,260)
pen.hideturtle()
pen.write('PLAYER A:0   PLAYER B:0',align='center',font=('Courier',24,'normal'))




#game score
score_a=0
score_b=0



#game ball

ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.goto(0,0)
ball.speed(0)
ball.penup()
ball.dx = 0.3
ball.dy = 0.3




#moving the paddles

def paddle_left_up():
    y = paddle_left.ycor()
    y+=20
    paddle_left.sety(y)
    

def paddle_left_down():
    y = paddle_left.ycor()
    y-=20
    paddle_left.sety(y)


def paddle_right_up():
    y = paddle_right.ycor()
    y+=20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y-=20
    paddle_right.sety(y)

#listening to keybord
wn.listen()
wn.onkeypress(paddle_left_up,'w')
wn.onkeypress(paddle_left_down,'s')
wn.onkeypress(paddle_right_up,'Up')
wn.onkeypress(paddle_right_down,'Down')





while True:
    wn.update()


    #moving the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)


    #creating borders for the game
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('boing.wav',winsound.SND_ASYNC)


    if ball.ycor() < - 290:
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound('boing.wav',winsound.SND_ASYNC)

    if ball.xcor() > 395:
        ball.goto(0,0)
        ball.dx *=-1
        pen.clear()
        winsound.PlaySound('boing.wav',winsound.SND_ASYNC)
        score_a+=1
        pen.write('PLAYER A:{}   PLAYER B:{}'.format(score_a,score_b),align='center',font=('Courier',24,'normal'))


    if ball.xcor() < -395:
        ball.goto(0,0)
        ball.dx*=-1
        pen.clear()
        winsound.PlaySound('boing.wav',winsound.SND_ASYNC)
        score_b+=1        
        pen.write('PLAYER A:{}   PLAYER B:{}'.format(score_a,score_b),align='center',font=('Courier',24,'normal'))


    #hitting the ball with paddles    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        winsound.PlaySound('boing.wav',winsound.SND_ASYNC)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-340)
        winsound.PlaySound('boing.wav',winsound.SND_ASYNC)
        ball.dx *=-1    