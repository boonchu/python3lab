#! /usr/bin/env python
#
# https://github.com/agronholm/pythonfutures/blob/master/test_futures.py
#

import sys
import os
import re
import subprocess


def executor(*args, **env_vars):
    cmd_line = [sys.executable]
    if not env_vars:
        cmd_line.append('-E')
    env = os.environ.copy()
    if env_vars.pop('__cleanenv', None):
        env = {}
    env.update(env_vars)
    cmd_line.extend(args)
    p = subprocess.Popen(cmd_line, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=env)
    try:
        out, err = p.communicate()
    finally:
        subprocess._cleanup()
        p.stdout.close()
        p.stderr.close()
    rc  = p.returncode
    return rc, out, re.sub(r"\[\d+ refs\]\r?\n?$".encode(), "".encode(), err).strip()


if __name__ == "__main__":
    """ assertion testing """
    rc, out, err = executor('-c', """if 1:
            from concurrent.futures import %s
            import time
            import sys

            def sleep_and_print(t, msg):
                time.sleep(t)
                print(msg)
                sys.stdout.flush()

            with %s(max_workers=5) as executor:
                t = executor.submit(sleep_and_print, 1.0, "apple")
            """ % ('ProcessPoolExecutor', 'ProcessPoolExecutor'))

    print " return code ", rc
    print " output [%s]"%out
    print " error ", err
