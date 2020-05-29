# github repository- Lavanya-B

def find(s, letter):
    res=[i for i, c in enumerate(s) if c==letter]
    return len(res), res

for s, l in [("Hello how are you", "e")]:
    print(s)
    print(l)
    le, pos=find(s, l)
    print("Occurs", le, "times.")
    print("Positions:", pos)
    print()