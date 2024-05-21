import torch.multiprocessing as mp

def square_number(q, n):
    q.put(n * n)

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    q = mp.Queue()
    processes = []
    
    for number in numbers:
        p = mp.Process(target=square_number, args=(q, number))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    results = [q.get() for _ in numbers]
    print(results)  # [1, 4, 9, 16, 25]