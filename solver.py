from derivation_system import * 
import argparse

def main():
    parser = argparse.ArgumentParser(description='program-semantics solver')↲
    parser.add_argument('--system', '-s', default='Nat',↲
                       help='derivation_system')↲
    parser.add_argument('--judgement', '-j',↲
                       help='derivation_system')↲
    parser.add_argument('--out', '-o', default='results/',↲
                       help='Directory to output the result')↲                                                                             
    args = parser.parse_args()

if __name__=="__main__":
    #  jud = Judgement("Z plus S(S(Z)) is S(S(Z))")
    #  jud = Judgement("S(S(Z)) plus Z is S(S(Z))")
    #  jud = Judgement("S(Z) plus S(S(S(Z))) is S(S(S(S(Z))))")
    jud = Judgement("S(S(Z)) times S(S(Z)) is S(S(S(S(Z))))")
    s = Nat(jud)
    rule, child = s.gen()
    print(rule)
    for i in range(len(child)):
        print(child[i].judge)
        print(child[i].id)
        print(child[i].parent)



