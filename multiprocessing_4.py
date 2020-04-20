
'''
Variation pathos, local method

Windows OS: Hangs/ multiprocess error with newer version of pathos
Mac OS:
Linux:
Debian (unclear because windows app but operated in same manner)

Cloud-based:
Repl.it: Works
Ideone.com: Fails-multiprocess error
'''


from multiprocess import freeze_support
from pathos.multiprocessing import ProcessPool

def f(vars):
    return vars[0]**vars[1]


if __name__ == "__main__":
    freeze_support()

    pool = ProcessPool(4)

    print(list(pool.imap(f, [(1, 5), (2, 8), (3, 9)])))