from derivation_system import * 

class Judgement():
    def __init__(self,judgement,my_id=0,parent_id=-1):
        self.judge = judgement
        self.id = my_id 
        self.parent = parent_id

if __name__=="__main__":
    #  jud = Judgement("Z plus S(S(Z)) is S(S(Z))")
    #  jud = Judgement("S(S(Z)) plus Z is S(S(Z))")
    jud = Judgement("S(Z) plus S(S(S(Z))) is S(S(S(S(Z))))")
    s = Nat(jud)
    rule, child = s.gen()
    print(rule,child)



