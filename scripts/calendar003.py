#!/usr/bin/python3

import sys
import time

def main(argv,start,end):
    x = argv + '\t' + start + '\t' + end
    print('call',argv,start,end,x)
    f = open('output.log', 'a+')
  #  with open('output.log','wb') as f:
    line = f.write(x + "\n")
    print('line',line)
    f.close()

if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    start_time= time.strftime('%Y-%m-%dT%H:%M:%S-07:00', time.localtime(int(sys.argv[1])))
    end_time = time.strftime('%Y-%m-%dT%H:%M:%S-07:00', time.localtime(int(sys.argv[2])))
    print(sys.argv[0],start_time,end_time)

    main(str(sys.argv[0]),str(start_time),str(end_time))
