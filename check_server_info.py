"""
Check server/PC info: num_cpu, num_cores, OS_version, memory size, disk volume.
-----------------

python check_server_info.py

"""

import argparse
import subprocess
import subprocess as sp
import re
import sys


def get_num_cpu():
    cmd = f'cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l'
    res = subprocess.getoutput(cmd)
    
    return res

def get_num_cores_for_each_cpu():
    cmd = f'cat /proc/cpuinfo| grep "cpu cores"| uniq'
    res = subprocess.getoutput(cmd)
    res = res.strip().split(' ')[-1]
    
    return res

def get_linux_info():
    cmd = f'uname -a'
    res = subprocess.getoutput(cmd)
    res = res.split('#')[0].strip()

    return res

def get_os_info():
    cmd = f'lsb_release -a'
    cmdout = subprocess.getoutput(cmd).split('\n')
    res1 = ''
    res2 = ''
    for line in cmdout:
        if 'Description' in line:
            res1 = line.strip().split(':')[-1].strip()
        if 'Codename' in line:
            res2 = line.strip().split(':')[-1].strip()
    res = f"{res1}, {res2}"

    return res

def get_memory_info():
    cmd = f'free -mh'
    cmdout = subprocess.getoutput(cmd).split('\n')
    res = cmdout[1].split('        ')
    res = f"total: {res[1].strip()}, used: {res[2].strip()}, free: {res[3].strip()}"

    return res

def get_disk_info():
    cmd = f"sudo fdisk -l | grep 'Disk /dev/sd'"
    cmdout = subprocess.getoutput(cmd).split('\n')
    res = ''
    for line in cmdout:
        res += f"   {line.strip().split(',')[0]}\n"

    return res


def main():
    print(f"""1. [\033[31mnum_cpu\033[0m]: {get_num_cpu()}\n2. [\033[31mcpu_cores\033[0m]: {get_num_cores_for_each_cpu()}\n3. [\033[31mos_info\033[0m]: {get_os_info()}\n4. [\033[31mlinux_info\033[0m]: {get_linux_info()}\n5. [\033[31mmemory_info\033[0m]: {get_memory_info()}\n6. [\033[31mdisk_info\033[0m]: \n{get_disk_info()}""")


if __name__=='__main__':
    main()

