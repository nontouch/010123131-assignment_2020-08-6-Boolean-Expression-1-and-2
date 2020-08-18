
class Truth_Table() :
    def __init__(self,equation,operate,file_name) :
        self.equation = equation
        self.operate = operate
        self.test_operate = {}
        self.head_equation = {}
        self.files = open(f"C:\\Users\\User\\Documents\\{file_name}.txt", "w")
#เป็นฟังก์ชั่นสำหรับการคำนวณค่าโดยดูว่าจะใช้ตัวoperationอะไร
    def operation(self,op,data1,data2) :                   
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

 # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    def calculatetree(self,data) :                        #เป็นฟังก์ชั่นคำนวณ expression tree list
        n = len(data)              
        NewList = []
        equation_form = []
        for i in range(n-1,-1,-1) : 
            arg = data[i] 
            if arg == '0' or arg == '1' :         #เป็นเงื่อนไขเพื่อบอกว่าหากสมาชิกตัวสุดท้ายของข้อมูลเป็นตัวเลขให้นำค่านั้นใส่ในlistชั่วคราวที่ใช้ในการเก็บตัวเลขสำหรับคำนวณ
                NewList.append(arg)
                #if self.equation[i] not in '0,1' :
                equation_form.append(self.equation[i])
            if arg == '&' or arg == '+' :                 
                ope = arg
                x = NewList.pop(0)
                y = NewList.pop(0)
                str1 = equation_form.pop(0)
                str2 = equation_form.pop(0)
                complete_equation = '(' + str1 + ope + str2 + ')'
                cal = self.operation(ope,x, y)
                NewList.append(cal)
                self.head_equation[complete_equation] = cal
                equation_form.append(complete_equation)

            elif arg == '!' :
                z = NewList.pop(0)
                Str = '(' + '!' + equation_form.pop(0) + ')'
                if z == "0" :
                    z = "1"
                else :
                    z = "0"
                NewList.append(z)
                equation_form.append(Str)
                self.head_equation[Str] = z
            elif arg == '' :
                pass

            #print(equation_form)
        return NewList[0]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def Make_table(self,Equation) :
        #self.Equation = Equation
        side = len(self.operate)
        show_head = self.set_head(self.equation)
        self.side_operate = []
        self.side_head = []
        count = 0
        print('#'*175)
        print("_"*150)
        self.files.write('#'*175)
        self.files.write('\n')
        self.files.write("_"*150)
        self.files.write('\n')
        for i in self.operate :
            self.side_operate.append(len(i)+2)
            print(' | ',end="")
            print(i,end="")
            self.files.write(' | ')
            self.files.write(i)
            count += 1
        for i in show_head:
            self.side_head.append(len(i)+2)
            print(' | ',end="")
            print(i,end="")
            self.files.write(' | ')
            self.files.write(i)
            count += 1
        self.line = sum(self.side_operate) + sum(self.side_head) + count
        print(' |')
        print(" "+"_"*self.line + "|")
        self.files.write(' |')
        self.files.write('\n')
        self.files.write(" "+"_"*self.line + "|")
        self.files.write('\n')

        for number in range(2**side) :
            test_digit = bin(number)[2:]
            if len(test_digit) < side :
                more_digit = side - len(test_digit)
                test_digit = ('0'*more_digit) + test_digit
            self.get_digit(test_digit)
            val_equation = self.take_values(Equation)
            output = self.calculatetree(val_equation)
            self.show_table()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def get_digit(self,digit) :
        for ope,Value in zip(self.operate,digit) :
            self.test_operate[ope] = Value

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
    def take_values(self,equ) :
        
        value_equation = []
        for i in equ :
            if i in self.operate :
                value_equation.append(self.test_operate[i])
            else :
                value_equation.append(i)
        return value_equation

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
    def show_table(self) :
        index = 0
        for i in self.test_operate :
            Length =  self.side_operate[index] - 2
            find_mid = int((Length - 1) / 2)
            if (Length - 1) % 2 != 0 :
                left = int(((Length - 1) // 2) + 1)
                right = int((Length - 1) // 2)
                print(' | ',end="")
                print((" "*left) + self.test_operate[i] + (" "*right),end="")
                self.files.write(' | ')
                self.files.write((" "*left) + self.test_operate[i] + (" "*right))
            else :
                left = find_mid
                right = find_mid
                print(' | ',end="")
                print((" "*left) + self.test_operate[i] + (" "*right),end="")
                self.files.write(' | ')
                self.files.write((" "*left) + self.test_operate[i] + (" "*right))
            index += 1

        index = 0
        for i in self.head_equation:
            Length =  self.side_head[index] - 2
            find_mid = int((Length - 1) / 2)
            if (Length - 1) % 2 != 0 :
                left = int(((Length - 1) // 2) + 1)
                right = int((Length - 1) // 2)
                print(' | ',end="")
                print((" "*left) + self.head_equation[i] + (" "*right),end="")
                self.files.write(' | ')
                self.files.write((" "*left) + self.head_equation[i] + (" "*right))
            else :
                left = find_mid
                right = find_mid
                print(' | ',end="")
                print((" "*left) + self.head_equation[i] + (" "*right),end="")
                self.files.write(' | ')
                self.files.write((" "*left) + self.head_equation[i] + (" "*right))
            index += 1

        print(' |')
        print(" "+"_"*self.line + "|")
        self.files.write(' |')
        self.files.write('\n')
        self.files.write(" "+"_"*self.line + "|")
        self.files.write('\n')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def set_head(self,equations) :
        n = len(equations)   
        head = []         
        equation_form = []
        for i in range(n-1,-1,-1) : 
            arg = equations[i] 
            if arg not in '&+!' and arg != '' :         #เป็นเงื่อนไขเพื่อบอกว่าหากสมาชิกตัวสุดท้ายของข้อมูลเป็นตัวเลขให้นำค่านั้นใส่ในlistชั่วคราวที่ใช้ในการเก็บตัวเลขสำหรับคำนวณ
                equation_form.append(arg)
            if arg == '&' or arg == '+':                 
                ope = arg
                str1 = equation_form.pop(0)
                str2 = equation_form.pop(0)
                complete_equation = '(' + str1 + ope + str2 + ')'
                equation_form.append(complete_equation)
                head.append(complete_equation)
               #หลังคำนวณเสร็จให้เก็บค่าที่คำนวณเเล้วในlistชั่วคราวอีกตัว

            elif arg == '!' :
                Str = '(' + '!' + equation_form.pop(0) + ')'
                equation_form.append(Str)
                head.append(Str)
            elif arg == '' :
                pass
        return head


"""test = ['+', '!', '!', '&', '', '+', '', 'I0', 'I1', '', '', 'I1', 'I2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
oper = ['I0','I1','I2']
tabel = Truth_Table(test,oper)
tabel.Make_table(test)"""