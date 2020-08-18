class check_bracket:
    def __init__(self):
        self.stack = []

    def check_last(self, test):
        # put method before for loop in create tree class
        for i in range(len(test)):
            if(test[i] == "("):
                # stack index 0 is "(" and stack index 1 is index where "(" exist
                self.stack.append([test[i], i])

            elif(test[i] == ")"):
                position_ = self.stack.pop()
                range_bracket = i - position_[1]
                # if "(" and ")" has range same length of subject list cut off both
                if(range_bracket == len(test)-1):
                    return test[1:-1]
        
        return test # return a list is cut already

"""# ----------------Testing class--------------------
testing_data_set = (  "(1+0)" # index 0
                    , "(0+I0&1)" # index 1
                    , "(I0+!I1+!(I2))" # index 2
                    , "(!(I0&I1)+!(I1+I2))" # index 3
                    , "(I3+I4)"  ) # index 4
for test in testing_data_set:
    Testing = check_bracket()
    print(test,"==>",Testing.check_last(test))
    print("-"*100)"""