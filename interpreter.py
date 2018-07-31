#各規則によって生じる子判断の数
children_num = {
    "P-Zero":0,
    "P-Succ":1,
    "T-Zero":0,
    "T-Succ":2,
    "R-Plus":1,
    "R-Times":1,
    "R-PlusL":1,
    "R-PlusR":1,
    "R-TimesL":1,
    "R-TimesR":1,
    "MR-Zero":0,
    "MR-One":1,
    "MR-Multi":2,
    "DR-Plus":1,
    "DR-Times":1,
    "DR-PlusL":1,
    "DR-PlusR":1,
    "DR-TimesL":1,
    "DR-TimesR":1,
    "E-Int":0,
    "E-Bool":0,
    "E-IfT":2,
    "E-IfF":2,
    "E-Plus":3,
    "E-Minus":3,
    "E-Times":3,
    "E-Lt":3,
    "B-Plus":0,
    "B-Minus":0,
    "B-Times":0,
    "B-Lt":0,
    #EvalML1Err
    "E-IfInt":1,
    "E-PlusBoolL":1,
    "E-PlusBoolR":1,
    "E-MinusBoolL":1,
    "E-MinusBoolR":1,
    "E-TimesBoolL":1,
    "E-TimesBoolR":1,
    "E-LtBoolL":1,
    "E-LtBoolR":1,
    "E-IfError":1,
    "E-IfTError":2,
    "E-IfFError":2,
    "E-PlusErrorL":1,
    "E-PlusErrorR":1,
    "E-MinusErrorL":1,
    "E-MinusErrorR":1,
    "E-TimesErrorL":1,
    "E-TimesErrorR":1,
    "E-LtErrorL":1,
    "E-LrErrorR":1,
    #EvalML2
    "E-Var1":0,
    "E-Var2":1,
    "E-Let":2,
    #EvalML3
    "E-Fun":0,
    "E-App":3,
    "E-LetRec":1,
    "E-AppRec":3,
}
#判断クラス
class Judgement():
    def __init__(self,judgement,my_id=0,rule=None):
        #この判断を導いた規則
        self.rule = rule
        self.str = judgement
        self.id = my_id 
        #直下の子の判断のid
        self.childs_id = list()

#1.self.pointerを表示する
#2.self.pointerを導く規則を入力させる（子判断の数だけ入力を受け付ける）
#3.子判断を入力させ，それらにidをつけ，self.pointerの判断の
#文字列を生成してそれにidを埋め込む
#4.
class Interpreter():
    def __init__(self,judgement):
        #今対象としている判断
        self.pointer = judgement
        #子判断をスタックする
        self.childs = list()
        #最終的な出力結果となる文字列
        self.string = "@0"
        #子判断のidをつけるときのもの
        self.c_id = judgement.id
        #ヒストリ
        self.history = list()

    def test(self):
        while(1):
            i = input()
            print(i)

    def run(self):
        print("対象：{}".format(self.pointer.str))
        jud = self.pointer.str
        j_id = self.pointer.id
        print("規則を教えて？")
        rule = input()
        while(1):
            try:
                num = int(children_num[rule])
                break
            except KeyError:
                print("そんな規則はございません")
                print("規則を教えて？")
                rule = input()
        jud += " by {} ".format(rule) + "{\n"
        if num!=0:
            for i in range(num):
                print("判断{}を教えて？".format(i))
                self.c_id += 1
                self.childs.append(Judgement(input(),self.c_id,rule))
                jud += "@" + str(self.c_id) + ";"
        jud += "}"

        self.string = self.string.replace("@"+str(j_id),jud)
        print("経過：{}".format(self.string))
        if self.childs==[]:
            return 
        self.pointer = self.childs.pop()
        self.run()


