
def progress_bar(progress,message):
    print("\r{0}:[{1}] {2}%".format(message,"#"*(progress/10),'percent'))