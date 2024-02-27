import pandas as pd
from sys import setrecursionlimit

def run_collatz(x, tests=1): # run the conjecture in a loop
    setrecursionlimit(10000)
    raw_data = []
    export_data = []
    print(f'Running Collatz Conjecture {tests} time(s) starting with {x}\n')


    def collatz(x, iterations=0):
        if iterations > 9993: # prevents error when stack is abt to overflow
            print(f'{x} exceeded recursion depth of 10000')
            exit()
        elif x == 1 or x == 0: # ends the recursion, returns the score (how many steps)
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
        
    df = pd.DataFrame(export_data, columns=['Integer', 'Iterations', 'Raw Data'])
    # df.set_index('Integer', inplace=True)
    return df

def test_loop():
    # run the test loop
    collatz = run_collatz(0, 100000).sort_values('Iterations', ascending=True)
    integer_last_value = []
    last_val_freq = {}
    
    for item in collatz['Integer']:
        item = str(item)[-1]
        print(item, end='')
        print()
        integer_last_value.append(item)
        if item in last_val_freq:
            last_val_freq[item] += 1
        else:
            last_val_freq[item] = 1
    
    # df_ilv = pd.DataFrame(integer_last_value, columns=['Last Value']).set_index('Last Value')
    # df_ilv.to_csv('integer_last_value.csv')

    # print(collatz)
    # collatz.to_csv('collatz.csv')

    return last_val_freq

    

print(test_loop())

