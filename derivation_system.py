#$BH=CG%/%i%9(B
class Judgement():
    def __init__(self,judgement,my_id=0,rule=None):
        #$B$3$NH=CG$rF3$$$?5,B'(B
        self.rule = rule
        self.str = judgement
        self.id = my_id 
        #$BD>2<$N;R$NH=CG$N(Bid
        self.childs_id = list()

#$B%Z%"%N?t(B
class PeanoNum():
    def __init__(self,peano):
        #S(S(S...(Z)...))$B$N(BS$B$N?t(B
        if peano=="Z":
            self.s_num = 0
        else:
            self.s_num = peano.count("S") 

    def succ(self):
        return self._toPeano(self.s_num + 1)

    def prev(self):
        return self._toPeano(self.s_num - 1)

    #$B<+J,(B-$B0z?t(B
    def sub(self,peano):
        s_num = self.s_num - peano.s_num
        return self._toPeano(s_num)

    def _toPeano(self,num):
        if num==0:
            return PeanoNum("Z")
        peano = str()
        for i in range(num):
            peano += "S("
        peano += "Z"
        for i in range(num):
            peano += ")"
        return PeanoNum(peano)

    def toStr(self):
        peano = str()
        if self.s_num==0:
            return "Z"
        for i in range(self.s_num):
            peano += "S("
        peano += "Z"
        for i in range(self.s_num):
            peano += ")"
        return peano

#$B%7%9%F%`$N%Y!<%9%/%i%9(B
#1.$B%k!<%HH=CG$+$i;RH=CG$r@8@.$7!$%9%?%C%/$9$k(B
#2.$B%k!<%HH=CG$NJ8;zNs$r@8@.$7$F;RH=CG$N(Bid$B$rJ8;zNs$KKd$a9~$`(B
#3.$B;RH=CG$,B8:_$7$J$+$C$?>l9g!$J8;zNs$rKd$a9~$^$:%+%C%3$rJD$8$k(B
#4.self.string$B$N(Bid$B$r@8@.$7$?J8;zNs$GCV$-49$($k(B
#3.$B%9%?%C%/$+$iH=CG$r0l$D%]%C%W$7!$$=$l$rBP>]$H$7$F(B
#3.$BMU%N!<%I$K$?$I$jCe$$$?$i(B
class System():
    def __inint__(self,judgement):
        #$B:#BP>]$H$7$F$$$kH=CG(B
        self.pointer = judgement
        #$B;RH=CG$r%9%?%C%/$9$k(B
        self.childs = list()
        #$B:G=*E*$J=PNO7k2L$H@.$kJ8;zNs(B
        self.string = "0"

    def run(self):
        self.stack()
        #self.string$B$N(Bid$B$rCV$-49$($kJ8;zNs$r@8@.(B
        j_id = self.pointer.id
        j_str = self.pointer.str
        j_rule = self.pointer.rule
        jud = j_str + "by {} {".format(j_rule)
        if self.pointer.childs_id==[]:
            jud += "}"
        else:
            for child_id in self.pointer.childs_id:
                jud += str(child_id) + "; "

        self.string.replace(str(j_id),jud)
        self.pointer = self.childs.pop()
        
        self.run()
        
#self.child$B$K;RH=CG$NJ8;zNs$rJ];}(B
#gen$B$G;RH=CG$rJV$9(B
class Nat(System):
    def __init__(self,judgement):
        super().__init__(judgement)
        self._str2tree()

    #$B5,B'$rE,MQ$7!$;RH=CG$r%9%?%C%/$9$k(B                
    def stack(self):
        self._parse()
        if self.rule=="P-Zero":
            self._pZero()
        elif self.rule=="P-Succ":
            self._pSucc()
        elif self.rule=="T-Zero":
            self._tZero()
        elif self.rule=="T-Succ":
            self._tSucc()

    #$BJ8;zNs$r07$$$d$9$$7A<0$K(B
    def _str2tree(self):
        bara = self.pointer.str.split()
        bara[0] = PeanoNum(bara[0])
        bara[2] = PeanoNum(bara[2])
        bara[4] = PeanoNum(bara[4])
        self.tree = bara

    #$B$I$N5,B'$r;H$C$F;RH=CG@8@.$9$k$+H=Dj(B
    def _parse(self):
        if self.tree[1]=="plus":
            if self.tree[0].s_num==0:
               self.rule = "P-Zero"
            else:
               self.rule = "P-Succ"
        elif self.tree[1]=="times":
            if self.tree[0].s_num==0:
                self.rule = "T-Zero"
            else:
                self.rule = "T-Succ"

    def _pZero(self):
        self.pointer.rule = "P-Zero"

    def _pSucc(self):
        tree = self.tree

        sn1 = tree[0]
        n1 = sn1.prev()
        n2 = tree[2]
        sn = tree[4]
        n = sn.prev()

        tree[0] = n1.toStr()
        tree[2] = n2.toStr()
        tree[4] = n.toStr()
        child_id = self.id + 1 
        child_jud = ' '.join(tree)
        child_judgement = Judgement(child_jud,child_id,self.id)
        self.childs.append(child_judgement)
        self.pointer.rule = "P-Succ"
        self.pointer.childs_id.append(child_id)

    def _tZero(self):
        self.pointer.rule = "T-Zero"

    def _tSucc(self):
        jud = self.tree

        sn1 = jud[0]
        n1 = sn1.prev()
        n2 = jud[2]
        n4 = jud[4]
        n3 = n4.sub(n2)

        child_id1 = self.id + 1
        child_jud1 = '{0} times {1} is {2}'.format(n1.toStr(),n2.toStr(),n3.toStr())
        child_judgement1 = Judgement(child_jud1,child_id1,self.id,"T-Succ")
        child_id2 = child_id1 + 1
        child_jud2 = '{0} plus {1} is {2}'.format(n2.toStr(),n3.toStr(),n4.toStr())
        child_judgement2 = Judgement(child_jud2,child_id2,self.id)
        self.childs.append(child_judgement1)
        self.childs.append(child_judgement2)
        self.pointer.rule = "T-Succ"
        self.pointer.childs_id.append(child_id1)
        self.pointer.childs_id.append(child_id2)

if __name__=='__main__':
    #peano = "S(S(S(S(Z))))"
    #peano = "Z"
    #a = PeanoNum(peano)
    #a.succ()
    #a.succ()
    #a.succ()
    #a.succ()
    #print(a.toStr())
    n = Nat("Z plus S(S(Z)) is S(S(Z))")
    print(n.tree)
