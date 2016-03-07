import os
import subprocess

STAN_DIR = "C:/Users/louis/Desktop/cmdstan-2.9.0/cmdstan-2.9.0"

make_cmd = """make C:/Users/louis/Desktop/Code/stan_tests/models/bernoulli/bernoulli.exe"""
run_cmd = "bernoulli.exe sample data file=bernoulli.data.R"

os.chdir(STAN_DIR)
print(os.getcwd())
s = subprocess.check_output(make_cmd, shell=True)
print(s)

# TODO:
# Make vs run
# Logging for output