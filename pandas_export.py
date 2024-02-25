
def run_collatz(x): # run the conjecture in a loop

    raw_data = []
    export_data = []

    def collatz(x, steps=0):
        if steps > 9993: # prevents error when stack is abt to overflow
            print(f'{x} exceeded recursion depth of 10000')
            exit()
        elif x == 1: # ends the recursion, returns the score (how many steps)
            raw_data.append(x)
            return steps
        elif x % 2 == 0: # if even, divide by 2
            raw_data.append(x)
            return collatz(x // 2, steps + 1)
        else: # if odd, multiply by 3 and add 1
            raw_data.append(x)
            return collatz(3 * x + 1, steps + 1)
    
    from sys import setrecursionlimit
    from pandas import DataFrame
    setrecursionlimit(10000)

    for i in range(1): # infinite loop to continuously test
        steps = collatz(x) # runs the conjecture recursion function
        export_data.append([x, steps, raw_data.copy()])
        for item in raw_data: raw_data.remove(item)
        x += 1 # move to next integer to test
    
    print('export data:', export_data)
    df = DataFrame(export_data)
    print(df)
    print(df[2][0])
        
    
run_collatz(20) # run the test loop
