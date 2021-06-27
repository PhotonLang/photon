from lark import Lark
from photon.helpers import TimerHelper
timer = TimerHelper()
json_parser = Lark(r"""
    value: dict
         | list
         | ESCAPED_STRING
         | SIGNED_NUMBER
         | "true" | "false" | "null"

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : ESCAPED_STRING ":" value

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='value')



text = '{"key": ["item0", "item1", 3.14]}'
timer.start()
output = json_parser.parse(text)
timer.end()
print(output)
print(timer.time() * 1000)