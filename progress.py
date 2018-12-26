import sys
from time import sleep

def progress_bar(current_val, total_val ,message):
    completion_rate = int(10*(current_val/total_val))
    sys.stdout.write("\r{0}:[ {1} ]".format(message,"#"*completion_rate))
    sys.stdout.flush()