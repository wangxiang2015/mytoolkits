"""
Clear cache on the given GPU-ID by killing processes' PID
"""

import subprocess
import subprocess as sp
import re

gpu_id = 1

get_processes_on_gpu_cmd = f'fuser -v /dev/nvidia*'
cmd = get_processes_on_gpu_cmd
out_info = subprocess.getoutput(cmd)

res = ''
for line in out_info.split('\n'):
    if f'/dev/nvidia{gpu_id}' in line:
        res = re.split(r'\s+', line)[2]
print(f"killing PID: {res}")

out_info = subprocess.run(f'kill -9 {res}', shell=True)

