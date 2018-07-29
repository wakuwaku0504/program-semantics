#! /usr/bin/python
import argparse
from derivation_system import * 

def main():
    parser = argparse.ArgumentParser(description='program-semantics solver')
    parser.add_argument('--system', '-s', default='Nat',
                       help='derivation_system')
    parser.add_argument('--judgement', '-j',
                       help='derivation_system')
    parser.add_argument('--out', '-o', default='results/',
                       help='Directory to output the result')                                                                             
    args = parser.parse_args()

    root_judgement = Judgement(args.judgement)

    if args.system=="Nat":
        system = Nat(root_judgement)
    
    child = system.gen()
    while(1):



    #  childs = list()
    #  while(1):
        #  rule, child = system.gen()
        #  print(
        #  while(1):

    child = system.gen()
    for i in range(len(child)):
        print(child[i].judge)
        print(child[i].id)
        print(child[i].parent)
        print(child[i].rule)


if __name__=="__main__":
    main()
    #  jud = Judgement("Z plus S(S(Z)) is S(S(Z))")
    #  jud = Judgement("S(S(Z)) plus Z is S(S(Z))")
    #  jud = Judgement("S(Z) plus S(S(S(Z))) is S(S(S(S(Z))))")
    

