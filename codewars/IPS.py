def ips_between(start, end):
    start = [int(x) for x in start.split(".")]
    start = sum(((x*(256**(i+1))) for i, x in enumerate(start[2::-1])), start[3])
    end = [int(x) for x in end.split(".")]
    end = sum(((x*(256**(i+1))) for i, x in enumerate(end[2::-1])), end[3])
    return end - start

print(ips_between("31.136.231.34", "255.255.255.255"))

3765901533