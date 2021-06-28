from photon.helpers import read_lark_file, TimerHelper
from lark import Lark, Transformer, Token
from photon.transformer import PhotonTransformer
from photon.prelude import Env

grammar = read_lark_file("photon/syntax/grammar.lark")

parser = Lark(grammar)
timer = TimerHelper()

text = """
OPEN './tests/image.jpg' AS image
APPLY 'solarize' TO image
SAVE image TOSYS 'output.png'
"""
timer.start()
parser_output = parser.parse(text)
timer.end()
print(timer.time() * 1000)
"""print(parser_output)
print(parser_output.pretty())
print(dir(parser_output))
for x in parser_output.scan_values(lambda v: isinstance(v, Token)):
    print(x)"""
print(PhotonTransformer(Env()).transform(parser_output))