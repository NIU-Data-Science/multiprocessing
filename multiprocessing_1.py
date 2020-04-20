'''
Variation uses pathos dependency

Windows OS: Hangs
Mac OS:
Linux:
Debian (unclear because windows app but operated in same manner)

Cloud-based:
Repl.it: Works
Ideone.com: Fails-multiprocess error
'''


from multiprocess import freeze_support
from pathos.multiprocessing import ProcessPool

if __name__ == "__main__":
    freeze_support()

    pool = ProcessPool(nodes=4)
    results = pool.uimap(pow, [1,2,3,4], [5,6,7,8])
    print("...")
    print(list(results))