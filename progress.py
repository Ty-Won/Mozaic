import sys
from time import sleep

def progress_bar(progress,message):
    sys.stdout.write("\r{0}:[ {1} ]%".format(message,"#"*int((progress/5))))
    sys.stdout.flush()