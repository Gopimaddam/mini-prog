
import multiprocessing
import time
import os
def Totalsum(num):
    print(num,multiprocessing.current_process().name,os.getpid())
    res=sum(i for i in range(num))
    return res
  
  
if __name__=="__main__":
    with multiprocessing.Pool(processes=4) as p:
        start=time.time()
        print(p)
        r=p.map(Totalsum,[100000000,1000000000,100000000,100000,1000000,10000000,1000,10000000])
        print(r)
        print(time.time()-start)