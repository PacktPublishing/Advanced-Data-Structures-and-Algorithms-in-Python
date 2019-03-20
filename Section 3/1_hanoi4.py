'''
n=3, 3 pegs:
start -> dest
start -> i
dest -> i
start -> dest
i -> start
i -> dest
start -> dest

n=3, 4 pegs:
start, i1
start -> i2
start -> dest
i2 -> dest
i1, dest
'''

def hanoi3(n, peg_start, peg_intermed, peg_dest):
    if n == 1:
        print('{} -> {}'.format(peg_start, peg_dest))
        return

    hanoi3(n - 1, peg_start, peg_dest, peg_intermed)
    print('{} -> {}'.format(peg_start, peg_dest))
    hanoi3(n - 1, peg_intermed, peg_start, peg_dest)

def hanoi4(n, peg_start, peg_intermed1, peg_intermed2, peg_dest):
    if n == 0:
        return
    if n == 1:
        print('{}, {}'.format(peg_start, peg_dest))
        return

    hanoi4(n - 2, peg_start, peg_intermed2, peg_dest, peg_intermed1)
    print('{} -> {}'.format(peg_start, peg_intermed2))
    print('{} -> {}'.format(peg_start, peg_dest))
    print('{} -> {}'.format(peg_intermed2, peg_dest))
    hanoi4(n - 2, peg_intermed1, peg_intermed2, peg_start, peg_dest)

print('n=3, 3 pegs:')
hanoi3(3, 'start', 'i', 'dest')
print('\nn=3, 4 pegs:')
hanoi4(3, 'start', 'i1', 'i2', 'dest')

















