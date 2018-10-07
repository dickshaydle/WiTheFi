#!/usr/bin/python3
"""HackRF Power Meter."""

import subprocess


cmdline = ['/usr/local/bin/hackrf_sweep', '-f', '2435:2440', '-w', '5000000']
process = subprocess.Popen(cmdline, stdout=subprocess.PIPE, universal_newlines=False)

power_sum = 0

while True:
    line = process.stdout.readline()
    vars = line.decode('utf8').split(',')
    freq = int(vars[2])
    power_sum += float(vars[-1])

    if freq == 2435000000:
        power = power_sum / 4
        power_sum = 0
        print(round(power, 2))
