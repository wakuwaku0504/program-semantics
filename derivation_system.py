#判断クラス
class Judgement():
    def __init__(self,judgement,my_id=0,rule=None):
        #この判断を導いた規則
        self.rule = rule
        self.str = judgement
        self.id = my_id 
        #直下の子の判断のid
        self.childs_id = list()

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

#システムのベースクラス
#1.ルート判断から子判断を生成し，スタックする
#2.ルート判断の文字列を生成して子判断のidを文字列に埋め込む
#3.子判断が存在しなかった場合，文字列を埋め込まずカッコを閉じる
#4.self.stringのidを生成した文字列で置き換える
#3.スタックから判断を一つポップし，それを対象として
#3.葉ノードにたどり着いたら
class System():
    def __inint__(self,judgement):
        #今対象としている判断
        self.pointer = judgement
        #子判断をスタックする
        self.childs = list()
        #最終的な出力結果と成る文字列
        self.string = "0"

    def run(self):
        self.stack()
        #self.stringのidを置き換える文字列を生成
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
        
#self.childに子判断の文字列を保持
#genで子判断を返す
class Nat(System):
    def __init__(self,judgement):
        super().__init__(judgement)
        self._str2tree()

    #規則を適用し，子判断をスタックする                
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

    #文字列を扱いやすい形式に
    def _str2tree(self):
        bara = self.pointer.str.split()
        bara[0] = PeanoNum(bara[0])
        bara[2] = PeanoNum(bara[2])
        bara[4] = PeanoNum(bara[4])
        self.tree = bara

    #どの規則を使って子判断生成するか判定
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
