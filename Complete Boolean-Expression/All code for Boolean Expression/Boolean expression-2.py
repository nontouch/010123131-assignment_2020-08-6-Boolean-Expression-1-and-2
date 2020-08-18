###################################################################
# File: Boolean expression part 2
# Date: 2020-08-06
###################################################################


import pygame
import math
import sub_boolean1 # Filter a bracket
import sub_boolean2 # Split a Expression to a list
import sub_boolean3

class CreateTree:

    def __init__(self,side):
        self.stack = []
        i = 0
        while True :
            if side <= (2**(i))-1 :
                temp = 2**(i) - 1
                break
            else :
                i += 1
        self.tree_list = [""]*temp*3
        #self.variable = ["I0","I1","I2","I3","1","0"]
        #self.posfix = []

    def Tree(self, left, right, root, test, q):
        # ******************************Preorder********************************
        stack_or = []
        stack_and = []
        RUN_OR = True
        test = filter.check_last(test)
        for i in range(len(test)):
            # check "(" and ")"
            if( test[i] == "(" ):
                RUN_OR = False
                self.stack.append(i)
            elif( test[i] == ")"):
                self.stack.pop()

            # if stack is empty
            if(len(self.stack) == 0):
                RUN_OR = True

            # filter "!" sinario !(I0&I1), (!I1&I2) and !(I0) etc
            if( (test[i] == "!") ):
                if(RUN_OR == False):
                    pass
                elif(RUN_OR == True):
                    if( root != "!" ):
                        Is_joke = filter.check_last(test[i+1:])
                        root = test[i]
                        left = Is_joke
                        right = right

                #print(RUN_OR)
                #print(f"test:{test} \nleft {left} \nroot {root} \nright {right}\n-----------------------")
            
            if(RUN_OR):
                # find the max position of + for split to left root right
                if(test[i] == "+"):
                    max_position_of_or = i
                    root = test[max_position_of_or]
                    left = test[:max_position_of_or]
                    right = test[max_position_of_or+1:]
                    stack_or.append(max_position_of_or)

                if(test[i] == "&"):
                    max_position_of_and = i
                    root = test[max_position_of_and]
                    left = test[:max_position_of_and]
                    right = test[max_position_of_and+1:]
                    stack_and.append(max_position_of_and)

                if(len(stack_and) > 0):
                    root = test[max_position_of_and]
                    left = test[:max_position_of_and]
                    right = test[max_position_of_and+1:]
                    
                if(len(stack_or) > 0):
                    root = test[max_position_of_or]
                    left = test[:max_position_of_or]
                    right = test[max_position_of_or+1:]
        
        pl = (2*q)+1
        pr = (2*q)+2
        self.tree_list[q] = root
        self.tree_list[pl] = left
        self.tree_list[pr] = right

        # *** (2*q)+1 = left index
        # *** (2*q)+2 = right index
        # *** q = root index

        # meter checking value recursive value
        ###print(f"test:{test} \nleft {left} \nroot {root} \nright {right}\n-----------------------")###
        # ######

        # ******************************Postorder********************************
        if(len(left) == 1):
            self.tree_list[pl] = left[0]
            if( len(right) > 1):
                ###print("###############Postorder###############")###
                self.Tree("", "", "", right, pr)
            else:
                if(right == ""):
                    self.tree_list[pr] = right
                else:
                    self.tree_list[pr] = right[0]
            return self.tree_list

        self.Tree("", "", "", left, pl)

        # all left finish

        if( len(right) > 1 ):
            ###print("###############Postorder###############")###
            self.Tree("", "", "", right, pr)
        else:
            if(right == ""):
                self.tree_list[pr] = right
            else:
                self.tree_list[pr] = right[0]
        
        ###print(q)###
        return self.tree_list


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# data set for testing my algorithm
file_input = open("C:\\Users\\User\\Documents\\Boolean expression input.txt", "r")
complete_file = file_input.read()
input_already = complete_file.split("\n")

for index in range(len(input_already)) :

    q = 0
    # split bracket from file sub_boolean1
    filter = sub_boolean1.check_bracket()
    # manage input to make Tree expression from sub_boolean2
    pre_split_expression = sub_boolean2.Boolean_algebra(input_already[index]) 
    # use function at class Boolean_algebra from sub_boolean2
    split_expression = pre_split_expression.split_expreesion() 
    # calculate side
    side_list = len(pre_split_expression.operate) + len(pre_split_expression.operator) 
    # use CreateTree class
    Test = CreateTree(side_list)
    # use function from CreateTree class
    show = Test.Tree('','','',split_expression, q)

    print("*"*60,input_already[index],"*"*60)
    print(show)
    operated = pre_split_expression.operate2
    truth_table = sub_boolean3.Truth_Table(show,operated,"Truth Table of  " + input_already[index])
    truth_table.Make_table(show)

    print('\n ',"="*175,'\n \n')
