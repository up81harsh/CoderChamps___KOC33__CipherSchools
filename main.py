def fxn(stng):
    # add first letter
    oupt = stng[0]

    # iterate over string
    for i in range(1, len(stng)):
        if stng[i - 1] == ' ':
            # add letter next to space
            oupt += stng[i]

    # uppercase oupt
    oupt = oupt.upper()
    return oupt

inpt1 = "Automated Teller Machines"
print(fxn(inpt1))

inpt1 = "World Health Organization"
print(fxn(inpt1))

inpt1 = "United States"
print(fxn(inpt1))