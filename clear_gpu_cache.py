"""
Clear cache on the given GPU-ID by killing processes' PID
-----------------
How to use?

python clear_gpu_cache.py 1
或
python clear_gpu_cache.py --gpu_id 1

"""

import argparse
import subprocess
import subprocess as sp
import re
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Clear cache on the given GPU-ID by killing processes' PID")
    parser.add_argument('--gpu_id', type=int, help='gpu id')
    args = parser.parse_args()
    return args

def main():
    gpu_id:int = -1
    if len(sys.argv)==2:
        gpu_id = int(sys.argv[1])
    elif len(sys.argv) ==3:
        args = parse_args()
        gpu_id = int(args.gpu_id)
    else:
        raise Exception("Error: argument number not correct.")
    
    get_processes_on_gpu_cmd = f'fuser -v /dev/nvidia*'
    cmd = get_processes_on_gpu_cmd
    out_info = subprocess.getoutput(cmd)

    pid = ''
    for line in out_info.split('\n'):
        if f'/dev/nvidia{gpu_id}' in line:
            pid = re.split(r'\s+', line)[2]
    
    if pid!='':
        print(f"killing PID: {pid} on GPU-{gpu_id} ...")
        out_info = subprocess.run(f'kill -9 {pid}', shell=True)
        print(f"--- Done! ---")
    else:
        print(f"No process running on GPU-{gpu_id}")


if __name__=='__main__':
    main()

