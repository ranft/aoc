import re
import sys

pattern=re.compile(r"(mul)\(([0-9]+),([0-9]+)\)|(don't\(\))|(do\(\))")

total=0
active=True
for p in pattern.findall(sys.stdin.read()):
    match p:
        case ("mul", a, b, "", ""):
            if active:
                total += int(a)*int(b)
        case ('', '', '', "don't()", ''):
            active = False
        case ('', '', '', '', 'do()'):
            active = True
        case other:
            raise ValueError(str(p))

print(total)
