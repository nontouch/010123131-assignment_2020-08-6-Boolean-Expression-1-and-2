class Boolean_algebra:
    def __init__(self, original):
        self.equation = original
        self.operator = [] # contain Operator
        self.operate = []  # contain Operate
        self.operate2 = []
        self.equation_list = [] # contain a expreesion is split already
        self.operator_include = ["+", "&", "!"]
        self.operate_sum = ""
        #self.char = [chr(i) for i in range(65,91)] # contain alphabet A-B only upper case
        #self.number = [str(i) for i in range(10)] # contain number 0-9 only upper case

    def split_expreesion(self):

        self.split_space()
        equation = self.equation

        for i in range(len(equation)) :
            element = equation[i]
            if element == '(' :
                self.equation_list.append(element)

            elif element in self.operator_include or element == ')' :
                if element != ')' :
                    self.operator.append(element)

                if len(self.operate_sum) != 0 :
                    self.operate.append(self.operate_sum)
                    self.equation_list.append(self.operate_sum)
                    if self.operate_sum not in self.operate2 and self.operate_sum not in "01":
                        self.operate2.append(self.operate_sum)

                self.equation_list.append(element)
                self.operate_sum = ""

            else :
                self.operate_sum += element

                if i+1 == len(equation) and self.operate_sum != 0 :
                    self.operate.append(self.operate_sum)
                    self.equation_list.append(self.operate_sum)
                    if self.operate_sum not in self.operate2 and self.operate_sum not in "01":
                         self.operate2.append(self.operate_sum)

        return self.equation_list

    def split_space(self) :
        no_space_equation = ""
        for element in self.equation :
            if element == " " :
                pass
            else :
                no_space_equation += element
        self.equation = no_space_equation



# ----------------Testing class--------------------
"""testing_data_set = (  "!(1+0)" # index 0
                    , "!(!(0+I0&1))" # index 1
                    , "(I0+!I1+!(I2))&(!I0+I1+I2)" # index 2
                    , "!(I0&I1)+!(I1+I2)" # index 3
                    , "(((I0&I1&!I2)+!I1)+I3)"  ) # index 4
for test in testing_data_set:
    Testing = Boolean_algebra(test)
    print(test,"==>",Testing.split_expreesion())
    print(Testing.operate2)
    print("-"*100)"""