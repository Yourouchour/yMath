from os import system
from pyperclip import copy
from typing import Tuple

from const import FUNCS, IDS, OPS

class parser:
    '''语法分析'''
    def __init__(self, tokens):
        self.tokens = tokens
        self.funclayer = {}
        self.layer = 0
        self.ans = ["<math xmlns=\"http://www.w3.org/1998/Math/MathML\">"]
        self.parse()

    def parse(self):
        for token in self.tokens:
            if token[0] == 'FN':
                self.fn(token[1])
            elif token[0] == 'MI':
                self.mi(token[1])
            elif token[0] == 'MO':
                self.mo(token[1])
            elif token[0] == 'MN':
                self.mn(token[1])
        self.ans.append("</math>")
        words = "".join(self.ans)
        copy(words)
        print(words, end="\n\n")

    def fn(self, token):
        self.layer += 1
        words = FUNCS.get(token, None)
        if words is None:
            print(f'未定义的函数`{ token }()`，你是想输入`{ token } ()`吗')
            system('pause')
            exit()
        self.ans.append(words[0])
        self.funclayer[self.layer] = words[1]

    def mi(self, token):
        if token.startswith('&'):
            self.ans.append(f'<mi>{ IDS.get(token[1:], token) }</mi>')
        else:
            self.ans.append(f'<mi>{ token }</mi>')

    def mn(self, token):
        self.ans.append(f'<mn>{ token }</mn>')

    def mo(self, token):
        if token == '(':
            self.layer += 1
            self.ans.append('<mo>(</mo>')

        elif token == ')':
            if func:=self.funclayer.get(self.layer, False):
                self.ans.append(func)
                self.funclayer.pop(self.layer)
            else:
                self.ans.append('<mo>)</mo>')
            self.layer -= 1
        elif token == ',':
            if func:=self.funclayer.get(self.layer, False):
                self.ans.append('</mrow><mrow>')
            else:
                self.ans.append('<mo>,</mo>')
        elif token == '^(':
            self._opfunc('<msup>', '</mrow></msup>')
        elif token == '_(':
            self._opfunc('<msub>', '</mrow></msub>')
        else:
            self.ans.append(f'<mo>{OPS.get(token,token)}</mo>')

    def _opfunc(self, start, end):
        self.layer += 1
        self.ans.insert(len(self.ans)-1, start)
        self.ans.append('<mrow>')
        self.funclayer[self.layer] = end