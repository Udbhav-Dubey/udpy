filter_nums=lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():",filter_nums("Geeks101"))

do_exclaim = lambda s: s + '!'
print("do_exclaim(): ",do_exclaim("i am tired"))

find_sum= lambda n : sum([int(x) for x in str(n)])
print("find_sum(): ",find_sum(101))

