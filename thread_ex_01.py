import threading
import queue,time

def thread1(a,q1):
    time.sleep(2)
    ret = [a,1]
    q1.put(ret)

def thread2(a,q2):
    time.sleep(1)
    ret = [a,2]
    q2.put(ret)

i1=1;i2=1
q1 =queue.Queue()  # queue which stores a result of a thread
q2 =queue.Queue()  # queue which stores a result of a thread
th1 = threading.Thread(target=thread1, args=(i1,q1),daemon=True)
th1.start()
th2 = threading.Thread(target=thread2, args=(i2,q2),daemon=True)
th2.start()
#th.join()
while True:
  if i1<=5 and th1.is_alive()==False:
    result = q1.get()
    print("thread: "+str(i1)+" "+str(result))
    i1=i1+1
    if i1<=5: 
      th1 = threading.Thread(target=thread1, args=(i1,q1),daemon=True)
      th1.start()
  if i2<=5 and th2.is_alive()==False:
    result = q2.get()
    print("thread: "+str(i2)+" "+str(result))
    i2=i2+1
    if i2<=5: 
      th2 = threading.Thread(target=thread2, args=(i2,q2),daemon=True)
      th2.start()
  print(i1);print(i2)
  if i1>5 and i2>5:
    break
  time.sleep(1)  #do other tasks

exit()
