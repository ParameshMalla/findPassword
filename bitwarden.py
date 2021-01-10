import subprocess
import itertools

# Runs command in powershell and captures the output
def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

# command to run in powershell and ends the for loop if right combination is found
def pow(hello_command):
    hello_info = run(hello_command)
    bBreak = False
    if(hello_info.returncode!=0):
        hello_info.stdout
    if hello_info.stderr != b'Username or password is incorrect. Try again.':
        print(hello_command)
        print(hello_info.stderr)
        bBreak = True
    else:
        print('Wrong')
    return bBreak

# Changes the character at a given index of a string
def changeCharacter(str,idx,ch):
    str = str[:idx] + ch + str[idx+1:]
    return str

# Finds all the indices of given character in a string
def find(str, ch):
    chIndices = []
    for i, ltr in enumerate(str):
        if ltr == ch:
            chIndices.append(i)
    return chIndices

if __name__ == '__main__':
    hello_command = "bw login youremailid@site.com "
    s = "'yourpossiblepassword'"

    aIndices = find(s,'a')
    iIndices = find(s,'i')
    eIndices = find(s,'e')
    sIndices = find(s,'s')
    p="'yourpossiblepassword'"
    count = 0

    # For loop to get all the given encoding combinations of a password
    for i in range(len(aIndices)+1):
        for subset in itertools.combinations(aIndices,i):
            for chIndex in subset:
                p = changeCharacter(p,chIndex,'@')
            if(subset==()):
                for chIndex in aIndices:
                    p = changeCharacter(p,chIndex,'a')
            for j in range(len(iIndices)+1):
                for subset in itertools.combinations(iIndices,j):
                    for chIndex in subset:
                        p = changeCharacter(p,chIndex,'1')
                    if(subset==()):
                        for chIndex in iIndices:
                            p = changeCharacter(p,chIndex,'i')
                    for k in range(len(eIndices)+1):
                        for subset in itertools.combinations(eIndices,k):
                            for chIndex in subset:
                                p = changeCharacter(p,chIndex,'3')
                            if(subset==()):
                                for chIndex in eIndices:
                                    p = changeCharacter(p,chIndex,'e')
                            for l in range(len(sIndices)+1):
                                for subset in itertools.combinations(sIndices,l):
                                    for chIndex in subset:
                                        p = changeCharacter(p,chIndex,'$')
                                    if(subset==()):
                                        for chIndex in sIndices:
                                            p = changeCharacter(p,chIndex,'s') 
                                    print(count)
                                    print(p)
                                    count = count + 1
                                    command = hello_command + p
                                    if(pow(command)):
                                        break
               