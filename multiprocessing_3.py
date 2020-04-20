'''
Variation no pathos, local method but with list
Assessed to be the most resilient

Windows OS: works
Mac OS:
Linux:
Debian thru Windows: Works

Cloud-based:
Repl.it: Works
Ideone.com: Works
'''


from multiprocessing import freeze_support
from multiprocessing import Pool


def f(vars):
    return vars[0] ** vars[1]


if __name__ == "__main__":
    freeze_support()

    pool = Pool(4)

    print(list(pool.imap(f, [(1, 5), (2, 8), (3, 9)])))