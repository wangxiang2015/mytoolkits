"""
Get processes's pids including contents in grep_str.
-----------------

python get_pids.py --grep_str evsjtu,envs/wangpy11,joblib,process-name

grep_str 逗号分割，不能有空格。

"""

import argparse
import subprocess
import subprocess as sp
import re
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Get processes's pids including contents in grep_str.")
    parser.add_argument('--grep_str', type=str, help='')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    grep_str = args.grep_str
    assert grep_str is not None, f"Error: Argument (grep_str) is required."
    assert isinstance(grep_str, str), f"Error: Argument (grep_str) should be a string list."
    ps_cmd = f"ps aux"
    for i in [_.strip() for _ in grep_str.split(',')]:
        ps_cmd += f" | grep {i}"
    print(f"{ps_cmd}")

    ps_out = subprocess.getoutput(ps_cmd).split('\n')
    ps_ids = list()
    for line in ps_out:
        if 'get_pids.py' in line or 'ps aux' in line:
            continue
        tmp = [_.strip() for _ in line.split(' ') if _.strip()]
        ps_ids.append(tmp[1])
    killed_ps_str = ' '.join(ps_ids)
    print(f"PIDs (num: {len(ps_ids)}): {killed_ps_str}")


if __name__=='__main__':
    main()

