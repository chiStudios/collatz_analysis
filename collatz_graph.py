import matplotlib.pyplot as plt
import time
from sys import setrecursionlimit
setrecursionlimit(10_000)

class cg():
    def __init__(self):
        self.global_cache = {}

    def collatz(self, x, step=0):
        if x in self.global_cache.keys():  
            return step + self.global_cache[x]
        elif x == 1: # ends the recursion, returns the score (how many steps)
            return step
        elif x % 2 == 0: # if even, divide by 2
            x //= 2
        else: # if odd, multiply by 3 and add 1
            x = x * 3 + 1
        step += 1

        return self.collatz(x, step)

    def run_collatz(self, x, rng, cache): # run the conjecture in a loop
        # paths = 0 # TODO: unique pathfinder
        y_points = []

        for x in range(x, rng):
            step = self.collatz(x)
            y_points.append(step) # conjecture recursion function
            if not x in cache.keys(): self.global_cache[x] = step

        return y_points

    def plot_points(self, start_val, stop_val):
        print(f'Running calculations for {start_val:,} through {stop_val:,}...')
        start_time = time.time()
        y_points = self.run_collatz(start_val, stop_val, self.global_cache)
        calc_time = time.time() - start_time
        x_points = [x for x in range(start_val, stop_val)]
        print(f'Took {calc_time:.2f} seconds...')

        print('Dumping cache...')
        self.global_cache.clear()

        print('Plotting coordinates...')
        plt.plot(x_points, y_points, marker=',', linestyle='')
        plt.xlabel('Loop Start Value') # set X axis label on graph
        plt.ylabel('Loop Range') # set Y axis label on graph
        plt.title(f'Collatz Conjecture | Plotting {start_val:,} to {stop_val:,} | Calculations took {calc_time:.1f} secs')

        print('Saving plot to image...')
        plt.savefig(f'Collatz_Array_{start_val}_{stop_val}_{calc_time:.0f}secs.png') # save graph to png

        print('Displaying plot...')
        plt.show() # show graph in gui

cg().plot_points(1, 10_000_000) # for stable execution do not exceed a 1,000,000 unit gap
