###################################################################
# File: Boolean expression part 1
# Date: 2020-08-05
###################################################################

import pygame

class Boolean() :
    def __init__(self,equation) :
        self.equation = []
        if " " in equation :
            equation = equation.split()
            self.equation = equation
            equation = ""
            for e in range(len(self.equation)) :
                equation += self.equation[e]
            self.equation = []
        if equation[0] == "(" :
            equation = equation[1:]
            equation = equation[:-1]
        for i in equation :
            self.equation.append(i)
        for E in range(len(self.equation)) :
            if self.equation[E] == "!" :
                if self.equation[E+1] == "(" :
                    self.equation[E] = "("
                    self.equation[E+1] = "!"
                    if self.equation[E+4] == "&" :
                        self.equation[E+4] = "+"
                    elif self.equation[E+4] == "+" :
                        self.equation[E+4] = "&"
                    self.ele1 = self.equation[E+5:]
                    self.ele2 = self.equation[:-(len(self.ele1))]
                    self.ele2 += "!"
                    self.equation = self.ele2 + self.ele1
        self.equation_f = self.equation
        equation = ""
        for e in range(len(self.equation)) :
            equation += self.equation[e]
        self.equation = []
        for i in range(len(self.equation_f)) :

            if self.equation_f[i] == "I" :
                if self.equation_f[i-1] == "!" :
                    self.equation_f[i-1] += self.equation_f[i] + self.equation_f[i+1]
                    self.equation.append(self.equation_f[i-1])
                else :
                    self.equation_f[i] += self.equation_f[i+1]
                    self.equation.append(self.equation_f[i])
            else :
                if self.equation_f[i] not in "0123456789!" :
                    self.equation.append(self.equation_f[i])

        self.equation_f = self.equation
        self.equation = []


        #print(self.equation_f)

class three() :               #คลาสสำหรับสร้างtree
    
    def __init__(self,data) :       #สำหรับการสร้างขนาดของtree เเบบ  complete
        self.data = data           
        self.ptree = []
        for i in range(len(data)) :     #เป็นการวนไล่เช็คเพื่อตัดวงเล็บในข้อมูลออกเพื่อได้ข้อมูลที่ต้องการ
            if data[i] == '(' or data[i] == ')' or data[i] == '!'  :      # เงื่อนไขสำหรับเช็ควงเล็บ
            #if data[i] == '!'  :
                pass
            else :
                if data[i] not in "&+)" :
                    if data[i-1] == "!" :
                        self.ptree.append(data[i-1] + data[i] )
                    else : 
                        self.ptree.append(data[i])
                else :
                    self.ptree.append(data[i])         #นำข้อมูลที่ไม่มีวงเล็บมาใส่ในlistใหม่
        i = 0
        while True :           #เป็นการวนเพื่อสร้างขนาดของtree เเบบ  complete ที่เหมาะสมกับจำนวนข้อมูล
            if len(self.ptree) <= (2**(i))-1 :      #เงื่อนว่าถ้าจำนวนของข้อมูลมีน้อยกว่าหรือเท่ากับขนาดของtreeให้ทำเงื่อนไขนี้ , (2**(i))-1 คือสมการหาขนาดของtree 
                temp = 2**(i) - 1                  #temp คือตัวเเปรสำหรับเก็บค่าขนาดของtree
                break                         #หยุดloop
            else :
                i += 1
                pass
        self.mylist = ['None'] * temp           #สร้างตัวเเปรสำหรับเก็บค่าlistที่มีสมาชิกเท่ากับtreeเเละเเต่ละตัวเป็นstring Noneเพื่อบอกว่าคือtreeเปล่า
        
    def making(self) :                           #เป็นฟังก์ชั่นเพื่อนำข้อมูลมาจัดให้อยู่ในรูปเเบบtree
        p = 0
        for i in self.data :                           
            self.left = (p * 2) + 1                        #สมการหาตำเเหน่งของnodeลูกฝั่งซ้ายจาก nodeพ่อเเม่
            self.right = (p * 2) + 2                      #สมการหาตำเเหน่งของnodeลูกฝั่งขวาจาก nodeพ่อเเม่
            if i == "(" :                                #เป็นเงื่อนไขเพื่อบอกว่าถ้าเจอวงเล็บเปิดให้ชี้ตำเเหน่งของnodeลูกเป็นตำเเหน่งที่เราสนใจ
                if self.mylist[self.left] == 'None' :      #เป็นเงื่อนไขเพื่อบอกว่าnodeลูกฝั่งซ้ายว่างหรือไม่ถ้าว่างทำ if ถ้าไม่ทำ else
                    p = self.left
                else :                                              
                    p = self.right

            #elif self.data[i] in "0123456789" :
                #pass 

            elif i not in "&+()" :                         #เป็นเงื่อนไขเพื่อบอกว่าถ้าเจอตัวเลขให้ใส่เข้าไปในnodeลูกจากตำเเหน่งที่เราสนใจ
                if self.mylist[self.left] == 'None' :      #เป็นเงื่อนไขเพื่อบอกว่าnodeลูกฝั่งซ้ายว่างหรือไม่ถ้าว่างทำ if ถ้าไม่ทำ else
                    self.mylist[self.left] = i
                else :
                    self.mylist[self.right] = i
            elif i in "&+" :
                if self.mylist[p] == 'None'  :                                   #เป็นเงื่อนไขเพื่อบอกว่าถ้าเจอพวกเครื่องหมายให้ใส่เข้าไปในตำเเหน่งที่เราสนใจหรือก็คือnodeพ่อเเม่
                    self.mylist[p] = i


            else :                              #เป็นเงื่อนไขเพื่อบอกว่าถ้าเจอวงเล็บปิดให้เลื่อนการชี้ตำเเหน่งของnodeลูกเป็นชี้ตำเเหน่งของปู่เป็นตำเเหน่งที่เราสนใจ
                if p%2 == 1 :                   #เป็นเงื่อนไขในกรณีที่เจอว่าวงเล็บปิดอยู่ที่nodeซ้าย
                    p = int((p-1)/2)
                else :
                    p = int((p-2)/2)             #เป็นเงื่อนไขในกรณีที่เจอว่าวงเล็บปิดอยู่ที่nodeซ้าย
                    
        return self.mylist

        
