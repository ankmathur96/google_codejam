def get_digits(n):
    return [int(c) for c in str(n)]
def combine(n, b):
    a = 0
    for x in get_digits(n):
        a = a * b + x
    return a
def create_possible_multiples():
    all_multiples = []
    iter_range = 2 ** 15
    for a in range(iter_range):
        x = '{0:b}'.format(a)
        x = "".join([c*2 for c in x])
        if len(x) != 30:
            x = (30 - len(x))*'0' + x
        all_multiples.append(int('1' + x + '1'))
    return all_multiples
factor_list = [3, 4, 5, 6, 7, 8, 9, 10, 11]
new_line = ['\n']
if __name__ == '__main__':
    f_stub = 'C-small-attempt0'
    f = open(f_stub + '.in', 'r')
    o = open(f_stub + '.out', 'w')
    n_cases = int(f.readline().strip())
    i = 1
    while i <= n_cases:
        o.write("Case #" + str(i) + ":\n")
        n_j_line = f.readline().split()
        N, J = int(n_j_line[0]), int(n_j_line[1])
        x_const = 10**(N-1) + 1
        all_multiples = create_possible_multiples()
        for multiple in all_multiples:
            is_a_jamcoin = True
            for each_base in range(2,11):
                base_converted = combine(multiple, each_base)
                if base_converted % (each_base+1) != 0:
                    is_a_jamcoin = False
                    break
            if is_a_jamcoin:
                o.write(' '.join([str(i) for i in [multiple] + factor_list] + new_line))
                J = J - 1
            if J == 0:
                break
        i += 1
    f.close()
    o.close()
