# with open('input.txt') as f:
#     contents = f.readlines()

INP = [l.strip() for l in open('input.txt')]
quantity = []
for elf in ('\n'.join(INP).split('\n\n')):
    res = 0
    for x in elf.split('\n'):
        res += int(x)
    quantity.append(res)

print(max(quantity))