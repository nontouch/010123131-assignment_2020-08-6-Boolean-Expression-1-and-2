import pygame
from Boolean_expression_2 import CreateTree # create tree by list
from sub_boolean2 import Boolean_algebra # Split a Expression to a list
import sub_boolean1

width,high = 800,600

# Colour Set
Black = (0,0,0)
White = (255,255,255)
Green = (0,255,0)
Red = (255,0,0)
blue = (82,220,200)
Blue = (82,100,220)


pygame.init()

display = pygame.display.set_mode([width,high],0,32)
pygame.display.set_caption(" Binary Tree of equation ")
myfont = pygame.font.SysFont("Comic Sans MS",20)
display.fill(White)

#----------------------------------------------Class Node & Line#----------------------------------------------
class Node:
    def __init__(self, x, y, text, radian=20):
        self.x = x
        self.y = y
        self.text = text
        self.radian = radian

    def draw(self, colour):
        # if text is "" then ignore them
        if(self.text != ""):
            pygame.draw.circle( display, colour, [self.x, self.y], self.radian )
            label = myfont.render( str(self.text),1,(Black) )
            display.blit( label,(self.x-5, self.y-15) )
            pygame.display.update()

class Line:
    def __init__(self, x_start, y_start):
        self.x_start = x_start
        self.y_start = y_start

    def draw(self, target ,colour):
        # Is a target node ""
        if(target.text != ""):
            pygame.draw.line(  display, colour, [self.x_start,self.y_start], [target.x, target.y], 5)
            pygame.display.update()
        else:
            pass

#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
class DrawTree:
    def __init__(self, tree, expression):
        self.radian = 20
        self.Level = 5 # level of tree
        self.column = 2**(self.Level-1) # column
        self.W = width//self.column
        self.H = high//self.Level
        self.pos_draw_line = []
        self.tree = tree
        self.expression = expression

    def run_pygame(self):
        self.cut()
        self.pre_draw_node()
        self.connect_node_and_line()

        running = True
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.image.save(display, f"{self.expression}.jpg")
                    running = False

            label = myfont.render( str(self.expression),1,(Black) )
            display.blit( label,(0, 0) )
            pygame.display.update()
            
        display.fill(White)
        pygame.display.update()

    def cut(self):
        temp = [""]*31
        for i in range(len(self.tree)) :
            if i < 31 :
                temp[i] = self.tree[i]
            else :
                pass
        print(len(temp))

        self.tree = temp

    def pre_draw_node(self):
        y = (high - self.radian-200) # 200 is offset bottom
        border = self.radian
        Index = len(self.tree)-1

        for R in range(self.Level): # level of tree
            Power = (2**R) # number of node
                
            # W*Power is divided node on each level
            for i in range(width-border-5, border, -self.W*Power): # since (far left border) to (far right borader)
                x = i
                circle = Node(x, y, self.tree[Index])
                self.pos_draw_line.append(circle)

                Index -= 1

            border += Power*25 # Level 5
            
            # ***************NO Use************************
            #border += Power*54 # Level 4
            #border += Power*126 # Level 3
            #border += Power*379 # Level 2
            #border += Power # Level 1
            # *********************************************

            y -= self.H + self.radian -80 # 80 is offset distance each level

    def connect_node_and_line(self):
        self.pos_draw_line.reverse()

        for j in range(len(self.pos_draw_line)):
            # q is root index
            # pl is left index
            # pr is right index
            print(self.pos_draw_line[j].x, self.pos_draw_line[j].y, self.pos_draw_line[j].text)

            # set index
            q = j
            pl = 2*q + 1
            pr = 2*q + 2

            if(  pr > len(self.pos_draw_line)-1  ):
                break

            # set x, y and text in target node
            x_node = self.pos_draw_line[q].x
            y_node = self.pos_draw_line[q].y
            text_node = self.pos_draw_line[q].text
            
            # draw line to target
            line = Line(x_node, y_node)
            line.draw(self.pos_draw_line[pl], Black)
            line.draw(self.pos_draw_line[pr], Black)

            # draw node after draw line because I want node cover line
            self.pos_draw_line[q].draw(Blue)
            self.pos_draw_line[pl].draw(Blue)
            self.pos_draw_line[pr].draw(Blue)
#------------------------------------------------------------------------------------------------------------
# (I0+!I1+!(I2))&(!I0+I1+I2) Test 3
#                                       &
#                             /                  \
#                      +                              +
#              /               \                  /       \
#            +                    !            +             I2
#          /    \               /            /   \          
#      I0        !           I2            !      I1      
#              /                         /
#            I1                        I0

if __name__ == "__main__":
    # data set for testing my algorithm
    Test_data_set = (  "!(1+0)" # index 0
                        ,"!(!(0+I0&1))" # index 1
                        ,"(I0+!I1+!(I2))&(!I0+I1+I2)" # index 2
                        ,"!(I0&I1)+!(I1+I2)" # index 3
                        ,"(((I0&I1&!I2)+!I1)+I3)" # index 4
                        ,"((I2&I1)+(I0&I1))" # index 5
                        ,"I2&I1+I0&I1" # index 6
                        ,"(I0&I1+!(I1&I2))" # index 7
                        ,"!!!I1+!!I0" # index 8
                        ,"I1&I0+I3&!!I0" # index 9
                        ,"!!!I0" # index 10  
                        ,"(!A&!B&!C) + (!A&!B&!C)"  ) # index 11

    #Test_data_set = Read("C:\\Users\\s6201012620279\\Software development\\050863\Tree\\New Version\\Input.txt").getInput()
    
    for exp in Test_data_set:
        filter = sub_boolean1.check_bracket()
        split_expression = Boolean_algebra(exp)
        complete_split_expression = split_expression.split_expreesion()
        side_list = len(split_expression.operate) + len(split_expression.operator)
        Test = CreateTree(side_list)
        tree = Test.Tree('','','',complete_split_expression, 0)
        print(tree)
        pen = DrawTree(tree, exp)
        pen.run_pygame()
        
    pygame.quit()