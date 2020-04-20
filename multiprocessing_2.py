'''
Variation no pathos, local method
Assessed to be the most resilient

Windows OS: works
Mac OS:
Linux:
Debian works

Cloud-based:
Repl.it: Works
Ideone.com: Works
'''


from multiprocessing import freeze_support
from multiprocessing import Pool


def f(vars):
    return vars[0]**vars[1]


if __name__ == "__main__":
    freeze_support()

    pool = Pool(4)

    for run in pool.imap(f, [(1,5), (2,8), (3,9)]):
        print(run)