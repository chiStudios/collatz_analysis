raw_data = []
def collatz(x, step=0):
    if step > 4993: # prevents error when stack is abt to overflow
        print(f'{x} exceeded recursion depth of 5000')
        exit()
    elif x == 1: # ends the recursion, returns the score (how many steps)
        return step, raw_data
    elif x % 2 == 0: # if even, divide by 2
        raw_data.append(x)
        return collatz(x // 2, step + 1)
    else: # if odd, multiply by 3 and add 1
        raw_data.append(x)
        return collatz(3 * x + 1, step + 1)

def run_collatz(x): # run the conjecture in a loop
    from sys import setrecursionlimit
    setrecursionlimit(10000)
    for i in range(3): # infinite loop to continuously test
        steps, raw = collatz(x) # runs the conjecture recursion function]
        output = [x, steps, raw]
        print(output)
        output.clear()
        raw_data.clear()
        x += 1 # move to next integer to test
        
    
# print(collatz(10000000))
run_collatz(100000000) # run the infinite test loop
# x: steps
