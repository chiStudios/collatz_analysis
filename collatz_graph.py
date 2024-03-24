import matplotlib.pyplot as plt
from time import time
from sys import setrecursionlimit
setrecursionlimit(10_000)

class cg():
    def __init__(self):
        self.global_cache = {}

    def collatz(self, x, seq_len=0):
        if x in self.global_cache.keys():  
            return seq_len + self.global_cache[x]
        elif x == 1: # ends the recursion, returns the score (how many steps)
            return seq_len
        elif x % 2 == 0: # if even, divide by 2
            x //= 2
        else: # if odd, multiply by 3 and add 1
            x = x * 3 + 1
        seq_len += 1

        return self.collatz(x, seq_len)

    def run_collatz(self, x, rng, cache): # run the conjecture in a loop
        y_points = []
        # paths = 0 # TODO: unique pathfinder

        for x in range(x, rng):
            seq_len = self.collatz(x)
            y_points.append(seq_len) # conjecture recursion function
            if not x in cache.keys(): self.global_cache[x] = seq_len

        return y_points

    def plot_collatz(self, start, stop, display=True, save=False):
        print(f'Running calculations for {start:,} through {stop:,}...')
        start_time = time()
        y_points = self.run_collatz(start, stop, self.global_cache)
        secs = time() - start_time # keep track of calculation time
        x_points = [x for x in range(start, stop)]
        print(f'Took {secs:.2f} seconds...')

        print('Dumping cache...')
        self.global_cache.clear() # sweet relief

        print('Plotting coordinates...')
        plt.plot(x_points, y_points, marker=',', linestyle='')
        plt.xlabel('Loop Start Value') # set X axis label on graph
        plt.ylabel('Loop Range') # set Y axis label on graph
        plt.title(f'Collatz Conjecture [{start:,}, {stop:,}] | Calculations took {secs:.1f} secs')

        if save:
            print('Saving plot to image...')
            plt.savefig(f'Collatz_Array_{start}_{stop}_{secs:.0f}secs.png') # save graph to png

        if display:
            print('Displaying plot...')
            plt.show() # show graph in gui

    def plot_seq_freq(self, start, stop, display=True, save=False):
        print(f'Running Calculations for {start:,} through {stop:,}...')
        start_time = time()
        seq_len_list = self.run_collatz(start, stop, self.global_cache)
        secs = time() - start_time # keep track of calculation time
        print(f'Took {secs:.2f} seconds...')

        print('Dumping cache...')
        self.global_cache.clear() # sweet relief

        print('Parsing data...')
        data = {}
        for seq_len in seq_len_list:
            if seq_len in data:
                data[seq_len] += 1
            else:
                data[seq_len] = 1

        print('Sorting data and dumping local cache...')
        data = sorted(list(data.items())) # convert dict(data) to sorted list of dict(data) contents
        x_points = [float(t[0]) for t in data] # parse nested tuples for value in index 0
        y_points = [float(t[1]) for t in data] # parse nested tuples for value in index 1
        data = [] # dump old data for memory optimization

        print('Plotting coordinates...')
        plt.plot(x_points, y_points, marker='.', markersize=1, linestyle='')
        plt.xlabel('Sequence Length') # set X axis label on graph
        plt.ylabel('Frequency') # set Y axis label on graph
        plt.title(f'Collatz Conjecture | Sequence Length Analysis [{start:,}, {stop:,}] | Calculations took {secs:.1f} secs')

        if save:
            print('Saving plot to image...')
            plt.savefig(f'Collatz_Array_SFA_{start}_{stop}_{secs:.0f}secs.png') # save graph to png

        if display:
            print('Displaying plot...')
            plt.show() # show graph in gui

while True:
    start = int(input('Start Value: ').replace(',', ''))
    stop = int(input('Stop Value: ').replace(',', ''))
    choice = input('Choose Plot Type:\n\t'
                   '[c] Original Collatz Conjecture\n\t'
                   '[s] Sequence Frequency Analysis\n').lower()
    
    # wider gap between values leads to larger memory usage
    if choice == 'c': cg().plot_collatz(start, stop, display=True, save=False)

    elif choice == 's': cg().plot_seq_freq(start, stop, display=True, save=False)

    elif choice in ('e', 'exit', 'quit'): break
    else: print('Invalid entry...')
