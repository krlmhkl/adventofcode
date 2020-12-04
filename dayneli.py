str = ""

batches = [value.strip() for value in f.read().split("\n\n")]




passport = dict([el.split(":") for el in str])