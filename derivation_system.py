#ペアノ数
class PeanoNum():
    def __init__(self,peano):
        #S(S(S...(Z)...))のSの数
        if peano=="Z":
            self.s_num = 0
        else:
            self.s_num = peano.count("S") 

    def succ(self):
        return self._toPeano(self.s_num + 1)

    def prev(self):
        return self._toPeano(self.s_num - 1)

    #自分-引数
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

#self.childに子判断の文字列を保持
#genで子判断を返す
class Nat():
    def __init__(self,judgement):
        self.judgement = judgement.judge
        self.child = list()
        self._str2tree()

    #規則を適用し，子判断を返す                
    def gen(self):
        self._parse()
        if self.rule=="P-Zero":
            self._pZero()
        elif self.rule=="P-Succ":
            self._pSucc()
        elif self.rule=="T-Zero":
            self._tZero()
        elif self.rule=="T-Succ":
            self._tSucc()
        return self.rule,self.child

    #文字列を扱いやすい形式に
    def _str2tree(self):
        bara = self.judgement.split()
        bara[0] = PeanoNum(bara[0])
        bara[2] = PeanoNum(bara[2])
        bara[4] = PeanoNum(bara[4])
        self.tree = bara

    #どの規則を使って子判断生成
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
        self.child.append("")

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
        self.child.append(' '.join(tree))

    def _tZero(self):
        self.child.append("")

    def _tSucc(self):
        jud1 = self.tree
        sn1 = jud1[0]
        n1 = sn1.prev()
        n2 = jud1[2]
        n4 = jud1[4]
        n3 = n4.sub(n2)
        jud1[0] = n1.toStr()
        jud1[2] = n2.toStr()
        jud1[4] = n3.toStr()
        self.child.append(' '.join(jud1))
        self.child.append('{0} plus {1} is {2}'.fomat(n2.toStr(),n3.toStr(),n4.toStr()))

        

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
