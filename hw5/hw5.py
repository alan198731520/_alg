import multiprocessing

# 測試 halt 函數
def target(queue, f, input):
    try:
        queue.put(f(*input))
    except Exception as e:
        queue.put(None)

def halt(f, input, timeout=5):  
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=target, args=(queue, f, input))
    process.start()
    process.join(timeout=timeout)  

    if process.is_alive():
        process.terminate()
        return False  
    else:
        result = queue.get()
        return result is not None

def f1(n):
    return n * n

def f2(n):
    s = 0
    for _ in range(n):
        for _ in range(n):
            for _ in range(n):
                for _ in range(n):
                    s = s + 1

if __name__ == "__main__":
    print('halt(f1, [3]) =', halt(f1, [3]))   
    print('halt(f2, [10]) =', halt(f2, [10], timeout=5)) 
    print('halt(f2, [1000]) =', halt(f2, [1000], timeout=10)) 