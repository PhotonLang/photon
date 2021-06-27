from photon.helpers import read_lark_file, TimerHelper
from lark import Lark

grammar = read_lark_file("photon/syntax/grammar.lark")

parser = Lark(grammar)
timer = TimerHelper()

text = """
OPEN 'image.png' AS image
APPLY 'solarize' TO image
SAVE image 'output.png'
"""
timer.start()
parser_output = parser.parse(text)
timer.end()
print(timer.time() * 1000)
print(parser_output)
print(parser_output.pretty())