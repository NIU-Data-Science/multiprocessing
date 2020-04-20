'''
Variation pathos, local method, iterated imap

Windows OS: Hangs/ multiprocess error with newer version of pathos
Mac OS:
Linux:
Debian Hangs

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
    print("start")
    for run in pool.imap(f, [(1, 5), (2, 8), (3, 9)]):
        print(run)