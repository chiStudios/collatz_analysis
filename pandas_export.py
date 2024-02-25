from sys import setrecursionlimit
from pandas import DataFrame

def run_collatz(x, tests=1): # run the conjecture in a loop

    setrecursionlimit(10000)
    raw_data = []
    export_data = []


    def collatz(x, iterations=0):
        if iterations > 9993: # prevents error when stack is abt to overflow
            print(f'{x} exceeded recursion depth of 10000')
            exit()
        elif x == 1: # ends the recursion, returns the score (how many steps)
            raw_data.append(x)
            return iterations
        elif x % 2 == 0: # if even, divide by 2
            raw_data.append(x)
            return collatz(x // 2, iterations + 1)
        else: # if odd, multiply by 3 and add 1
            raw_data.append(x)
            return collatz(3 * x + 1, iterations + 1)


    for i in range(tests): # test loop
        iterations = collatz(x) # runs the conjecture recursion function
        export_data.append([x, iterations, raw_data.copy()])
        raw_data.clear() # refresh for next integer to test
        x += 1 # move to next integer to test
    
    df = DataFrame(export_data)
    df.columns = ['Integer', 'Iterations', 'Raw Data']
    return df
    
print(run_collatz(7, 3)) # run the test loop