bruh = "((I0&I1) + !(I1&I2))" 
zee = Boolean(bruh)
test = zee.equation_f
print(test)
test2 = three(test)
#print(test2.ptree)
final = test2.making()
print(final)

#____________________________________________________________________________________________________________________
width,high = 1000,800
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0) 
BLUE  = (0, 0, 255)
pygame.font.init() 
text_font = pygame.font.SysFont('browallianewbrowallianewbrowallianewboldbrowallianewitalicbrowalliaupcbrowalliaupcboldbrowalliaupcbolditalicbrowalliaupcitalic', 96)

display = pygame.display.set_mode([width,high])
pygame.display.set_caption("My Boolean")
run = True
while(run):


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    text_surface = text_font.render( f"{final[0]}", False, GREEN )
    pygame.draw.circle(display,WHITE,[500,100],50)
    pygame.draw.rect(display,WHITE,(500,100,280,30))
    pygame.draw.rect(display,WHITE,(750,100,30,200))
    #Left
    pygame.draw.rect(display,WHITE,(500,100,-280,30))
    pygame.draw.rect(display,WHITE,(220,100,30,200))
    display.blit( text_surface,(480,50) )


    text_surface = text_font.render( f"{final[1]}", False, GREEN )
    pygame.draw.circle(display,WHITE,[250,300],50)
    pygame.draw.rect(display,WHITE,(250,300,170,30))
    pygame.draw.rect(display,WHITE,(400,300,30,200))
    #Left
    pygame.draw.rect(display,WHITE,(250,300,-170,30))
    pygame.draw.rect(display,WHITE,(80,300,30,200))
    display.blit( text_surface,(230,250) )

    text_surface = text_font.render( f"{final[2]}", False, GREEN )
    pygame.draw.circle(display,WHITE,[750,300],50)
    pygame.draw.rect(display,WHITE,(750,300,170,30))
    pygame.draw.rect(display,WHITE,(900,300,30,200))
    #Left
    pygame.draw.rect(display,WHITE,(750,300,-170,30))
    pygame.draw.rect(display,WHITE,(570,300,30,200))
    display.blit( text_surface,(730,250) )

    text_surface = text_font.render( f"{final[3]}", False, GREEN )
    pygame.draw.circle(display,WHITE,[100,500],50)
    display.blit( text_surface,(80,450) )


    text_surface = text_font.render( f"{final[4]}", False, GREEN )
    pygame.draw.circle(display,WHITE,[400,500],50)
    display.blit( text_surface,(380,450) )

    text_surface = text_font.render( f"{final[5]}", False, GREEN )
    pygame.draw.circle(display,WHITE,[900,500],50)
    display.blit( text_surface,(880,450) )

    text_surface = text_font.render( f"{final[6]}", False, GREEN )
    pygame.draw.circle(display,WHITE,[600,500],50)
    display.blit( text_surface,(580,450) )
    pygame.display.update()
pygame.quit()


