from photon.helpers import read_lark_file
from lark import Lark

grammar = read_lark_file("photon/syntax/grammar.lark")

parser = Lark(grammar)

text = "OPEN 'image.png' AS image"
parser_output = parser.parse(text)
print(parser_output)
print(parser_output.pretty())