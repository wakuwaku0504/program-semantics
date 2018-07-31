#! /usr/bin/python3
import argparse
from derivation_system import * 
from interpreter import *

def main():
    parser = argparse.ArgumentParser(description='program-semantics solver')
    parser.add_argument('--system', '-s', default='Nat',
                       help='derivation_system')
    parser.add_argument('--name', '-n', 
                       help='save name')
    parser.add_argument('--judgement', '-j',
                       help='root judgement')
    parser.add_argument('--out', '-o', default='answer/',
                       help='Directory to output the result')
    parser.add_argument('--inter', '-i', default=1,
                        help='1:interpreter')
    args = parser.parse_args()

    root_judgement = Judgement(args.judgement)

    if args.system=="Nat":
        system = Nat(root_judgement)


    #対話的
    if args.inter==1:
        inter = Interpreter(root_judgement)

        inter.test()
        #  inter.run()
        #  savepath = args.out + args.name 
        #  f = open(savepath,'w')
        #  f.write(inter.string)
        #  f.close


    #全自動
    else:
        system.run()
        print(system.string)
        savepath = args.out + args.name 
        f = open(savepath,'w')
        f.write(system.string)
        f.close


if __name__=="__main__":
    main()
    

