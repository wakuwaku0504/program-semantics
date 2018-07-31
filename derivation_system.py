#  class Tree():
    #  def __init__(self,tree0,tree1,op):
        #  self.top = 

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
#1.self.pointerの判断からself.stackによって子判断を生成し，self.childsにスタックする
#2.self.pointerの判断の文字列を生成して子判断のidを文字列に埋め込む
#3.子判断が存在しなかった場合，文字列を埋め込まずカッコを閉じる
#4.self.stringのidを生成した文字列で置き換えたものを新たなself.stringとする
#5.self.childsスタックから判断を一つポップし，それを対象としてself.pointerに代入
#6.1に戻る
#7.self.childsが空になったら終了
#self.stackはシステム独自に定義する
#self.stackは，self.pointerを導くルールと判断（子判断）を
#解析し，
#・子判断はself.childsにスタック
#・self.pointer.childs_idに子判断のidをappend
#・self.pointer.ruleにルールを代入
#する
class System():
    def __init__(self,judgement):
        #今対象としている判断
        self.pointer = judgement
        #子判断をスタックする
        self.childs = list()
        #最終的な出力結果となる文字列
        self.string = "0"

    #解析実行
    def run(self):
        self.stack()
        #self.stringのidを置き換える文字列を生成
        j_id = self.pointer.id
        j_str = self.pointer.str
        j_rule = self.pointer.rule
        jud = j_str + " by {} ".format(j_rule) + "{"
        if not self.pointer.childs_id==[]:
            for child_id in self.pointer.childs_id:
                jud += str(child_id) + "; "
        jud += "}"
        self.string = self.string.replace(str(j_id),jud)
        if self.childs==[]:
            return 
        self.pointer = self.childs.pop()
        self.run()
        
class Nat(System):
    def __init__(self,judgement):
        super().__init__(judgement)
        #項を分割する文字列
        self.splitter = ["plus","times","is"]

    #規則を適用し，子判断をスタックする                
    def stack(self):
        self._str2tree()
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
        self._str2tree()
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
        child_id = self.pointer.id + 1 
        child_jud = ' '.join(tree)
        child_judgement = Judgement(child_jud,child_id)
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

        child_id1 = self.pointer.id + 1
        child_jud1 = '{0} times {1} is {2}'.format(n1.toStr(),n2.toStr(),n3.toStr())
        child_judgement1 = Judgement(child_jud1,child_id1)
        child_id2 = child_id1 + 1
        child_jud2 = '{0} plus {1} is {2}'.format(n2.toStr(),n3.toStr(),n4.toStr())
        child_judgement2 = Judgement(child_jud2,child_id2)
        self.childs.append(child_judgement1)
        self.childs.append(child_judgement2)
        self.pointer.rule = "T-Succ"
        self.pointer.childs_id.append(child_id1)
        self.pointer.childs_id.append(child_id2)

#  class EvalNatExp(Nat):
    #  def __init__(self,judgement)
        #  super().__init__(judgement)
        #  self.splitter.append("evalto")

    #  def 




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
