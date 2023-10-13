'''
数学公式编辑器
'''

from os import system
from sys import argv

from lexer import lexer
from parcer import parser
from const import add_ops, add_ids

def interactive():
    while True:
        try:
            parser(lexer(input()))
        except (EOFError, KeyboardInterrupt):
            break
        except Exception:
            pass

def compilation():
    for file in argv[1:]:
        with open(file, 'r') as f:
            words = ""
            for line in f:
                line = line.strip()
                if line.startswith('::'):
                    continue
                if line.startswith(':op:'):
                    add_ops(line[4:])
                elif line.startswith(':id:'):
                    add_ids(line[4:])
                if line != "":
                    words += line
                else:
                    parser(lexer(words))
                    words = ""
            parser(lexer(words))
                

def main():
    if len(argv) > 1:
        compilation()
    else:
        interactive()


if __name__ == '__main__':
    main()
    input()
