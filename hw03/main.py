import time
import turtle as t
import os
def draw_rectangle(start_x,start_y,x,y):
    t.goto(start_x,start_y)
    t.color('red','red')
    t.begin_fill()
    for i in range(2):
        t.forward(x)
        t.left(90)
        t.forward(y)
        t.left(90)
    t.end_fill()
 

def draw_star(center_x,center_y,radius):
    t.setpos(center_x,center_y)
    #find the peak of the five-pointed star
    pt1=t.pos()
    t.circle(-radius,72)
    pt2=t.pos()
    t.circle(-radius,72)
    pt3=t.pos()
    t.circle(-radius,72)
    pt4=t.pos()
    t.circle(-radius,72)
    pt5=t.pos()
    #draw the five-pointed star
    t.color('yellow','yellow')
    t.begin_fill()
    t.goto(pt3)
    t.goto(pt1)
    t.goto(pt4)
    t.goto(pt2)
    t.goto(pt5)
    t.end_fill()

#start the project
t.speed(2)
t.penup()
#draw the rectangle
star_x=-320
star_y=-260
len_x=660
len_y=440
draw_rectangle(star_x,star_y,len_x,len_y)
#draw the big star
pice=660/30
big_center_x=star_x+5*pice
big_center_y=star_y+len_y-pice*5
t.goto(big_center_x,big_center_y)
t.left(90)
t.forward(pice*3)
t.right(90)
draw_star(t.xcor(),t.ycor(),pice*3)
#draw the small star
t.goto(star_x+10*pice,star_y+len_y-pice*2)
t.left(t.towards(big_center_x,big_center_y)-t.heading())
t.forward(pice)
t.right(90)
draw_star(t.xcor(),t.ycor(),pice)
#draw the second star
t.goto(star_x+pice*12,star_y+len_y-pice*4)
t.left(t.towards(big_center_x,big_center_y)-t.heading())
t.forward(pice)
t.right(90)
draw_star(t.xcor(),t.ycor(),pice)
#draw the third
t.goto(star_x+pice*12,star_y+len_y-7*pice)
t.left(t.towards(big_center_x,big_center_y)-t.heading())
t.forward(pice)
t.right(90)
draw_star(t.xcor(),t.ycor(),pice)
#draw the final
t.goto(star_x+pice*10,star_y+len_y-9*pice)
t.left(t.towards(big_center_x,big_center_y)-t.heading())
t.forward(pice)
t.right(90)
draw_star(t.xcor(),t.ycor(),pice)
