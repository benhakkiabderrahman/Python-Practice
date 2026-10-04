import utils
ips = utils.read_targets("targets.txt")
if ips:
    print("Targets loaded successfully:")
    print(ips)