FUNCS = {
    'msup'    : ('<msup><mrow>',                '</mrow></msup>'),
    'msub'    : ('<msub><mrow>',                '</mrow></msub>'),
    'msubsup' : ('<msubsup><mrow>',             '</mrow></msubsup>'),
    'mfrac'   : ('<mfrac><mrow>',               '</mrow></mfrac>'),
    'mroot'   : ('<mroot><mrow>',               '</mrow></mroot>'),
    'msqrt'   : ('<msqrt><mrow>',               '</mrow></msqrt>'),
    'mspace'  : ('<mspace>',                    '</mspace>'),
    'log'     : ('<msub><mi>log</mi><mrow>',    '</mrow></msub>'),
    'int'     : ('<msubsup><mo>∫</mo><mrow>',   '</mrow></msubsup>'),
    'sigma'   : ('<munderover><mo>∑</mo><mrow>','</mrow></munderover>')
}
IDS = {
    'PI'     : 'π',
    'INFIN'  : "∞",
    'INT'    : "∫",
    'ALPHA'  : "α",
    'BETA'   : "β",
    'GAMMA'  : "γ",
    'DELTA'  : "Δ",
    'THETA'  : "θ",
    'LAMBDA' : "λ",
}

OPS = {
    '*'    : '×',
    '/'    : '÷',
    '+-'   : "±",
    '!='   : "≠",
    '>='   : "≥",
    '<='   : "≤",
    '<->'  : "⟺",
}

def add_ids(filename):
    global IDS
    pass

def add_ops(filename):
    global OPS
    pass