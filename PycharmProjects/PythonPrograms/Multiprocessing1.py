import multiprocessing

def calSquare(numbers,result,v):
    v.value = 5.67
    for idx, n in enumerate(numbers):
        result[idx] = n*n

if __name__ == "__main__":
    numbers = [1,2,3]
    result = multiprocessing.Array('i',3)
    v = multiprocessing.Value('d',0.0)
    p = multiprocessing.Process(target=calSquare,args=(numbers,result,v))
    p.start()
    p.join()

    print(result[:])
    print(v.value)