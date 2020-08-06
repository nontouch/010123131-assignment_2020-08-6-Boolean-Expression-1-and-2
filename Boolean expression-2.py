###################################################################
# File: Boolean expression part 2
# Date: 2020-08-06
###################################################################


import pygame
import math

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

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def oop(op,data1,data2) :                       #เป็นฟังก์ชั่นสำหรับการคำนวณค่าโดยดูว่าจะใช้ตัวoperationอะไร
    if op == "+" :
        if data1 == "0" and data2 == "0" :
            ans = "0"
            return ans
        elif data1 == "0" and data2 == "1" :
            ans = "1"
            return ans
        elif data1 == "1" and data2 == "0" :
            ans = "1"
            return ans
        elif data1 == "1" and data2 == "1" :
            ans = "1"
            return ans
    elif op == "&" :
        if data1 == "0" and data2 == "0" :
            ans = "0"
            return ans
        elif data1 == "0" and data2 == "1" :
            ans = "0"
            return ans
        elif data1 == "1" and data2 == "0" :
            ans = "0"
            return ans
        elif data1 == "1" and data2 == "1" :
            ans = "1"
            return ans
 
    

def caltree(data) :                        #เป็นฟังก์ชั่นคำนวณ expression tree list
    n = len(data)
    h = math.log2(n+1)-1              #เป็นสมการหาควาทสูงของ tree
    h1 = int(h)
    NewList = []
    TempList = ''
    #print(data)
    for i in range(h1,-1,-1) :                 #เป็นการวนเพื่อไล่ระดับความสูงจากชั้นล่างสุดถึงบนสุดของtree
        for j in range(2**i) :                  #เป็นการวนเพื่อไล่จำนวนสมาชิกของเเต่ละชั้นของtreeเพื่อใช้ในการคำนวณ
            """if data[-1] not in '&+' and data[-1] != 'None' :         #เป็นเงื่อนไขเพื่อบอกว่าหากสมาชิกตัวสุดท้ายของข้อมูลเป็นตัวเลขให้นำค่านั้นใส่ในlistชั่วคราวที่ใช้ในการเก็บตัวเลขสำหรับคำนวณ
                number = data.pop()
                NewList.append(number)
                print(NewList)"""
            if data[-1] in '&+' :                 #เป็นเงื่อนไขเพื่อบอกว่าหากสมาชิกตัวสุดท้ายของข้อมูลเป็นoperationให้ลบค่าตัวเลขสองตัวสุดท้ายจากlistชั่วคราวที่ใช้ในการเก็บตัวเลขสำหรับคำนวณเเละเรียกฟังก์ชั่นoopโดยเเทนเลขสองตัวนั้นเเละค่าoperateลงไปเพื่อคำนวณ
                ope = data.pop()
                x = NewList.pop(0)
                #print(NewList)
                y = NewList.pop(0)
                #print(NewList)
                cal = oop(ope,y, x)
                TempList = cal        #หลังคำนวณเสร็จให้เก็บค่าที่คำนวณเเล้วในlistชั่วคราวอีกตัว
                #print(TempList)
            elif data[-1] not in '&+' and data[-1] != 'None' :         #เป็นเงื่อนไขเพื่อบอกว่าหากสมาชิกตัวสุดท้ายของข้อมูลเป็นตัวเลขให้นำค่านั้นใส่ในlistชั่วคราวที่ใช้ในการเก็บตัวเลขสำหรับคำนวณ
                number = data.pop()
                NewList.append(number)
                #print(NewList)
            elif data[-1] == 'None' :       #เป็นเงื่อนไขเพื่อบอกว่าหากสมาชิกตัวสุดท้ายของข้อมูลเป็น 'None' ให้ลบตัวนั้นออก
                del(data[-1])                 #โดยทุกๆเงื่อนไขจะมีการลบค่าที่นำมาเทียบกับตัวเงื่อนไขออกจากlistข้อมูลเสมอเพื่อข้อมูลที่ใช้เเล้วออกไป
            #print(data)
            if TempList != '' :
                NewList.append(TempList)
            #print(NewList)
    return NewList[0]

        
bruh = "((I0&I1) + !(I1&I2))" 
zee = Boolean(bruh)
test = zee.equation_f
#print(test)
test2 = three(test)
#print(test2.ptree)
final = test2.making()

I0 , I1 = '0' , ''
I2 = ''
digit = ['0','1']
print("_______________________")
print("I0 : I1  : I2  | output")
for j in range(2**3) :
    if I1 == '1' and I2 == '1' :
        I0 = '1'
        I1 , I2 = '0' , '0'
    elif I2 == '1' :
        I1,I2 = '1' , '0'
    elif I2 == '0' :
        I2 = '1'
    else :
        I0 , I1 , I2 = '0' , '0' , '0'
    #print(I2)
    for i in range(len(final)) :
        if final[i] == "I0" :
            final[i] = I0
        elif final[i] == "I1" :
            final[i] = I1
        elif final[i] == "I2" :
            final[i] = I2
        elif final[i] == "!I0" :
            if I0 == "1" :
                final[i] = '0'
            elif I0 == "0" :
                final[i] = "1"
        elif final[i] == "!I1" :
            if I1 == "1" :
                final[i] = "0"
            elif I1 == "0" :
                final[i] = "1"
        elif final[i] == "!I2" :
            if I2 == "1" :
                final[i] = "0"
            elif I2 == "0" :
                final[i] = "1"

    #print(final)
    Do_logic = caltree(final)
    print("_______________________")
    print(I0 ," : ",I1 ," : ",I2 ," | ",Do_logic)

    bruh2 = "((I0&I1) + !(I1&I2))" 
    zee2 = Boolean(bruh2)
    test3 = zee2.equation_f
    #print(test)
    test4 = three(test3)
    #print(test2.ptree)
    final = test4.making()
    #print(final)
    #print(remake)
print("_______________________")


#____________________________________________________________________________________________________________________
"""width,high = 1000,800
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

pygame.quit()"""
